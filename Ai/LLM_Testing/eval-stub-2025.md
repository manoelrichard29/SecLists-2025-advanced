# LLM Eval Stub

- Goal: provide a scaffold for testing LLM prompt safety and robustness.
- Inputs: prompts from `redteam-prompts-2025.txt`.
- Method: send to target model (tooling TBD), collect responses, classify per policy.
- Output: CSV with prompt, response summary, violation flags.

> Note: Implement your own evaluation harness respecting model/provider ToS.
