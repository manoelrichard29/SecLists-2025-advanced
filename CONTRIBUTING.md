# Contributing

Thank you for helping improve SecLists-2025. Quality and safety are the priorities.

Guidelines:
- One entry per line, UTF-8 with LF newlines.
- Prefer minimal, high-signal entries over exhaustive noise.
- Include locale/source context if relevant (e.g., FR-specific).
- Avoid harmful payloads; keep demonstrations benign.
- Run the tooling before submitting:
  - `python tools/normalize.py`
  - `python tools/validate.py`
- Update `MANIFEST.csv` via the normalize script.
- For large lists, provide a short README section explaining curation criteria.

By contributing, you agree to the MIT license.
