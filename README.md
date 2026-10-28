<div align="center">

<img src="banner.png" alt="Tech Banner" width="100%" style="max-height: 280px; object-fit: cover; border-radius: 6px;" />

# Jean-Marie Renouard 👋

<p align="center"><strong>Principal Data & AI Systems Architect • Creator of MicroLLM • Lead Maintainer of MySQLTuner • Founder of LightPath</strong></p>

[![Website](https://img.shields.io/badge/Blog-jmrenouard.fr-3b82f6?style=for-the-badge&logo=google-chrome&logoColor=white)](https://jmrenouard.fr)
[![Company](https://img.shields.io/badge/Company-LightPath.fr-10b981?style=for-the-badge)](https://lightpath.fr)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-jmrenouard-0077B5?style=for-the-badge)](https://www.linkedin.com/in/jmrenouard)
[![X / Twitter](https://img.shields.io/badge/X-@jmrenouard-000000?style=for-the-badge&logo=x&logoColor=white)](https://x.com/jmrenouard)
[![SlideShare](https://img.shields.io/badge/SlideShare-jmrenouard-0077B5?style=for-the-badge&logo=slideshare&logoColor=white)](https://www.slideshare.net/jmrenouard)
[![Hugging Face](https://img.shields.io/badge/Hugging%20Face-jmrenouard-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)](https://huggingface.co/jmrenouard)
[![Docker Hub](https://img.shields.io/badge/Docker%20Hub-jmrenouard-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://hub.docker.com/u/jmrenouard)
[![PyPI](https://img.shields.io/badge/PyPI-microllm--jev-3775A9?style=for-the-badge&logo=pypi&logoColor=white)](https://pypi.org/project/microllm-jev/)
[![GitLab](https://img.shields.io/badge/GitLab-jmrenouard-FC6D26?style=for-the-badge&logo=gitlab&logoColor=white)](https://gitlab.com/jmrenouard)
[![DEV.to](https://img.shields.io/badge/DEV.to-jmrenouard-0A0A0A?style=for-the-badge&logo=devdotto&logoColor=white)](https://dev.to/jmrenouard)
[![Buy Me A Coffee](https://img.shields.io/badge/Buy%20Me%20A%20Coffee-jmrenouard-FFDD00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black)](https://buymeacoffee.com/jmrenouard)
[![Email](https://img.shields.io/badge/Email-contact@lightpath.fr-ea4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:contact@lightpath.fr)

</div>

---

## 🧭 Executive Overview

I am a **Principal Data Architect, Systems Engineer, and Open Source Creator** with over 20 years of hands-on experience designing, tuning, and securing mission-critical database infrastructures and high-throughput systems.

Through my engineering consultancy [**LightPath**](https://lightpath.fr) (founded in 2012), I provide direct, unmediated expertise to international banking institutions, energy giants, national research networks, and large-scale retailers—including **BNP Paribas**, **EDF Datanumia**, **RENATER**, and **E.Leclerc GALEC**—maintaining strict 99.99%+ availability SLAs across multi-terabyte distributed clusters.

My current engineering focus unites **high-performance relational & NoSQL storage engines**, **cloud-native platform automation (GitOps, Kubernetes, IaC)**, and **deterministic System-1 AI architectures (MicroLLM)** delivering certified sub-5ms CPU inference and conformal safety guardrails for autonomous agentic workflows.

---

## ⚡ Key Engineering Metrics

| Metric | Measurement | Impact & Context |
| :--- | :---: | :--- |
| **Field Experience** | `20+ Years` | Deep Linux internals, database engine optimization, and distributed data systems |
| **Global Servers Audited** | `10,000,000+` | Production database instances evaluated worldwide via MySQLTuner algorithms |
| **MySQLTuner Contributions** | `1,691+ Commits` | Primary maintainer and #1 active contributor worldwide to [major/MySQLTuner-perl](https://github.com/major/MySQLTuner-perl) (9,470+ ⭐) |
| **Banking & Cloud Scale** | `600+ DBs • 45 TB` | 23 Cassandra clusters, 600 MongoDB databases, and 120+ AWS RDS instances governed simultaneously |
| **System-1 AI Latency** | `< 5 ms (CPU)` | INT8 zero-shot inference and Neyman-Pearson safety verification with zero GPU requirement |
| **Security Auditing** | `887 Controls` | Automated compliance coverage across 18 official CIS Benchmarks and DISA STIGs |

---

## 🚀 Featured Major Projects

### 1. [MySQLTuner-perl](https://github.com/major/MySQLTuner-perl) &mdash; *The World Standard for MySQL & MariaDB Tuning*

[![GitHub stars](https://img.shields.io/github/stars/major/MySQLTuner-perl?style=flat-square&color=gold)](https://github.com/major/MySQLTuner-perl)
[![Commits](https://img.shields.io/badge/Contributions-1%2C691%2B%20Commits%20%28%231%29-brightgreen?style=flat-square)](https://github.com/major/MySQLTuner-perl/graphs/contributors)
[![License](https://img.shields.io/badge/License-GPL--3.0-blue?style=flat-square)](https://github.com/major/MySQLTuner-perl/blob/master/LICENSE)

The industry-standard, high-performance database diagnostic and configuration tuning engine written in Perl, executed over 15,000 times weekly across millions of production database servers worldwide. As the primary maintainer (#1 contributor worldwide with 1,691+ commits), I have architected its modern capabilities:
* **Deep Engine Internals**: Comprehensive InnoDB Buffer Pool heuristics, adaptive hash indexes, redo log contention, and thread pool analysis.
* **Clustering & High Availability**: Galera Cluster quorum validation, split-brain detection, flow control monitoring, and InnoDB Cluster telemetry.
* **Modern AI & Agentic Integration**: Interactive standalone HTML dashboard reports, machine-actionable JSON output, and native Model Context Protocol (MCP) server integration for automated AI database operations.

```bash
# Instant zero-installation live execution
wget http://mysqltuner.pl/ -O mysqltuner.pl && perl mysqltuner.pl
```

*Development Fork:* [jmrenouard/MySQLTuner-perl](https://github.com/jmrenouard/MySQLTuner-perl)

---

### 2. [MicroLLM (`microllm-jev`)](https://github.com/jmrenouard/MicroLLM) &mdash; *Local Hybrid System-1 Decision Engine & AI Safety Guardrails*

[![PyPI](https://img.shields.io/pypi/v/microllm-jev?style=flat-square&color=blue)](https://pypi.org/project/microllm-jev/)
[![Hugging Face Models](https://img.shields.io/badge/Hugging%20Face-4%20Models-FFD21E?style=flat-square&logo=huggingface&logoColor=black)](https://huggingface.co/jmrenouard)
[![Inference](https://img.shields.io/badge/Inference-Sub--5ms%20CPU-success?style=flat-square)](https://github.com/jmrenouard/MicroLLM)
[![License](https://img.shields.io/badge/License-Apache--2.0-green?style=flat-square)](https://github.com/jmrenouard/MicroLLM/blob/main/LICENSE)

A high-speed, local CPU-only System-1 probabilistic decision and guardrail engine built with NumPy, ONNX Runtime INT8, and SafeTensors. Designed for AI agents and high-throughput API gateways to offload 85% to 92% of deterministic classification and safety decisions in under 5 milliseconds without consuming expensive GPU resources:
* **Sub-5ms Inference Pipeline**: Combines AnyJev L0 lexical pre-filtering (< 1 ms), calibrated linear heads, and quantized INT8 embeddings on standard x86_64 / ARM64 CPUs.
* **Conformal Calibration (RLCD²)**: Strictly calibrated confidence scores (Expected Calibration Error `ECE = 0.008`, `Brier score = 0.021`) with guaranteed coverage $(1 - \alpha)$ and certified abstention (`x_abstain`).
* **Neyman-Pearson Safety Gates**: Bounded false-positive rate ($\alpha \le 0.05$) with 97.4% recall against Prompt Injections, PII leakage, and destructive SQL statements (`DROP`, `TRUNCATE`).
* **Hugging Face Suite**: Published suite of 4 official ONNX INT8 models ([`microllm-fast-cpu-int8`](https://huggingface.co/jmrenouard/microllm-fast-cpu-int8), [`microllm-guardrail-int8`](https://huggingface.co/jmrenouard/microllm-guardrail-int8), [`microllm-multilingual-int8`](https://huggingface.co/jmrenouard/microllm-multilingual-int8), [`microllm-rlcd2-decision-head`](https://huggingface.co/jmrenouard/microllm-rlcd2-decision-head)) and an interactive Gradio Studio ([`microllm-decision-studio`](https://huggingface.co/spaces/jmrenouard/microllm-decision-studio)).

```bash
pip install microllm-jev
microllm guardrail "DROP TABLE users;" --policy strict_enterprise
```

---

### 3. [CIS Benchmarks Tools Suite](https://github.com/jmrenouard/cis_benchmarks_tools) &mdash; *Zero-Dependency Security Compliance Engine*

[![PyPI](https://img.shields.io/pypi/v/cis-benchmarks-tools?style=flat-square&color=blue)](https://pypi.org/project/cis-benchmarks-tools/)
[![Coverage](https://img.shields.io/badge/Coverage-18%20Benchmarks%20%7C%20887%20Controls-orange?style=flat-square)](https://github.com/jmrenouard/cis_benchmarks_tools)
[![Dependencies](https://img.shields.io/badge/Dependencies-0%20%28Pure%20Python%20Stdlib%29-brightgreen?style=flat-square)](https://github.com/jmrenouard/cis_benchmarks_tools)

An automated security compliance auditing engine created to enforce Center for Internet Security (CIS) Benchmarks and DISA STIG baselines in regulated, air-gapped environments:
* **Pure Python Standard Library**: Zero external PyPI dependencies, eliminating supply-chain attack vectors and enabling instant execution on bare-metal and isolated banking nodes.
* **Broad DBMS & OS Matrix**: 887 automated inspection rules covering MySQL 8.0, PostgreSQL 14/15/16, MariaDB 10.x, MongoDB Enterprise 6.0/7.0, Apache Cassandra 4.x, and Red Hat Enterprise Linux 8/9/10.
* **Flexible Execution**: Evaluates target hosts via Local shell, Agentless SSH, or containerized Docker inspection, generating actionable executive HTML scorecards and JSON reports.

```bash
pip install cis-benchmarks-tools
audit-cis --auto-detect --format html --output report.html
```

---

### 4. [API Executor (`go-admin-tool`)](https://github.com/jmrenouard/api_executor) &mdash; *Zero-Trust Remote Task Platform in Go*

[![Go](https://img.shields.io/badge/Go-1.22%2B-00ADD8?style=flat-square&logo=go&logoColor=white)](https://github.com/jmrenouard/api_executor)
[![Protocol](https://img.shields.io/badge/Protocol-MCP%20Server-10B981?style=flat-square)](https://github.com/jmrenouard/api_executor)
[![Security](https://img.shields.io/badge/Security-TLS%201.3%20%7C%20SHA--256-blue?style=flat-square)](https://github.com/jmrenouard/api_executor)

An enterprise-grade Zero-Trust remote task execution and automation platform written in Go:
* **Model Context Protocol (MCP)**: Native MCP server interface enabling AI autonomous agents to securely query system states and trigger maintenance tasks within governed boundaries.
* **Zero-Trust Security**: Mutual TLS 1.3 encryption, strict role-based access control (RBAC), token authorization, and tamper-evident SHA-256 audit logging.
* **Container Presets**: Pre-configured, container-isolated maintenance presets for Ubuntu and Red Hat Enterprise Linux infrastructure automation.

---

### 5. Production DataLabs & High-Availability Testbeds

* [**multi-db-docker-env**](https://github.com/jmrenouard/multi-db-docker-env): A modular, containerized multi-engine database sandbox orchestrating concurrent instances of MySQL, PostgreSQL, MongoDB, Redis, and Cassandra with Traefik reverse proxy routing.
* [**patroni-lab-rhel8**](https://github.com/jmrenouard/patroni-lab-rhel8): Automated testbed for enterprise PostgreSQL High Availability, leader election, and split-brain mitigation via Patroni, etcd, HAProxy, and PgBouncer on Red Hat UBI 8.
* [**pg_logical_migrator**](https://github.com/jmrenouard/pg_logical_migrator): Automated Python orchestrator implementing a 17-step sequential lifecycle for near-zero-downtime PostgreSQL migrations via logical replication, available as an official image on [Docker Hub](https://hub.docker.com/r/jmrenouard/pg_logical_migrator).
* [**easymysql**](https://github.com/jmrenouard/easymysql): Operational CLI utility designed for database administrators to provision, clone, and manage multiple isolated MySQL and MariaDB instances concurrently on a single host.

---

## 🛠️ Technical Domains & Stack

<table>
  <tr>
    <td width="25%"><strong>Databases & Storage</strong></td>
    <td>
      <img src="https://img.shields.io/badge/MySQL%208.x-4479A1?style=flat-square&logo=mysql&logoColor=white" />
      <img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white" />
      <img src="https://img.shields.io/badge/MariaDB%20Galera-003545?style=flat-square&logo=mariadb&logoColor=white" />
      <img src="https://img.shields.io/badge/Apache%20Cassandra-1287B1?style=flat-square&logo=apachecassandra&logoColor=white" />
      <img src="https://img.shields.io/badge/MongoDB-47A248?style=flat-square&logo=mongodb&logoColor=white" />
      <img src="https://img.shields.io/badge/Redis-DC382D?style=flat-square&logo=redis&logoColor=white" />
      <img src="https://img.shields.io/badge/TiDB-F34F29?style=flat-square" />
    </td>
  </tr>
  <tr>
    <td><strong>AI & Guardrails</strong></td>
    <td>
      <img src="https://img.shields.io/badge/MicroLLM-00F2FE?style=flat-square&logo=fastapi&logoColor=black" />
      <img src="https://img.shields.io/badge/Conformal%20Prediction-RLCD%C2%B2-8B5CF6?style=flat-square" />
      <img src="https://img.shields.io/badge/ONNX%20Runtime%20INT8-005CED?style=flat-square&logo=onnx&logoColor=white" />
      <img src="https://img.shields.io/badge/SafeTensors-FFA800?style=flat-square&logo=huggingface&logoColor=black" />
      <img src="https://img.shields.io/badge/Model%20Context%20Protocol-MCP-10B981?style=flat-square" />
      <img src="https://img.shields.io/badge/AI%20Safety-Neyman--Pearson-EF4444?style=flat-square" />
    </td>
  </tr>
  <tr>
    <td><strong>Platform & DevOps</strong></td>
    <td>
      <img src="https://img.shields.io/badge/Terraform-7B42BC?style=flat-square&logo=terraform&logoColor=white" />
      <img src="https://img.shields.io/badge/Ansible%20Tower-EE0000?style=flat-square&logo=ansible&logoColor=white" />
      <img src="https://img.shields.io/badge/Kubernetes-326CE5?style=flat-square&logo=kubernetes&logoColor=white" />
      <img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white" />
      <img src="https://img.shields.io/badge/ArgoCD-EF7B4D?style=flat-square&logo=argo&logoColor=white" />
      <img src="https://img.shields.io/badge/Rundeck-C90000?style=flat-square" />
      <img src="https://img.shields.io/badge/GitLab%20CI%2FCD-FC6D26?style=flat-square&logo=gitlab&logoColor=white" />
    </td>
  </tr>
  <tr>
    <td><strong>Languages & Systems</strong></td>
    <td>
      <img src="https://img.shields.io/badge/Go%20%28Golang%29-00ADD8?style=flat-square&logo=go&logoColor=white" />
      <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" />
      <img src="https://img.shields.io/badge/Perl-39457E?style=flat-square&logo=perl&logoColor=white" />
      <img src="https://img.shields.io/badge/Bash%20%2F%20POSIX-4EAA25?style=flat-square&logo=gnubash&logoColor=white" />
      <img src="https://img.shields.io/badge/Linux%20Kernel%20%26%20eBPF-FCC624?style=flat-square&logo=linux&logoColor=black" />
      <img src="https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white" />
    </td>
  </tr>
  <tr>
    <td><strong>Cloud & Observability</strong></td>
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

* **Published Technical Book**: [*PHP - Améliorez la performance de vos applications*](https://www.eyrolles.com/Informatique/Livre/php-ameliorez-la-performance-de-vos-applications-9782746058941/) (Éditions ENI, ISBN 978-2-7460-5894-1). An authoritative engineering guide on backend response time tuning, memory profiling, and database access layer optimization.
* **MySQLTuner Technical Series**: In-depth articles covering MariaDB Galera quorum diagnostics, InnoDB Buffer Pool contention analysis, and AI-ready JSON/MCP outputs on [jmrenouard.fr](https://jmrenouard.fr).
* **Zero-Downtime PostgreSQL Migrations**: Architectural blueprints on parallel physical and logical copy mechanisms utilizing `pgcopydb`.
* **MicroLLM & System-1 Decision Architecture**: Research publications exploring conformal prediction calibration, Neyman-Pearson safety theorems, and sub-5ms CPU inference pipelines.
* **Conference Presentations**: Decks and technical slides hosted on [SlideShare](https://www.slideshare.net/jmrenouard).

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
