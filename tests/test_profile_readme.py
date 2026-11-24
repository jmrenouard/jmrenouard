#!/usr/bin/env python3
"""Offline integrity and hygiene tests for the jmrenouard GitHub profile repository (100% PSL)."""

from __future__ import annotations

import os
import re
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"

_BOX_DRAW_RE = re.compile(r"[\u2500-\u257f]")
_MERMAID_HEADERS = (
    "flowchart",
    "graph",
    "sequencediagram",
    "classdiagram",
    "statediagram",
    "erdiagram",
    "gantt",
    "pie",
    "gitgraph",
    "mindmap",
    "timeline",
)
_IMAGE_MAGICS = (
    b"\x89PNG\r\n\x1a\n",
    b"\xff\xd8\xff",
    b"GIF87a",
    b"GIF89a",
    b"RIFF",
    b"<svg",
)
_FRENCH_PROSE_RE = re.compile(
    r"\b(?:dans|avec|pour|vos|votre|notre|cette|sont|depuis|tutoriel|guides|prérequis|vérification)\b",
    re.IGNORECASE,
)
_SECRET_RE = re.compile(
    r"(?:BEGIN\s+(?:RSA|OPENSSH|EC|DSA)?\s*PRIVATE\s+KEY|"
    r"(?:api[_-]?key|secret|password|token)\s*[:=]\s*['\"][A-Za-z0-9_\-/+=]{12,}['\"]|"
    r"\.kdbx\b|\.keyx\b)",
    re.IGNORECASE,
)
_LOCAL_PATH_RE = re.compile(
    r"(?:/home/jmren\b|[A-Za-z]:\\Users\\jmren\b|file:///)",
    re.IGNORECASE,
)


def _extract_fenced_blocks(text: str) -> list[tuple[int, int, str, str]]:
    """Return (start_line, indent, lang, body) tuples for closed fenced blocks."""
    blocks: list[tuple[int, int, str, str]] = []
    current: tuple[int, int, str, list[str]] | None = None
    for lineno, line in enumerate(text.splitlines(), 1):
        fence_match = re.match(r"^( *)```(.*)$", line)
        if fence_match and current is None:
            current = (lineno, len(fence_match.group(1)), fence_match.group(2).strip().lower(), [])
        elif fence_match and current is not None and not fence_match.group(2).strip():
            blocks.append((current[0], current[1], current[2], "\n".join(current[3])))
            current = None
        elif current is not None:
            current[3].append(line)
    return blocks


def _run_mmdc_svg(mermaid_src: str) -> tuple[bool, str]:
    """Compile a Mermaid diagram with native mmdc or WSL mmdc if available."""
    native_mmdc = shutil.which("mmdc")
    wsl_bin = shutil.which("wsl") if os.name == "nt" else None
    if not native_mmdc and not wsl_bin:
        return True, "mmdc_unavailable"

    with tempfile.TemporaryDirectory() as tmp:
        in_path = Path(tmp) / "diagram.mmd"
        out_path = Path(tmp) / "diagram.svg"
        in_path.write_text(mermaid_src, encoding="utf-8")

        if native_mmdc:
            cmd = [native_mmdc, "-i", str(in_path), "-o", str(out_path)]
        else:
            assert wsl_bin is not None
            drive = in_path.drive.rstrip(":").lower()
            wsl_in = f"/mnt/{drive}{in_path.as_posix()[2:]}"
            wsl_out = f"/mnt/{drive}{out_path.as_posix()[2:]}"
            cmd = [
                wsl_bin,
                "bash",
                "-lc",
                f"command -v mmdc >/dev/null 2>&1 || exit 127; mmdc -i '{wsl_in}' -o '{wsl_out}'",
            ]
        proc = subprocess.run(cmd, capture_output=True, text=True, check=False)
        if proc.returncode == 127:
            return True, "mmdc_unavailable"
        if proc.returncode != 0 or not out_path.is_file():
            return False, (proc.stderr or proc.stdout).strip()
        return "<svg" in out_path.read_text("utf-8", errors="replace"), "compiled"


class TestProfileReadme(unittest.TestCase):
    """Validate profile README assets, links, diagrams, language, and hygiene."""

    def test_local_assets_and_relative_links_exist(self) -> None:
        self.assertTrue(README.is_file())
        self.assertFalse((ROOT / "home.md").exists(), "Unused Wiki.js home.md stub must remain deleted")
        text = README.read_text("utf-8")

        raw_targets = re.findall(r'!?\[[^\]]*\]\(([^)\n]+)\)', text)
        raw_targets.extend(re.findall(r'(?:src|href)=["\']([^"\']+)["\']', text))
        self.assertTrue(any("banner.png" in tgt for tgt in raw_targets))

        for raw in raw_targets:
            target = unquote(raw.strip().split("#", 1)[0].split("?", 1)[0])
            if not target or target.startswith(("http://", "https://", "mailto:")):
                continue
            resolved = (ROOT / target).resolve()
            self.assertTrue(resolved.exists(), f"Missing local target: {target}")
            if resolved.suffix.lower() in {".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg"}:
                head = resolved.read_bytes()[:64]
                self.assertGreater(len(head), 8, f"Empty image file: {target}")
                self.assertTrue(
                    any(head.lstrip().startswith(sig) for sig in _IMAGE_MAGICS),
                    f"Unrecognized image header in {target}: {head[:12]!r}",
                )

    def test_zero_ascii_diagrams_and_valid_mermaid(self) -> None:
        md_files = [p for p in sorted(ROOT.rglob("*.md")) if ".git" not in p.parts]
        self.assertEqual(md_files, [README], f"Unexpected markdown files found: {md_files}")

        mermaid_blocks: list[str] = []
        for md in md_files:
            text = md.read_text("utf-8")
            self.assertIsNone(_BOX_DRAW_RE.search(text), f"Box-drawing characters found in {md.name}")
            for lineno, indent, lang, body in _extract_fenced_blocks(text):
                if lang == "mermaid":
                    self.assertEqual(indent, 0, f"Indented mermaid fence at {md.name}:{lineno}")
                    self.assertNotIn("<br", body.lower(), f"HTML <br> in mermaid at {md.name}:{lineno}")
                    first = next((ln.strip().lower() for ln in body.splitlines() if ln.strip()), "")
                    self.assertTrue(
                        any(first.startswith(hdr) for hdr in _MERMAID_HEADERS),
                        f"Invalid Mermaid diagram header at {md.name}:{lineno}: {first!r}",
                    )
                    mermaid_blocks.append(body)
                elif lang in {"", "text", "ascii"}:
                    self.assertNotRegex(
                        body,
                        r"(?:\+[-=]{2,}\+|-->|<--)",
                        f"ASCII diagram found inside fence at {md.name}:{lineno}",
                    )

        self.assertGreaterEqual(len(mermaid_blocks), 1)
        for idx, block in enumerate(mermaid_blocks, 1):
            ok, detail = _run_mmdc_svg(block)
            if detail == "mmdc_unavailable":
                continue
            self.assertTrue(ok, f"mmdc compilation failed on Mermaid block #{idx}: {detail}")

    def test_english_only_and_zero_french_prose_leakage(self) -> None:
        text = README.read_text("utf-8")
        allowed_french_title = "PHP - Améliorez la performance de vos applications"
        self.assertIn(allowed_french_title, text)

        in_fence = False
        for lineno, raw_line in enumerate(text.splitlines(), 1):
            if raw_line.strip().startswith("```"):
                in_fence = not in_fence
                continue
            if in_fence:
                continue
            cleaned = raw_line.replace(allowed_french_title, "")
            cleaned = re.sub(r"https?://[^\s)\"'>]+", "", cleaned)
            cleaned = re.sub(r"`[^`]+`", "", cleaned)
            self.assertIsNone(
                _FRENCH_PROSE_RE.search(cleaned),
                f"Unexpected French prose token on README.md:{lineno}: {cleaned!r}",
            )

    def test_markdown_structure_tables_fences_and_url_hygiene(self) -> None:
        text = README.read_text("utf-8")
        lines = text.splitlines()
        fence_markers = [ln for ln in lines if re.match(r"^\s*```", ln)]
        self.assertEqual(len(fence_markers) % 2, 0, "Unbalanced fenced code blocks in README.md")
        self.assertRegex(text, r"(?m)^#\s+Jean-Marie Renouard")

        for tag in ("table", "tr", "td"):
            opens = len(re.findall(rf"<{tag}\b", text, re.IGNORECASE))
            closes = len(re.findall(rf"</{tag}>", text, re.IGNORECASE))
            self.assertEqual(opens, closes, f"Unbalanced <{tag}> tags: {opens} != {closes}")

        self.assertNotIn("\\operatorname", text)
        for lineno, line in enumerate(lines, 1):
            cleaned_line = re.sub(r"`[^`]+`", "", line)
            for match in re.finditer(r"(?<!\$)\$(?!\$)([^\n$]+?)(?<!\$)\$(?!\$)", cleaned_line):
                inner = match.group(1)
                self.assertFalse(
                    inner.startswith(" ") or inner.endswith(" "),
                    f"Loose inline math spacing at README.md:{lineno}: ${inner}$",
                )

        urls = re.findall(r'(?:href=|src=|\]\()(https?://[^)\s"\'<>]+)', text)
        self.assertGreater(len(urls), 50)
        for url in urls:
            self.assertNotIn("[", url)
            self.assertNotIn("]", url)

    def test_zero_secrets_or_local_filesystem_leaks(self) -> None:
        text_suffixes = {".md", ".txt", ".yml", ".yaml", ".json", ".sh", ".py"}
        candidates = [
            p for p in sorted(ROOT.rglob("*"))
            if p.is_file() and ".git" not in p.parts and p != Path(__file__) and p.suffix.lower() in text_suffixes
        ]
        for path in candidates:
            content = path.read_text("utf-8")
            self.assertIsNone(_SECRET_RE.search(content), f"Potential secret leak in {path.name}")
            self.assertIsNone(_LOCAL_PATH_RE.search(content), f"Local path leak in {path.name}")


if __name__ == "__main__":
    unittest.main()
