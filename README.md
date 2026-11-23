<div align="center">

<img src="banner.png" alt="Tech Banner" width="100%" style="max-height: 280px; object-fit: cover; border-radius: 6px;" />

# Jean-Marie Renouard 👋

<p align="center"><strong>Principal Data & AI Systems Architect • Lead Maintainer of MySQLTuner • Creator of MicroLLM & FileCleaner • Founder of LightPath</strong></p>

[![Website](https://img.shields.io/badge/Blog-jmrenouard.fr-3b82f6?style=for-the-badge&logo=google-chrome&logoColor=white)](https://jmrenouard.fr)
[![Company](https://img.shields.io/badge/Company-LightPath.fr-10b981?style=for-the-badge)](https://lightpath.fr)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-jmrenouard-0077B5?style=for-the-badge)](https://www.linkedin.com/in/jmrenouard)
[![X / Twitter](https://img.shields.io/badge/X-@jmrenouard-000000?style=for-the-badge&logo=x&logoColor=white)](https://x.com/jmrenouard)
[![SlideShare](https://img.shields.io/badge/SlideShare-jmrenouard-0077B5?style=for-the-badge&logo=slideshare&logoColor=white)](https://www.slideshare.net/jmrenouard)
[![Hugging Face](https://img.shields.io/badge/Hugging%20Face-jmrenouard-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)](https://huggingface.co/jmrenouard)
[![Docker Hub](https://img.shields.io/badge/Docker%20Hub-jmrenouard-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://hub.docker.com/u/jmrenouard)
[![PyPI](https://img.shields.io/badge/PyPI-micro--jev-3775A9?style=for-the-badge&logo=pypi&logoColor=white)](https://pypi.org/project/micro-jev/)
[![GitLab](https://img.shields.io/badge/GitLab-jmrenouard-FC6D26?style=for-the-badge&logo=gitlab&logoColor=white)](https://gitlab.com/jmrenouard)
[![DEV.to](https://img.shields.io/badge/DEV.to-jmrenouard-0A0A0A?style=for-the-badge&logo=devdotto&logoColor=white)](https://dev.to/jmrenouard)
[![Buy Me A Coffee](https://img.shields.io/badge/Buy%20Me%20A%20Coffee-jmrenouard-FFDD00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black)](https://buymeacoffee.com/jmrenouard)
[![Email](https://img.shields.io/badge/Email-contact@lightpath.fr-ea4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:contact@lightpath.fr)

</div>

---

## 🧭 Executive Overview

I am a **Principal Data Architect, Systems Engineer, and Open Source Creator** with over 20 years of hands-on experience designing, tuning, and securing mission-critical database infrastructures, high-throughput platforms, and deterministic AI tooling.

Through my engineering consultancy [**LightPath**](https://lightpath.fr) (founded in 2012), I provide direct, unmediated expertise to international banking institutions, energy giants, national research networks, and large-scale retailers—including **BNP Paribas**, **EDF Datanumia**, **RENATER**, and **E.Leclerc GALEC**—maintaining strict 99.99%+ availability SLAs across multi-terabyte distributed clusters.

My current engineering work spans five pillars: **high-availability & multi-master relational databases** (MySQL, MariaDB Galera, PostgreSQL HA/Multi-Master), **deterministic System-1 AI guardrails** (`MicroLLM`), **zero-dependency CIS/STIG security compliance** (`cis_benchmarks_tools`), **fail-closed Rust & Go systems tooling** (`FileCleaner`, `api_executor`), and **open technical documentation & training standards** (`ASD-STF100`, `lightpath-training-portal`).

---

## ⚡ Key Engineering Metrics

| Metric | Measurement | Impact & Context |
| :--- | :---: | :--- |
| **Field Experience** | `20+ Years` | Deep Linux internals, database engine optimization, and distributed data systems |
| **Global Servers Audited** | `10,000,000+` | Production database instances evaluated worldwide via MySQLTuner algorithms |
| **MySQLTuner Contributions** | `1,723+ Commits` | Primary maintainer and #1 active contributor worldwide to [major/MySQLTuner-perl](https://github.com/major/MySQLTuner-perl) (`9,474` ⭐, `v2.9.4`) |
| **Banking & Cloud Scale** | `600+ DBs • 45 TB` | 23 Cassandra clusters, 600 MongoDB databases, and 120+ AWS RDS instances governed simultaneously |
| **System-1 AI Latency** | `0.013 ms p50 (CPU)` | `MicroLLM v0.4.1`: `12/12` suites (`131,487` decisions in `66.73 s`), `0%` GPU/NPU, `$0.00` API cost |
| **Security Compliance** | `18 Benchmarks • 887 Controls` | `cis_benchmarks_tools v2.10.0`: Pure Python stdlib coverage across 15 DBMS + 3 OS/STIG baselines |
| **PostgreSQL Multi-Master** | `18 Topologies • 628+ Rows` | Empirical `pgbench`/`sysbench`/`tc netem` matrix & 13 Docker labs in `ClusterPostgreSQL-Series` |
| **Rust Systems & Standards** | `94.01% Cov • 53 Rules` | `FileCleaner v1.0.1` (`135` tests, `11,473` lines) & `ASD-STF100 v1.0.0` (`1,293`-entry dictionary) |

---

## 🚀 Featured Major Projects

### 1. [MySQLTuner-perl](https://github.com/major/MySQLTuner-perl) &mdash; *The World Standard for MySQL & MariaDB Tuning*

[![GitHub stars](https://img.shields.io/github/stars/major/MySQLTuner-perl?style=flat-square&color=gold)](https://github.com/major/MySQLTuner-perl)
[![Release](https://img.shields.io/github/v/release/major/MySQLTuner-perl?style=flat-square&color=blue)](https://github.com/major/MySQLTuner-perl/releases)
[![Commits](https://img.shields.io/badge/Contributions-1%2C723%2B%20Commits%20%28%231%29-brightgreen?style=flat-square)](https://github.com/major/MySQLTuner-perl/graphs/contributors)
[![License](https://img.shields.io/badge/License-GPL--3.0-blue?style=flat-square)](https://github.com/major/MySQLTuner-perl/blob/master/LICENSE)

The industry-standard, high-performance database diagnostic and configuration tuning engine written in Perl, executed across millions of production servers worldwide (`9,474` stars, `1,280` forks). As the primary maintainer (`#1` contributor worldwide with `1,723+` commits), `v2.9.4` delivers:
* **1,125 Diagnostic Indicators**: `165` efficiency checks, `322` risk detections, `582` informational telemetry points, and `56` recommendations exported cleanly via `--list-indicators` and core `JSON::PP` (`--agent-json --outputfile`).
* **Deep Engine & TLS Auditing**: Wired auditors for Performance Schema stages, InnoDB Adaptive Hash Index (AHI), table definition cache, and TLS ciphers/protocols via `performance_schema.tls_channel_status` (MySQL `8.4`/`9.7`/`26.10` and MariaDB `10.x`–`13.0+` compatible).
* **Clustering, Containers & MCP**: `discover_cluster_topology` (Galera Cluster quorum, Group Replication, Replicas with NULL/stopped lag detection), `cgroup` v2/v1 memory awareness, PowerShell CIM Windows telemetry, zero-mutation hardening, and a JSON-RPC 2.0 / SSE MCP server with 3 diagnostic skills (`analyze_buffer_pool`, `diagnose_replication_lag`, `detect_fragmented_tables`).

```bash
# Instant zero-installation live execution
wget http://mysqltuner.pl/ -O mysqltuner.pl && perl mysqltuner.pl
```

*Development Fork:* [jmrenouard/MySQLTuner-perl](https://github.com/jmrenouard/MySQLTuner-perl)

---

### 2. [MicroLLM (`micro-jev`)](https://github.com/jmrenouard/MicroLLM) &mdash; *Local Hybrid System-1 Decision Engine & AI Safety Guardrails*

[![PyPI](https://img.shields.io/pypi/v/micro-jev?style=flat-square&color=blue)](https://pypi.org/project/micro-jev/)
[![Hugging Face Models](https://img.shields.io/badge/Hugging%20Face-6%20Models-FFD21E?style=flat-square&logo=huggingface&logoColor=black)](https://huggingface.co/jmrenouard)
[![Inference](https://img.shields.io/badge/Inference-0.013%20ms%20p50%20CPU-success?style=flat-square)](https://microllm.lightpath.fr/)
[![License](https://img.shields.io/badge/License-Apache--2.0-green?style=flat-square)](https://github.com/jmrenouard/MicroLLM/blob/main/LICENSE)

A local, CPU-only System-1 probabilistic decision and guardrail engine built with NumPy, ONNX Runtime INT8, and SafeTensors (`v0.4.1`, `1,371` passing tests at `92%` coverage). Designed for coding agents and API gateways to execute deterministic routing and safety verification at zero GPU cost:
* **Sub-Millisecond CPU Throughput**: `12/12` benchmark suites PASS (`128,713` items / `131,487` decisions in `66.73 s` CPU, `0%` GPU/NPU, `$0.00` API cost); `test_cases_11000` achieves `99.75%` accuracy at `0.013 ms` p50 (`38,917 dec/s`).
* **Conformal Calibration & Guardrail Precision**: RLCD² conformal coverage $(1 - \alpha)$ with certified abstention (`x_abstain`), Neyman-Pearson safety gates ($\alpha \le 0.05$), logit-space `S1-SHAP` counterfactual attribution, and `100.00%` F1 / `0.00%` FPR at `0.280–0.367 ms` p50 against LLM-Judge across `220` tool calls.
* **Agentic Hardening & Multilingual Gear-2**: Inter-clause evidence-competition hijack defense (`x_hijack_suspected`), coding-agent `policy_boundaries` (`allowed`/`forbidden`) with NFKC & remainder-based hazard checks, quadrilingual `EN`/`FR`/`ES`/`PT` support, and portable KeePass vault resolution.
* **Hugging Face Suite & Docs**: `6` ONNX INT8 models ([`microllm-fast-cpu-int8`](https://huggingface.co/jmrenouard/microllm-fast-cpu-int8), [`microllm-guardrail-int8`](https://huggingface.co/jmrenouard/microllm-guardrail-int8), [`microllm-multilingual-int8`](https://huggingface.co/jmrenouard/microllm-multilingual-int8), [`microllm-rlcd2-decision-head`](https://huggingface.co/jmrenouard/microllm-rlcd2-decision-head), [`microllm-multilingual-minilm-int8`](https://huggingface.co/jmrenouard/microllm-multilingual-minilm-int8), [`microllm-multilingual-mdeberta-int8`](https://huggingface.co/jmrenouard/microllm-multilingual-mdeberta-int8)), Gradio Studio ([`microllm-decision-studio`](https://huggingface.co/spaces/jmrenouard/microllm-decision-studio)), `2` datasets ([`microllm-benchmarks`](https://huggingface.co/datasets/jmrenouard/microllm-benchmarks), [`microllm-multilingual-benchmarks`](https://huggingface.co/datasets/jmrenouard/microllm-multilingual-benchmarks)), and docs at [microllm.lightpath.fr](https://microllm.lightpath.fr/).

```bash
pip install micro-jev
microllm guardrail "DROP TABLE users;" --policy strict_enterprise
```

---

### 3. [CIS Benchmarks Tools Suite](https://github.com/jmrenouard/cis_benchmarks_tools) &mdash; *Zero-Dependency Security Compliance Engine*

[![PyPI](https://img.shields.io/pypi/v/cis-benchmarks-tools?style=flat-square&color=blue)](https://pypi.org/project/cis-benchmarks-tools/)
[![Coverage](https://img.shields.io/badge/Coverage-18%20Benchmarks%20%7C%20887%20Controls-orange?style=flat-square)](https://cis-benchmarks.lightpath.fr/)
[![Dependencies](https://img.shields.io/badge/Dependencies-0%20%28Pure%20Python%20Stdlib%29-brightgreen?style=flat-square)](https://github.com/jmrenouard/cis_benchmarks_tools)
[![License](https://img.shields.io/badge/License-GPL--3.0-blue?style=flat-square)](https://github.com/jmrenouard/cis_benchmarks_tools/blob/main/LICENSE)

An automated security compliance auditing engine (`v2.10.0`) built to enforce Center for Internet Security (CIS) Benchmarks and DISA STIG baselines in regulated, air-gapped environments:
* **100% Pure Python 3.8+ Stdlib**: `35` modules (~`25,600` lines, `314` unit tests) with zero external PyPI dependencies, eliminating supply-chain attack surface on isolated banking and critical-infrastructure hosts.
* **18 Benchmarks & 887 Verified Controls**: Covers MariaDB (`10.6`, `10.11`), MySQL Enterprise (`8.0`, `8.4 LTS`, `9.7 Innovation`) & Community (`8.4 LTS`, `9.7 Innovation`), PostgreSQL (`16`, `17`, `18`), MongoDB (`7.0`, `8.0`), Apache Cassandra (`4.0`, `4.1`, `5.0`), and Red Hat Enterprise Linux (`8`, `9`, `10` CIS + DISA STIG).
* **4-Tier Transport & Offline Telemetry**: Evaluates Local shell, Agentless SSH, Local Docker, and Remote SSH+Docker targets with child-env credential protection (`MYSQL_PWD`, `PGPASSWORD`, `CIS_DB_PASSWORD`), EN/FR i18n, and zero-CDN inline SVG HTML/JSON/XML/TXT reports.

```bash
pip install cis-benchmarks-tools
audit-cis --auto-detect --format html --output report.html
```

*Docs & Container:* [cis-benchmarks.lightpath.fr](https://cis-benchmarks.lightpath.fr/) &bull; [Docker Hub](https://hub.docker.com/r/jmrenouard/cis-benchmarks-tools)

---

### 4. [ClusterPostgreSQL-Series](https://github.com/jmrenouard/ClusterPostgreSQL-Series) &mdash; *PostgreSQL Multi-Master & Active-Active Architecture Study*

[![Docs](https://img.shields.io/badge/Docs-postgresql--cluster.lightpath.fr-3b82f6?style=flat-square)](https://postgresql-cluster.lightpath.fr/)
[![Topologies](https://img.shields.io/badge/Matrix-18%20Topologies%20%7C%2040%20Criteria-10B981?style=flat-square)](https://github.com/jmrenouard/ClusterPostgreSQL-Series)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](https://github.com/jmrenouard/ClusterPostgreSQL-Series/blob/main/LICENSE)

A reproducible engineering research suite and Docker Compose benchmark harness evaluating PostgreSQL multi-master, active-active, and distributed SQL topologies:
* **40-Criterion Matrix & Bilingual Study**: Compares `18` topologies (`16` solutions across `19` EN/FR sheets) across `15` bilingual EN+FR chapters (`01`–`14` incl. `03a`/`03b`), paired with `13` `log10` charts and an offline zero-CDN PACELC decision dashboard (`dashboard/index.html`).
* **13 Docker Compose Labs & 18 Deep Probes**: Built atop `multi-db-docker-env` (`v2.6.4`), executing `18` functional/limit probes (`L1–L8`, `T11–T18`) alongside PostgreSQL `18.6` AIO, `uuidv7()`, conflict resolution, and YT `T_REVERT` fault tests.
* **628+ Empirical Benchmark Rows**: Combines `310` baseline (`PG_SCALE=2`) and `318` V5 tuned (`PG_SCALE=20`) `pgbench`/`sysbench`/`tc netem` measurements plus `36` YT Cluster rows—reaching `1,837.64 TPS` (`0` drift) on CRDT `pgedge-delta-apply`, `4,163.31 TPS` on `pg18-birep`, and `189,286.48 TPS` (`0` drift) on `yt-cluster-async`.

```bash
make init-env && make build-bench-image
make up-pgedge && make test-pgedge && make down-pgedge
```

---

### 5. [FileCleaner](https://github.com/jmrenouard/FileCleaner) &mdash; *Fail-Closed Rust Directory Retention & Backup Guardrail Engine*

[![Release](https://img.shields.io/github/v/release/jmrenouard/FileCleaner?style=flat-square&color=blue)](https://github.com/jmrenouard/FileCleaner/releases)
[![Rust](https://img.shields.io/badge/Rust-Edition%202021-000000?style=flat-square&logo=rust&logoColor=white)](https://github.com/jmrenouard/FileCleaner)
[![Docker Hub](https://img.shields.io/badge/Docker%20Hub-filecleaner-2496ED?style=flat-square&logo=docker&logoColor=white)](https://hub.docker.com/r/jmrenouard/filecleaner)
[![License](https://img.shields.io/badge/License-Apache--2.0-green?style=flat-square)](https://github.com/jmrenouard/FileCleaner/blob/main/LICENSE)

A fail-closed systems utility written in pure Rust (`v1.0.1`) engineered for deterministic retention cleanup, compression, and archive rotation around production database dumps and critical storage paths:
* **6-Phase Fail-Closed Pipeline & In-Use Detection**: Enforces a `6`-layer active-file matrix (sidecars, `flock`, `/proc/*/fd`, Windows `share_mode(0)`, `min_idle_age`, `2`-point stability window) before touching any file.
* **Dead-Man's-Switch Backup Guardrails**: Protects backup chains via `min_valid_backup_bytes`, `min_keep_files`, `require_newer_within`, direct `argv` pre-delete hooks (exit `42` veto), and pure-Rust `gzip`/`lz4`/`brotli`/`zip` compression with atomic `.fc-tmp` SHA-256 moves.
* **Daemon Modes & High Assurance**: Ships `interval`, `notify`, and `hybrid` daemon modes across `9` cross-compile targets (`amd64`/`arm64` Docker images), backed by `135` active tests, `6/6` PostgreSQL 17 + MinIO E2E checks, `94.01%` line coverage across `11,473` lines (`cargo llvm-cov`), and `0` Clippy warnings.

```bash
docker run --rm jmrenouard/filecleaner:latest --version
filecleaner init --output filecleaner.toml --profile backups --format toml && filecleaner plan -c filecleaner.toml --json
```

*Documentation:* [filecleaner.lightpath.fr](https://filecleaner.lightpath.fr/)

---

### 6. [ASD-STF100](https://github.com/jmrenouard/asd-stf100) &mdash; *Open Simplified Technical French Specification & Linter*

[![Version](https://img.shields.io/badge/Spec-v1.0.0-blue?style=flat-square)](https://github.com/jmrenouard/asd-stf100)
[![Rules](https://img.shields.io/badge/Standard-53%20Rules%20%7C%201%2C293%20Dict%20Entries-10B981?style=flat-square)](https://github.com/jmrenouard/asd-stf100)
[![Dependencies](https://img.shields.io/badge/Python%20CLI-0%20Runtime%20Deps-brightgreen?style=flat-square)](https://github.com/jmrenouard/asd-stf100)
[![License](https://img.shields.io/badge/License-MIT%20%2B%20CC--BY--SA--4.0-blue?style=flat-square)](https://github.com/jmrenouard/asd-stf100/blob/main/LICENSE)

An open-source controlled-language standard (`v1.0.0`) bringing structured procedural clarity to French operational runbooks, maintenance procedures, and safety instructions (independent open specification, not affiliated with ASD):
* **Formal Rulebook & Controlled Dictionary**: Defines `53` French procedural and descriptive rules across `9` sections (`1.1`–`9.4`), `8` general recommendations (`GR-1`–`GR-8`), `22` noun and `4` verb categories, and a `1,293`-entry JSON dictionary (`spec/*.json` + ReportLab A4 PDF `dist/ASD-STF100_ISSUE1.pdf`).
* **Zero-Dependency Linter (`stf-check`)**: Pure Python `>= 3.10` CLI auditing procedural/descriptive modes alongside `Vale STF100` rules and `5` pytest verification suites.
* **French Diátaxis Docs-as-Code & Agent Skills**: Includes `diataxis-fr-scaffold`, `diataxis-fr-check --strict --check-stf`, and `2` installable Agent Skills (`francais-technique-simplifie`, `diataxis-docs-fr`).

```bash
git clone https://github.com/jmrenouard/asd-stf100.git && cd asd-stf100 && pip install -e ".[pdf,dev]"
stf-check --mode procedural docs/02-guides-pratiques/rediger-procedure-stf100.md
```

---

### 7. [LightPath Training Portal](https://github.com/jmrenouard/lightpath-training-portal) &mdash; *Zero-Dependency PHP 8.3 LMS with Live Docker SQL Labs*

[![Release](https://img.shields.io/github/v/release/jmrenouard/lightpath-training-portal?style=flat-square&color=blue)](https://github.com/jmrenouard/lightpath-training-portal/releases)
[![PHP](https://img.shields.io/badge/PHP-%3E%3D%208.3%20%280%20Runtime%20Deps%29-777BB4?style=flat-square&logo=php&logoColor=white)](https://github.com/jmrenouard/lightpath-training-portal)
[![Standards](https://img.shields.io/badge/Compliance-SCORM%201.2%20%7C%20Qualiopi-10B981?style=flat-square)](https://www.lightpath.fr)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](https://github.com/jmrenouard/lightpath-training-portal/blob/main/LICENSE)

A lightweight, self-hosted Learning Management System (`v2.0.0`) written in zero-dependency PHP `>= 8.3` with strict zero-CDN Content Security Policy (`style-src 'self'`, SHA-256 `script-src`) and dual `JsonStorage` / transactional `PdoStorage` (`pgsql`/`mysql`/`sqlite`):
* **Per-Learner Docker PostgreSQL 18 Sandboxes**: Provisions isolated `lp_pg18_user_<id>` containers (`12` Sakila tables, `4` `pgbench` tables / `1,000` accounts, plus `cloud_simulated` fallback) with an interactive SQL workbench, automated boolean oracle checks, and chaos scenarios.
* **Qualiopi & SCORM 1.2 Automation**: Covers the full `7`-pillar Qualiopi audit trail (`15`-Q diagnostic, dual-signed attendance, `40`-Q exam at `75%` pass threshold, CSPRNG QR certificates, J+60 surveys, OPCO CSV) and outbound **SCORM 1.2** `.zip` exports.
* **Verified Multi-Course Scale**: Configurable via `10` feature flags (`4` profiles) and `LMS_COURSE_ROOT` scaling from bundled demo packs to `34`-module PostgreSQL 18 curricula (`727/727` Mode A, `741/741` Mode B, `405/405` HTTP tests + Playwright E2E).

```bash
cp .env.example .env && docker compose up -d
php bin/lab-runner.php list
```

---

### 8. [API Executor (`go-admin-tool`)](https://github.com/jmrenouard/api_executor) &mdash; *Zero-Trust Remote Task Platform in Go*

[![Release](https://img.shields.io/github/v/release/jmrenouard/api_executor?style=flat-square&color=blue)](https://github.com/jmrenouard/api_executor/releases)
[![Go](https://img.shields.io/badge/Go-1.24%2B-00ADD8?style=flat-square&logo=go&logoColor=white)](https://github.com/jmrenouard/api_executor)
[![Protocol](https://img.shields.io/badge/Protocol-MCP%202024--11--05-10B981?style=flat-square)](https://api-executor.lightpath.fr/)
[![License](https://img.shields.io/badge/License-GPL--3.0-blue?style=flat-square)](https://github.com/jmrenouard/api_executor/blob/main/LICENSE)

An enterprise Zero-Trust remote task execution and automation platform written in Go `1.24.3` (`v2.1.0`), verified by `88/88` E2E and `464` unit/integration tests:
* **Model Context Protocol (MCP) & Async Queue**: Native MCP JSON-RPC 2.0 (`2024-11-05`) interface with Human-in-the-Loop (HITL) gating, SHA-256 hash-chained audit/trace replay, and priority job queue (`POST /api/v1/jobs`, `High`/`Normal`/`Low` heap, Web Console).
* **Zero-Trust Security & Telemetry**: HTTPS/TLS 1.3 by default with atomic certificate rotation, RBAC + PATs + service accounts, and Prometheus per-action/mode metrics.
* **305 Automation Plugins**: `24` Go native + `281` YAML plugins across `10` operational domains with Ubuntu/Debian and RHEL/UBI9 OS presets, docs at [api-executor.lightpath.fr](https://api-executor.lightpath.fr/), and images on [Docker Hub](https://hub.docker.com/r/jmrenouard/api_executor).

---

### 9. Production DataLabs, Migration & DBA Utilities

* [**multi-db-docker-env**](https://github.com/jmrenouard/multi-db-docker-env) (`v2.6.4`, `GPL-3.0`): Unified Go CLI (`./mdb` / `mdb.cmd`) orchestrating **31 active E2E-verified environments** (`11` standalone + `20` cluster/HA/multi-master) covering MySQL `8.4`/`9.7`, MariaDB `10.11`–`12.3` (Galera & Replication), Percona `8.4`, PostgreSQL `15`–`18` (Patroni, PgPool-II, pgEdge/Spock 5, Bucardo, Citus `14.2`, YT-Cluster, CockroachDB `v25.4`, YugabyteDB `2026.1.3`), and MongoDB `7.0`/`8.0` with Traefik v3 and HAProxy LTS.
* [**dbscripts**](https://github.com/jmrenouard/dbscripts) (`v1.0.0`, `GPL-3.0`): Multi-vendor DBA automation suite for MariaDB/Galera, MySQL, PostgreSQL, MongoDB, Cassandra, and Oracle—bundling `18` operational scripts (`mbbackup.sh`/`mbrestore.sh`, `mysqldump_database_splitter.py`, `show_cql_grants.py`, `ora2mariadb.sh`), `17` Ansible playbooks/roles, `8` Docker labs (`mysql_docker.py`, 3-node Galera+HAProxy), and `11` SQL scripts (`60/60` unit tests).
* [**patroni-lab-rhel8**](https://github.com/jmrenouard/patroni-lab-rhel8) (`GPL-3.0`): Automated PostgreSQL `17` High Availability cluster testbed on Red Hat UBI 8 orchestrating Patroni, `etcd`, HAProxy, and PgBouncer with end-to-end TLS & mTLS.
* [**pg_logical_migrator**](https://github.com/jmrenouard/pg_logical_migrator) (`v1.4.1`, `MIT`): Python `3.9+` automated `17`-step logical replication orchestrator for near-zero-downtime PostgreSQL migrations (LOB & `UNLOGGED` tables sync, SQL/shell hardening, HTML reports), published on [Docker Hub](https://hub.docker.com/r/jmrenouard/pg_logical_migrator).
* [**grafana-tools**](https://github.com/jmrenouard/grafana-tools) (`v1.0.1`, `GPL-3.0`): Python CLI and Ansible playbooks shipping `20+` pre-built YAML observability dashboards for MySQL, PostgreSQL, MongoDB, Cassandra, and Linux, published on [Docker Hub](https://hub.docker.com/r/jmrenouard/grafana-tools).

---

## 🛠️ Technical Domains & Stack

<table>
  <tr>
    <td width="25%"><strong>Databases &amp; Storage</strong></td>
    <td>
      <img src="https://img.shields.io/badge/MySQL%208.4%20%2F%209.x-4479A1?style=flat-square&logo=mysql&logoColor=white" />
      <img src="https://img.shields.io/badge/PostgreSQL%2018-4169E1?style=flat-square&logo=postgresql&logoColor=white" />
      <img src="https://img.shields.io/badge/MariaDB%20Galera-003545?style=flat-square&logo=mariadb&logoColor=white" />
      <img src="https://img.shields.io/badge/Apache%20Cassandra-1287B1?style=flat-square&logo=apachecassandra&logoColor=white" />
      <img src="https://img.shields.io/badge/MongoDB-47A248?style=flat-square&logo=mongodb&logoColor=white" />
      <img src="https://img.shields.io/badge/Redis-DC382D?style=flat-square&logo=redis&logoColor=white" />
      <img src="https://img.shields.io/badge/CockroachDB%20%2F%20YugabyteDB-6933FF?style=flat-square" />
    </td>
  </tr>
  <tr>
    <td><strong>AI &amp; Guardrails</strong></td>
    <td>
      <img src="https://img.shields.io/badge/MicroLLM%20%28micro--jev%29-00F2FE?style=flat-square&logo=fastapi&logoColor=black" />
      <img src="https://img.shields.io/badge/Conformal%20Prediction-RLCD%C2%B2-8B5CF6?style=flat-square" />
      <img src="https://img.shields.io/badge/ONNX%20Runtime%20INT8-005CED?style=flat-square&logo=onnx&logoColor=white" />
      <img src="https://img.shields.io/badge/SafeTensors-FFA800?style=flat-square&logo=huggingface&logoColor=black" />
      <img src="https://img.shields.io/badge/Model%20Context%20Protocol-MCP-10B981?style=flat-square" />
      <img src="https://img.shields.io/badge/AI%20Safety-Neyman--Pearson-EF4444?style=flat-square" />
    </td>
  </tr>
  <tr>
    <td><strong>Platform &amp; DevOps</strong></td>
    <td>
      <img src="https://img.shields.io/badge/Terraform-7B42BC?style=flat-square&logo=terraform&logoColor=white" />
      <img src="https://img.shields.io/badge/Ansible-EE0000?style=flat-square&logo=ansible&logoColor=white" />
      <img src="https://img.shields.io/badge/Kubernetes-326CE5?style=flat-square&logo=kubernetes&logoColor=white" />
      <img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white" />
      <img src="https://img.shields.io/badge/ArgoCD-EF7B4D?style=flat-square&logo=argo&logoColor=white" />
      <img src="https://img.shields.io/badge/CIS%20%26%20DISA%20STIG-1E293B?style=flat-square" />
      <img src="https://img.shields.io/badge/GitLab%20CI%2FCD-FC6D26?style=flat-square&logo=gitlab&logoColor=white" />
    </td>
  </tr>
  <tr>
    <td><strong>Languages &amp; Systems</strong></td>
    <td>
      <img src="https://img.shields.io/badge/Rust-000000?style=flat-square&logo=rust&logoColor=white" />
      <img src="https://img.shields.io/badge/Go%201.24%2B-00ADD8?style=flat-square&logo=go&logoColor=white" />
      <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" />
      <img src="https://img.shields.io/badge/PHP%208.3-777BB4?style=flat-square&logo=php&logoColor=white" />
      <img src="https://img.shields.io/badge/Perl-39457E?style=flat-square&logo=perl&logoColor=white" />
      <img src="https://img.shields.io/badge/Bash%20%2F%20POSIX-4EAA25?style=flat-square&logo=gnubash&logoColor=white" />
      <img src="https://img.shields.io/badge/Linux%20Kernel%20%26%20eBPF-FCC624?style=flat-square&logo=linux&logoColor=black" />
      <img src="https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white" />
    </td>
  </tr>
  <tr>
    <td><strong>Cloud &amp; Observability</strong></td>
    <td>
      <img src="https://img.shields.io/badge/AWS%20%28RDS%2C%20Aurora%2C%20EKS%29-232F3E?style=flat-square" />
      <img src="https://img.shields.io/badge/Google%20Cloud%20Platform-4285F4?style=flat-square&logo=googlecloud&logoColor=white" />
      <img src="https://img.shields.io/badge/Microsoft%20Azure-0078D4?style=flat-square" />
      <img src="https://img.shields.io/badge/Prometheus-E6522C?style=flat-square&logo=prometheus&logoColor=white" />
      <img src="https://img.shields.io/badge/Grafana-F46800?style=flat-square&logo=grafana&logoColor=white" />
      <img src="https://img.shields.io/badge/Datadog-632CA6?style=flat-square&logo=datadog&logoColor=white" />
    </td>
  </tr>
</table>

---

## 📚 Publications & Technical Writing

* **Published Technical Book**: [*PHP - Améliorez la performance de vos applications*](https://www.eyrolles.com/Informatique/Livre/php-ameliorez-la-performance-de-vos-applications-9782746058941/) (Éditions ENI, ISBN 978-2-7460-5894-1). An engineering guide on backend response-time tuning, memory profiling, and database access-layer optimization.
* **Linux Hardening & Security Guide v2.0**: Enterprise OS security engineering covering RHEL 9 / Ubuntu 24.04, `nftables`, LUKS2, AIDE SHA-512, OpenSSH FIDO2, and `systemd` sandboxing — [Online Article](https://www.jmrenouard.fr/en/programmation-en/linux-hardening-security-guide-v2-0-modern-os-nftables-openssh-fido2-and-systemd-sandboxing) &bull; [PDF Edition](https://www.lightpath.fr/downloads/Linux-Hardening-Security-Guide-2.0-EN.pdf).
* **ClusterPostgreSQL-Series Study**: Comparative PostgreSQL multi-master & active-active study across `18` topologies, `40` criteria, `15` bilingual EN+FR chapters (`01`–`14` incl. `03a`/`03b`), and `628+` empirical benchmarks on [postgresql-cluster.lightpath.fr](https://postgresql-cluster.lightpath.fr/).
* **ASD-STF100 Open Specification (Issue 1)**: Open Simplified Technical French standard (`53` rules, `1,293`-entry dictionary, French Diátaxis Docs-as-Code toolkit) at [jmrenouard/asd-stf100](https://github.com/jmrenouard/asd-stf100).
* **MySQLTuner Technical Series**: In-depth articles covering MariaDB Galera quorum diagnostics, InnoDB Buffer Pool contention analysis, and AI-ready JSON/MCP outputs on [jmrenouard.fr](https://jmrenouard.fr).
* **MicroLLM & System-1 Decision Architecture**: Research and documentation on conformal prediction calibration, `S1-SHAP` attribution, Neyman-Pearson safety gates, and sub-millisecond CPU inference at [microllm.lightpath.fr](https://microllm.lightpath.fr/).
* **Zero-Downtime PostgreSQL Migrations**: Architectural blueprints on parallel physical and logical replication workflows (`pgcopydb`, `pg_logical_migrator`).
* **Conference Presentations**: Technical slide decks hosted on [SlideShare](https://www.slideshare.net/jmrenouard).

---

## 📊 GitHub Analytics

<div align="center">

<img src="https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=jmrenouard&theme=nord_dark" alt="Profile Details" /><br/>
<img src="https://github-profile-summary-cards.vercel.app/api/cards/repos-per-language?username=jmrenouard&theme=nord_dark" alt="Repos per Language" />
<img src="https://github-profile-summary-cards.vercel.app/api/cards/most-commit-language?username=jmrenouard&theme=nord_dark" alt="Most Commits by Language" /><br/>
<img src="https://github-profile-summary-cards.vercel.app/api/cards/stats?username=jmrenouard&theme=nord_dark" alt="Stats" />
<img src="https://github-profile-summary-cards.vercel.app/api/cards/productive-time?username=jmrenouard&theme=nord_dark" alt="Productive Time" /><br/>
<img src="https://github-readme-streak-stats.herokuapp.com/?user=jmrenouard&theme=tokyonight" alt="GitHub Streak" />

</div>

---

## 💡 Motivations & Drives

Outside of solving complex database performance bottlenecks and architecting AI decision engines, my daily energy stems from (in strict hierarchical order):
1. ❤️ **My Wife & Children**
2. 🤝 **My Friends**
3. 💻 **Coding & Open Source Contributions**
4. 🐶 **My Dog**
5. 🗣️ **Endless Technical Speeches & Unbreakable Enthusiasm**
6. 🧠 **The Million Projects Running in My Head**

---

## ☕ Support & Contact

If my open-source tools or diagnostics saved your production cluster during an outage, helped optimize your queries, or accelerated your pipeline, consider fueling my next late-night coding session!

<div align="center">

[![Buy Me A Coffee](https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png)](https://buymeacoffee.com/jmrenouard)

**Direct Consulting Inquiries:** [contact@lightpath.fr](mailto:contact@lightpath.fr) &bull; [https://lightpath.fr](https://lightpath.fr)

</div>
