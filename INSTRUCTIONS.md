# Instructions — Lab 4 — Python Requests Library

## Objectives
- Use the Python `requests` library to send HTTP requests and receive responses.
- Export a request from Postman into Python and run it as a script.
- Parse JSON into Python dicts/lists and extract specific fields.
- Pretty-print JSON and compose f-strings for clear output.
- Implement loops and conditionals for user interaction.
- Work with a multi-step API flow (Deck of Cards: create deck → draw cards).
- Build a mini game using API data and comparison logic.

## Prerequisites
- Python 3.11 (via the provided dev container)
- Accounts: GitHub
- Devices/Sandboxes: Public APIs (Dad Jokes, Deck of Cards)

## Overview
Move from cURL/Postman into actual Python automation with `requests`. You’ll fetch JSON, pretty-print and extract fields, add a small user-driven loop, then chain API calls with Deck of Cards to build a tiny “highest card wins” game.


> **Before you begin:** Open the dev container and verify outbound HTTPS works. Confirm `python --version` and that `requests` is importable. Create the folders `logs/`, `data/raw/`, and `data/reports/` if needed.


## Resources
- [Requests (Python)](https://requests.readthedocs.io/en/latest/)- [Dad Jokes API](https://icanhazdadjoke.com/api) — Use Accept: application/json to get JSON.- [Deck of Cards API](https://deckofcardsapi.com/) — Create deck → store deck_id → draw.- [pprint (Python)](https://docs.python.org/3/library/pprint.html)
## Deliverables
- Standard README with objectives, resources, grading, and tips.
- Stepwise INSTRUCTIONS for four scripts, artifacts under data/, and logs under logs/.
- Grading: **75 points**

Follow these steps in order.

> **Logging Requirement:** Write progress to `logs/*.log` as you complete each step.

## Step 1 — Clone the Repository
**Goal:** Get your Classroom repo locally.

**What to do:**  
Clone, `cd` into it, and ensure `logs/`, `data/raw/`, and `data/reports/` exist.

**You’re done when:**  
You see the folders above; Git is tracking changes.

**Log marker to add:**  
`[LAB4_START]`

## Step 2 — Open a Dev Container
**Goal:** Use the standardized environment.

**What to do:**  
Open in VS Code and reopen in container. Wait for READY, confirm Python.

**You’re done when:**  
`[STEP 2] Dev Container Started` is written to `logs/lab4_devcontainer.log`.

**Log marker to add:**  
`[[STEP 2] Dev Container Started]`

## Step 3 — Export from Postman → Python
**Goal:** Move a Dad Jokes request from Postman into code.

**What to do:**  
Export as Python; save to `src/jokes_postman_export.py`; run and print response.

**You’re done when:**  
Raw response prints and required log markers exist.

**Log marker to add:**  
`[LAB4_POSTMAN_EXPORT_RUN, LAB4_HTTP_OK, LAB4_RAW_PRINTED]`

## Step 4 — Request JSON + pretty-print
**Goal:** Parse and inspect JSON cleanly.

**What to do:**  
Add `Accept: application/json`; save last JSON to `data/raw/jokes_last.json`; pretty-print with `pprint` and write a one-line report to `data/reports/joke_of_the_day.txt`.

**You’re done when:**  
`LAB4_JSON_LOADED` and `LAB4_PPRINT_OK` appear; report file exists.

**Log marker to add:**  
`[LAB4_ACCEPT_JSON_HEADER_SET, LAB4_HTTP_OK, LAB4_JSON_LOADED, LAB4_PPRINT_OK, LAB4_JOKE_FIELD_OK, LAB4_JOKE_PRINTED]`

## Step 5 — Add a simple loop
**Goal:** Fetch jokes until user stops.

**What to do:**  
Normalize input (`.strip().lower()`); loop with `y/n`; handle invalid input; log each round.

**You’re done when:**  
Loop runs at least twice; proper LOOP_* markers present.

**Log marker to add:**  
`[LAB4_LOOP_BEGIN, LAB4_LOOP_CONTINUE, LAB4_LOOP_STOP]`

## Step 6 — Create a deck (Deck of Cards)
**Goal:** Chain calls with saved state.

**What to do:**  
Create a shuffled deck; store `deck_id`; log success or failure.

**You’re done when:**  
`LAB4_DECK_CREATE_OK deck_id=...` exists in `logs/high_card.log`.

**Log marker to add:**  
`[LAB4_DECK_CREATE_OK]`

## Step 7 — Highest card wins
**Goal:** Use API data to power a tiny game.

**What to do:**  
From same deck, draw one card for player and CPU; map face values; compare; handle ties; append round summaries to `data/reports/high_card_results.txt`.

**You’re done when:**  
At least one round logged with DRAW/COMPARE/WINNER (or TIE); `GAME_END` when exiting.

**Log marker to add:**  
`[LAB4_DRAW, LAB4_COMPARE, LAB4_ROUND_WINNER, LAB4_ROUND_TIE, LAB4_GAME_END]`

## Step 8 — Error handling & polish
**Goal:** Fail predictably.

**What to do:**  
Wrap requests in `try/except` with `timeout=`; on handled error, write `LAB4_ERR type=<ExceptionName> msg="..."` to the relevant log.

**You’re done when:**  
One controlled `LAB4_ERR` appears in any script log.

**Log marker to add:**  
`[LAB4_ERR]`

## Step 9 — Commit, push, open PR
**Goal:** Submit work for grading.

**What to do:**  
Commit source + artifacts + logs; push; open a PR to `main`.

**You’re done when:**  
PR is open and green.

**Log marker to add:**  
`[LAB4_END]`


## FAQ
**Q:** I got HTML back instead of JSON—why?  
**A:** Add a header like `Accept: application/json` for APIs (e.g., Dad Jokes).

**Q:** My draw fails on the Deck API.  
**A:** You must pass the exact `deck_id` returned from the create call into the draw call.

**Q:** Face cards compare weirdly.  
**A:** Map values once: {2..10, JACK:11, QUEEN:12, KING:13, ACE:14} and compare integers.


## 🔧 Troubleshooting & Pro Tips
**Got HTML instead of JSON**  
*Symptom:* Output looks like an HTML page  
*Fix:* Set `headers={'Accept': 'application/json'}`.

**Requests hangs**  
*Symptom:* Script stuck on network call  
*Fix:* Pass `timeout=10` and handle `requests.Timeout`.

**KeyError on JSON**  
*Symptom:* `data['joke']` explodes  
*Fix:* Inspect full JSON once; use `.get('joke')` and validate.

**Deck exhausted**  
*Symptom:* Draw returns too few cards  
*Fix:* Recreate or reshuffle when `remaining` is 0.

**Logs missing**  
*Symptom:* Autograder finds no markers  
*Fix:* Use the provided `log(...)` helper and write to the correct file per script.


## Grading Breakdown
| Step | Requirement | Points |
|---|---|---|
| 2 | `[STEP 2] Dev Container Started` appears in `logs/lab4_devcontainer.log` | 5 |
| 3 | `logs/jokes_postman_export.log` has START, POSTMAN_EXPORT_RUN, HTTP_OK, RAW_PRINTED, END | 10 |
| 4 | `logs/jokes_json.log` shows JSON header set, HTTP_OK, JSON_LOADED, PPRINT_OK | 10 |
| 5 | `logs/jokes_json.log` includes JOKE_FIELD_OK and JOKE_PRINTED | 5 |
| 6 | `logs/jokes_loop.log` shows LOOP_BEGIN, JOKE_FIELD_OK, and LOOP_CONTINUE/LOOP_STOP | 10 |
| 7 | `logs/high_card.log` shows DECK_CREATE_OK with valid deck_id | 5 |
| 8 | `logs/high_card.log` shows card draws, comparison, and winner/tie for ≥1 round | 15 |
| 9 | Any script log includes an `LAB4_ERR ...` marker for a handled error | 5 |
| 10 | All artifacts committed/pushed and PR opened | 10 |
| **Total** |  | **75** |

## Autograder Notes
- Log file: `logs/*.log`
- Required markers: `LAB4_START`, `[STEP 2] Dev Container Started`, `LAB4_POSTMAN_EXPORT_RUN`, `LAB4_HTTP_OK`, `LAB4_RAW_PRINTED`, `LAB4_ACCEPT_JSON_HEADER_SET`, `LAB4_JSON_LOADED`, `LAB4_PPRINT_OK`, `LAB4_JOKE_FIELD_OK`, `LAB4_JOKE_PRINTED`, `LAB4_LOOP_BEGIN`, `LAB4_LOOP_CONTINUE`, `LAB4_LOOP_STOP`, `LAB4_DECK_CREATE_OK`, `LAB4_DRAW`, `LAB4_COMPARE`, `LAB4_ROUND_WINNER`, `LAB4_ROUND_TIE`, `LAB4_GAME_END`, `LAB4_ERR`, `LAB4_END`

## Submission Checklist
- [ ] logs/jokes_postman_export.log includes START/END and required markers.
- [ ] logs/jokes_json.log includes JSON header, HTTP_OK, JSON_LOADED, PPRINT_OK, JOKE_FIELD_OK, JOKE_PRINTED.
- [ ] logs/jokes_loop.log shows multiple rounds with LOOP markers.
- [ ] logs/high_card.log shows DECK_CREATE_OK, per-round DRAW/COMPARE/WINNER (or TIE), and GAME_END.
- [ ] data/raw/jokes_last.json present.
- [ ] data/raw/deck_draw_last.json present.
- [ ] data/reports/joke_of_the_day.txt present.
- [ ] data/reports/high_card_results.txt present.
