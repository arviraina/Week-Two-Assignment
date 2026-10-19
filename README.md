# Week 2 — Newsroom Triage, Option A

Course starter app adapted for local VS Code use. It classifies news into World, Sports, Business and Sci/Tech and shows routing, retrieved notes and guard checks.

## Run

Install requirements.txt in a project Python environment and run `python run.py`. Without a GROQ_API_KEY environment variable it uses a rule-based demonstration. The notebook is an alternative: open it from this project folder, run cells in order, and enter any API key only in its hidden prompt. Never commit keys or saved notebook outputs. The app sends entered news text to the model provider when a key is present.

## Experiments

The answer sheet contains 30 news items and the learner's category judgments. Versions.csv records the experiments. Best measured prompt: 23/30 (76.7%), kappa 0.6912. Final experimental configuration: 22/30 (73.3%), kappa 0.6418. The final settings retain the uncertainty wording, 0.4 confidence floor, weather refusal rule and escalation notes. No successful saved live-model answer was below 0.4; the cutoff therefore did not demonstrate a protective effect on these examples.

Changes include clearer category instructions, prompt trials, a confidence cutoff, weather routing, escalation retrieval, response allowance and rate-limit handling, and a kappa calculation that includes blocked answers. Both notebook and app scoring use the learner's labels.

## Sharing scope

This copy excludes API secrets, private settings, local computer paths, saved notebook outputs, conversation databases, screenshots, personal report documents, course PDFs, the instructor answer key, environments and caches. The working originals are untouched. Only the 30-item answer sheet is included; the larger course dataset is omitted. Course starter code and supplied news text retain their original ownership; no new license is asserted here.

Screenshots, the two-page report and the current temporary public app link remain separate submission materials. This repository alone does not replace the assignment submission.
