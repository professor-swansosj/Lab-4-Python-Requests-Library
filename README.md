# Lab 4 — Python Requests Library

**Course:** Software Defined Networking  
**Module:** Network Automation Fundamentals • **Lab #:** 4  
**Estimated Time:** 90–120 minutes

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


## Resources
- [Requests (Python)](https://requests.readthedocs.io/en/latest/)- [Dad Jokes API](https://icanhazdadjoke.com/api) — Use Accept: application/json to get JSON.- [Deck of Cards API](https://deckofcardsapi.com/) — Create deck → store deck_id → draw.- [pprint (Python)](https://docs.python.org/3/library/pprint.html)

## FAQ
**Q:** I got HTML back instead of JSON—why?  
**A:** Add a header like `Accept: application/json` for APIs (e.g., Dad Jokes).

**Q:** My draw fails on the Deck API.  
**A:** You must pass the exact `deck_id` returned from the create call into the draw call.

**Q:** Face cards compare weirdly.  
**A:** Map values once: {2..10, JACK:11, QUEEN:12, KING:13, ACE:14} and compare integers.



## Deliverables
- Standard README with objectives, resources, grading, and tips.
- Stepwise INSTRUCTIONS for four scripts, artifacts under data/, and logs under logs/.
- Grading: **75 points**

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



## Autograder Notes
- Log file: `logs/*.log`
- Required markers: `LAB4_START`, `[STEP 2] Dev Container Started`, `LAB4_POSTMAN_EXPORT_RUN`, `LAB4_HTTP_OK`, `LAB4_RAW_PRINTED`, `LAB4_ACCEPT_JSON_HEADER_SET`, `LAB4_JSON_LOADED`, `LAB4_PPRINT_OK`, `LAB4_JOKE_FIELD_OK`, `LAB4_JOKE_PRINTED`, `LAB4_LOOP_BEGIN`, `LAB4_LOOP_CONTINUE`, `LAB4_LOOP_STOP`, `LAB4_DECK_CREATE_OK`, `LAB4_DRAW`, `LAB4_COMPARE`, `LAB4_ROUND_WINNER`, `LAB4_ROUND_TIE`, `LAB4_GAME_END`, `LAB4_ERR`, `LAB4_END`

## License
© 2025 Your Name — Classroom use.

# HAPPY CODING!