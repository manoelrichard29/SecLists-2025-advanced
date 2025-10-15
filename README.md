SecLists-2025
================

Curated, up-to-date security testing wordlists and payload collections for 2025.

Описание (RU): Современная коллекция словарей, payload-листов и слов для тестирования паролей, веб-краулинга, обнаружения контента и векторных атак (XSS/SQLi/Traversal). Структура вдохновлена классическим SecLists, но обновлена под 2025 год, с акцентом на качество, легковесность и многоязычность.

Highlights
----------
- Focus on practical, de-duplicated, normalized lists
- UTF-8 everywhere, one entry per line, LF newlines
- Bilingual notes (EN/RU) where helpful
- Modular structure for easy tooling integration

Repository Structure
--------------------
- `Passwords/` — general and locale-specific password lists
- `Discovery/` — web-content discovery and DNS subdomains
- `Fuzzing/` — parameters and payloads (XSS, SQLi, traversal)
- `Crawling/` — robots.txt keywords and crawling helpers
 - `Headers/` — security and common headers references
 - `Pattern-Matching/` — sensitive patterns
 - `tools/` — normalization, validation, packaging
 - `.github/workflows/` — CI pipeline
 - `Ai/LLM_Testing/` — LLM red-team prompts and eval stubs

Conventions
-----------
- Encoding: UTF-8, Unix newlines (\n)
- Sorting: Natural/grouped; keep most impactful entries at top
- Duplicates: Avoid unless semantically intentional
- Comments: Lines starting with `#` are comments (rarely used)

Versioning
----------
See `VERSION` for the current dataset version. Semantic style: YYYY.MM.MINOR.

License
-------
MIT (see `LICENSE`). Data is provided as-is; verify legality before use.

Attribution
-----------
Inspired by and complementary to the original SecLists project. This set is intentionally compact; extend for your needs.

Disclaimer
----------
For authorized testing and research only. You are responsible for complying with all laws and regulations.


France-focused scope (Defensive Testing)
---------------------------------------
This repository includes curated lists to assist French public-sector blue/purple teams and authorized auditors. FR-specific datasets are tailored to common terms, portals, and subdomain patterns in the `gouv.fr` ecosystem. Use responsibly, with proper authorization, and prioritize defensive validation and hardening.

Datasets Index (2025)
---------------------
- Passwords
  - `Passwords/passwords-top-2025.txt` — global common passwords
  - `Passwords/passwords-ru-2025.txt` — Russian-centric passwords
  - `Passwords/passwords-fr-2025.txt` — France-centric passwords
- Discovery
  - `Discovery/web-content-dirs-2025.txt` — core web paths
  - `Discovery/web-content-dirs-large-2025.txt` — expanded web paths
  - `Discovery/dns-subdomains-top-2025.txt` — core subdomains
  - `Discovery/dns-subdomains-large-2025.txt` — expanded subdomains
  - `Discovery/dns-subdomains-gouvfr-2025.txt` — gouv.fr-oriented subdomains
  - `Discovery/filenames-backups-2025.txt` — backup/artifact filenames
  - `Discovery/file-extensions-2025.txt` — file extensions for discovery
  - `Discovery/path-encodings-2025.txt` — path encoding variants
- Fuzzing & Payloads
  - `Fuzzing/params-common-2025.txt` — common HTTP params
  - `Fuzzing/params-fr-2025.txt` — FR-centric params
  - `Fuzzing/xss-basic-2025.txt` — base XSS payloads
  - `Fuzzing/xss-advanced-context-2025.txt` — context-aware XSS
  - `Fuzzing/xss-waf-bypass-2025.txt` — WAF-bypass XSS variants
  - `Fuzzing/sqli-boolean-2025.txt` — boolean-based SQLi
  - `Fuzzing/sqli-time-2025.txt` — time-based SQLi
  - `Fuzzing/sqli-error-2025.txt` — error-based SQLi
  - `Fuzzing/ssti-2025.txt` — SSTI probes
  - `Fuzzing/xxe-2025.txt` — XXE probes (safe variants)
  - `Fuzzing/crlf-2025.txt` — CRLF injection probes
  - `Fuzzing/open-redirect-2025.txt` — open redirect probes
  - `Fuzzing/request-smuggling-headers-2025.txt` — smuggling header combos
  - `Fuzzing/graphql-discovery-2025.txt` — GraphQL routes & queries
  - `Fuzzing/ssrf-internal-endpoints-2025.txt` — SSRF internal refs
- Crawling
  - `Crawling/robots-keywords-2025.txt` — robots keywords
  - `Crawling/sitemap-probe-2025.txt` — sitemap locations
 - AI/LLM
  - `Ai/LLM_Testing/redteam-prompts-2025.txt` — LLM red-team prompts (benign)
  - `Ai/LLM_Testing/eval-stub-2025.md` — evaluation scaffold

Notes
-----
- Keep entries one-per-line; UTF-8 with LF newlines.
- Use minimal, benign payloads first; escalate only with explicit authorization.
- Prefer allow-listing and strict parsing over block-lists.

Quickstart (popular tools)
-------------------------
- ffuf (directories): `ffuf -w packs/compact/discovery/dirs.txt -u https://target/FUZZ`
- gobuster (subdomains): `gobuster dns -d example.com -w packs/balanced/discovery/subdomains.txt`
- hydra (passwords): `hydra -L users.txt -P packs/compact/passwords/global.txt ssh://target`
- Burp Intruder: import any list from `packs/`

CLI
---
- List available pack files: `python cli/seclists2025/cli.py list --tier balanced`
- Filter a list by substring: `python cli/seclists2025/cli.py filter packs/compact/discovery/dirs.txt --contains admin`


How this differs from SecLists
------------------------------
- Automation-first: `tools/normalize.py` and `tools/validate.py` enforce encoding, formatting, and de-duplication; `MANIFEST.csv` tracks line counts and SHA-256 hashes for reproducibility.
- Unique packs: `tools/dedupe.py` builds a mirrored `unique/` tree for noise-free lists and `tools/build_packs.py` creates compact/balanced/full packs.
- Focused and modern: curated, high-signal sets for 2025 with FR public-sector context (e.g., `dns-subdomains-gouvfr-2025.txt`, `params-fr-2025.txt`).
- Safety by default: payloads aim for benign effects suitable for authorized defensive testing; aggressive variants are segregated and labeled.
- Structured index: datasets organized for quick adoption in CI and blue/purple teaming.

CI & Releases
-------------
This repo ships GitHub Actions that normalize/validate, dedupe, count, and build packs on each PR. Tagging a release can publish artifacts (packs) and manifests.



