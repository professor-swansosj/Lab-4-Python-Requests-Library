# Lab Instructions

## Lab Title
`The Python Request Library`

## Version
`v1.0 / 9/25`

## Estimated Time
- `90–120 minutes`
    - `30-40 minutes Dad Jokes API`
    - `45-60 minutes Deck of Cards API`

---

## Learning Objectives
By the end of this lab, you will be able to:
- Objective 1 – Use the Python requests library to send HTTP requests and receive responses.
- Objective 2 – Export a request from Postman into Python code and successfully run it as a script.
- Objective 3 – Parse JSON responses into Python dictionaries and extract specific values.
- Objective 4 – Apply pretty print (`pprint`) to make JSON output readable in the terminal.
- Objective 5 – Combine f-strings with dictionary data to produce user-friendly output.
- Objective 6 – Implement loops and conditionals for repeated API calls and user interaction.
- Objective 7 – Work with a multi-step API flow (Deck of Cards: create deck → draw cards).
- Objective 8 – Build a small Python game that uses an API, compares values, and prints results.
- Objective 9 – Strengthen your confidence moving from GUI tools (Postman) into real Python automation.

These objectives build foundational skills for aspiring **network engineers** and **infrastructure specialists**.

---

## Tools & Technologies
You will use:
- Editor/Runtime
    - Visual Studio Code + Dev Containers extension
    - Docker Desktop (Windows/macOS; WSL2 enabled on Windows)
    - Git & GitHub Classroom repository
- Language & Libraries (preinstalled in container)
    - Python 3.x
    - `requests` (Python library for HTTP requests)
    - `json` (built-in Python library for working with JSON data)
    - `pprint` (built-in Python library for pretty-printing dictionaries)
- API Tools
    - Postman (graphical API client; desktop or web app, used for exporting to Python code)
    - cURL (command-line API client, reference from previous lab)
- APIs (targets for requests)
    - [Dad Jokes API](https://icanhazdadjoke.com/)
    - [Deck of Cards API](https://deckofcardsapi.com/)
- Command Line
    - Bash (WSL, macOS, or inside the devcontainer)

---

## Prerequisites
Before starting, make sure you:
- Completed Lab 3: Introduction to APIs (you should already know what an API is, how to identify URL, method, headers, body, and status code).
- Installed and used Postman to make basic API requests and learned how to export a request.
- Run basic cURL commands to test an API from the terminal.
- Worked with GitHub Classroom repositories and Dev Containers (cloning a repo, opening in VS Code, and confirming the environment).
- Comfort with writing and running a Python script from a `.py` file.
- Basic understanding of variables, strings, loops, and conditionals.
- Awareness of Python functions (we’ll practice structuring code into functions in this lab).

**:brain: Mindset**
- Curiosity and patience: APIs sometimes return unexpected results, and your job is to explore, debug, and adapt.

---

## Deliverables
Commit and push the following to your Classroom repo (do not rename paths/files):

### Source Code (in `src/`)
1. `src/jokes_postman_export.py`
    - Direct Postman → Python export of the Dad Jokes request from Lab 3.
    - Prints the raw/plain-text response (no JSON parsing yet).
    - Required log lines (to `logs/jokes_postman_export.log`):
        - `LAB4_START`
        - `LAB4_POSTMAN_EXPORT_RUN`
        - `LAB4_HTTP_OK status=200` (or `LAB4_HTTP_FAIL` ... if not)
        - `LAB4_RAW_PRINTED`
        - `LAB4_END`

2. `src/jokes_json.py`
    - Requests JSON from the Dad Jokes API, converts to a Python dict, pretty-prints, and extracts "joke" into an f-string.
    - Required log lines (to `logs/jokes_json.log`):
        - `LAB4_START`
        - `LAB4_ACCEPT_JSON_HEADER_SET`
        - `LAB4_HTTP_OK status=200` (or fail marker)
        - `LAB4_JSON_LOADED keys=...`
        - `LAB4_PPRINT_OK`
        - `LAB4_JOKE_FIELD_OK`
        - `LAB4_JOKE_PRINTED`
        - `LAB4_END`

3. `src/jokes_loop.py`
    - Simple loop: fetch a new joke until the user chooses to stop. Normalize input and handle empty/invalid input.
    - Required log lines (to `logs/jokes_loop.log`):
        - `LAB4_START`
        - For each iteration:
            - `LAB4_LOOP_BEGIN n=<round>`
            - `LAB4_HTTP_OK status=200` (or fail marker)
            - `LAB4_JOKE_FIELD_OK`
            - `LAB4_LOOP_CONTINUE` or `LAB4_LOOP_STOP`
            - `LAB4_END`

4. `src/high_card.py`
    - Uses Deck of Cards API to create a shuffled deck, draw one card for player and one for computer, map ranks, compare, announce winner, offer replay; handles tie and reshuffle/exhaustion.
    - Required log lines (to `logs/high_card.log`):
        - `LAB4_START`
        - `LAB4_DECK_CREATE_OK deck_id=<id>` (or `LAB4_DECK_CREATE_FAIL ...`)
        - For each round:
            - `LAB4_DRAW player=value=<face> suit=<suit>`
            - `LAB4_DRAW cpu=value=<face> suit=<suit>`
            - `LAB4_COMPARE p=<int> c=<int>`
            - `LAB4_ROUND_WINNER=player|cpu or LAB4_ROUND_TIE`
            - `LAB4_PLAY_AGAIN=yes|no`
            - `LAB4_GAME_END`
            - `LAB4_END`

✅ Error handling: If you catch an error (timeout, non-200, JSON decode), log a clear marker like `LAB4_ERR type=<ExceptionName> msg="..."` to the relevant script log. Handling at least one controlled error path is part of grading.

### Data Artifacts (in `data/`)
- `data/raw/jokes_last.json`
    - The last full JSON object received from the Dad Jokes API (overwrite each run).
- `data/raw/deck_draw_last.json`
    - The last full JSON object from a Deck of Cards draw (overwrite each run).
- `data/reports/joke_of_the_day.txt`
    - A single line like: `Your daily joke is: <joke>` (written by `jokes_json.py`).
- `data/reports/high_card_results.txt`
    - Append one line per round with a compact summary, e.g.:
        - `round=1 player=ACE♠ cpu=9♥ winner=player`
        - `round=2 player=7♦ cpu=7♣ result=tie`

### Logs (in `logs/`)
- `logs/jokes_postman_export.log`
    - Contains: `LAB4_START`, `LAB4_POSTMAN_EXPORT_RUN`, `LAB4_HTTP_OK`, `LAB4_RAW_PRINTED`, `LAB4_END`.
- `logs/jokes_json.log`
    - Contains: `LAB4_START`, `LAB4_ACCEPT_JSON_HEADER_SET`, `LAB4_HTTP_OK`, `LAB4_JSON_LOADED`, `LAB4_PPRINT_OK`, `LAB4_JOKE_FIELD_OK`, `LAB4_JOKE_PRINTED`, `LAB4_END`.
- `logs/jokes_loop.log`
    - Contains: multiple `LAB4_LOOP_BEGIN n=...`, `LAB4_JOKE_FIELD_OK`, and either `LAB4_LOOP_CONTINUE` or `LAB4_LOOP_STOP`, plus `LAB4_START/END`.
- `logs/high_card.log`
    - Contains: `LAB4_DECK_CREATE_OK deck_id=...`, per-round `LAB4_DRAW ...`, `LAB4_COMPARE ...`, `LAB4_ROUND_WINNER=...` or `LAB4_ROUND_TIE`, `LAB4_PLAY_AGAIN=...`, `LAB4_GAME_END`, plus `LAB4_START/END`.
- `logs/devcontainer_health.log` (auto-generated)
    - Contains: `LAB4_HEALTH_START/END`, at least one `LAB4_DNS_OK`, `LAB4_NET_OK`, `LAB4_PKG_OK name=requests`, and `LAB4_HEALTH_SUMMARY ... overall=True`.
- `logs/DEVCONTAINER_STATUS.txt` (auto-generated)
    - Shows banner with `Overall status: READY`.

⚠️ Important: Autograding will validate file presence and grep for the markers above. Do not rename deliverables or markers.

---

## Logging Snippet to Include
**INSERT THIS CODE SNIPPET AT THE VERY TOP OF YOUR CODE RIGHT AFTER YOUR IMPORT STATEMENTS. IF A LOG MESSAGE IS REQUIRED AT ANY TIME IT WILL BE ANNOTAED IN THE INSTRUCTIONS.**
```python
from datetime import datetime, timezone
from pathlib import Path

def now_iso():
    return datetime.now(timezone.utc).isoformat().replace("+00:00","Z")

def log(line, path):
    # Ensure logs directory exists even if student runs from repo root
    Path("logs").mkdir(parents=True, exist_ok=True)
    with open(path, "a", encoding="utf-8") as f:
        f.write(f"{line} ts={now_iso()}\n")

# usage examples:
# log("LAB4_START", "logs/jokes_json.log")
# log("LAB4_HTTP_OK status=200", "logs/high_card.log")
# log('LAB4_ERR type=Timeout msg="request timed out"', "logs/jokes_loop.log")
```

**Where to put it (student message)**
- Open each file in `src/` (`jokes_postman_export.py`, `jokes_json.py`, `jokes_loop.py`, `high_card.py`).
- Place the snippet immediately after your `import` statements.
- Use `log("...","logs/<matching-log>.log")` at each required milestone listed above.
- Commit and push when done. The autograder reads the `logs/*.log` files to award points.

## Overview
In this lab you’ll move from testing APIs in Postman (Lab 3) into actually writing Python code that calls APIs, handles responses, and turns them into usable programs. The focus is the requests library, one of the most common tools developers use when working with APIs in Python.

You’ll begin by exporting a Dad Jokes API call from Postman, running it in Python, and printing the raw text response. From there, you’ll request JSON instead of plain text, parse it into a Python dictionary, and use pretty print to display the results cleanly. Once you can extract the "joke" field, you’ll practice output formatting with a fun f-string like:
Your daily joke is: <the joke>

The second half of the lab introduces the Deck of Cards API. You’ll make multiple requests to shuffle and draw cards, then use that data to power a simple “highest card wins” game where you play against the computer. Each round, the script compares card values and announces the winner, looping until you decide to stop.

By the end of the lab, you’ll have written two small but functional programs that combine Python fundamentals—requests, JSON parsing, loops, conditionals, and user input—with real APIs. This sets the stage for more advanced automation projects later in the course.

💡 **Why this matters:** Modern networks cannot be managed manually at scale. Automation skills give you an edge as a job candidate and make you more effective in real-world environments.  

---

## Instructions

Follow these steps in order:

### Step 1 – Clone the Repository
Open your GitHub Classroom repository for Lab 4 on your local machine. Make sure you are inside the repository folder before you continue.

Why this matters: This ensures all your work is tracked in Git, organized in the right folder structure, and ready to push back for grading.

### Step 2 – Open a Dev Container
Open the repository in VS Code. Reopen the project in a Dev Container when prompted. The container will automatically install Python, required libraries, and set up your environment.

This may take a few minutes the first time you start it. Wait until the container is fully ready.

Log Requirement:
Your logs/lab4_devcontainer.log file should include the line:
[STEP 2] Dev Container Started


### Step 3 – Export a Postman request into Python
Using the Dad Jokes API request you built in Lab 3, export that request as Python code from Postman. Save it as your first script inside src/. Run the script and confirm that the response from the API prints to your terminal.

Goal: Move from testing in Postman into running the same request directly from Python.

Log Requirement:
Your log for this script (`logs/jokes_postman_export.log`) should show that you started the script, ran the exported request, received a response, and printed it.


### Step 4 – Work with JSON responses
Update your Dad Jokes request so that it asks for JSON instead of plain text. Convert the response into a Python dictionary and pretty-print the output so it’s easier to read.

Goal: Understand that APIs often return JSON and that Python can easily convert and display that data.

Log Requirement:
Your log for this script (`logs/jokes_json.log`) should show that you requested JSON, successfully loaded it, and pretty-printed the result.


### Step 5 – Extract a single field
From the JSON response, find the `"joke"` field and print it in a friendly message using a formatted string.

Goal: Practice pulling out a specific piece of data from a JSON response and displaying it in a user-friendly way.

Log Requirement:
Your log (`logs/jokes_json.log`) should confirm that the "joke" field was found and printed.

### Step 6 – Add a simple loop
Make your joke script interactive. After printing a joke, ask the user if they want another one. Continue looping until the user decides to stop.

Goal: Combine API requests with loops and user input to make your script interactive.

Log Requirement:
Your log (`logs/jokes_loop.log`) should show each loop round beginning, the joke being fetched, and whether the user continued or stopped.

### Step 7 – Use the Deck of Cards API
Connect to the Deck of Cards API. Create a new shuffled deck and save its unique identifier. Then draw cards from it.

Goal: Learn how some APIs require multiple requests that build on each other. The `deck_id` you receive from the first request will be used in later requests.

Log Requirement:
Your log (`logs/high_card.log`) should show that the deck was created successfully and include the deck ID.

### Step 8 – Build a “highest card wins” game
Draw one card for yourself and one for the computer from the same deck. Compare the two card values and announce who wins. Handle ties appropriately. Let the user play multiple rounds until they quit.

Goal: Apply program logic and API data together to create a functional game loop.

Log Requirement:
Your log (`logs/high_card.log`) should show the card drawn for each player, the comparison made, the winner of each round, and whether the game continued or ended.

### Step 9 – Wrap up with error handling and polish
Add basic error handling to your scripts. For example, log a clear error message if an API request fails or the JSON response is missing expected fields. Make sure your scripts end gracefully.

Goal: Build resilience into your programs and practice writing logs for both success and failure cases.

Log Requirement:
Any controlled error you catch should be logged in the proper log file with an `ERR` marker.

### Step 10 – Open a Pull Request
When you have finished and tested your scripts, push your changes to GitHub. Open a Pull Request (PR) in your Classroom repository. Your instructor and the autograder will use the PR to review your logs and code.

Goal: Submit your work in a professional workflow used by real developers.

## Troubleshooting
1. Dev Container Didn’t Install Dependencies
    - Symptom: ModuleNotFoundError: No module named 'requests' when running scripts.
    - Fix: Make sure you’re running code inside the Dev Container. Confirm requests is installed by listing installed packages. If missing, reinstall with the requirements file.

2. No Internet Access from Container
    - Symptom: API calls fail with timeouts or DNS errors.
    - Fix: Rerun the health check script (.devcontainer/health_check.py) to confirm connectivity. If DNS resolution fails, stop and rebuild your container.

3. Got HTML Instead of JSON
    - Symptom: Response prints a long HTML page instead of JSON or text.
    - Fix: APIs often require headers to specify the format. For the Dad Jokes API, include a header that asks for JSON if you need structured data.

4. KeyError on JSON Fields
    - Symptom: Script crashes when trying to access data["joke"].
    - Fix: Check the raw JSON response first. If the key name doesn’t exist (or is spelled wrong), Python will throw a KeyError. Always inspect what fields are actually returned.

5. Infinite Joke Loop
    - Symptom: Script never stops fetching jokes even after typing “no”.
    - Fix: Normalize your input (yes/no) by trimming spaces and making it lowercase before checking it. Handle unexpected input by reprompting the user.

6. Deck of Cards Draw Doesn’t Work
    - Symptom: You get an error or empty result when drawing cards.
    - Fix: Make sure you’re passing the deck_id from the first API call into the second. Without it, the API doesn’t know which deck you’re using.

7. Card Comparison Always Wrong
    - Symptom: The wrong winner is declared, or face cards don’t compare correctly.
    - Fix: Remember that "ACE", "KING", "QUEEN", and "JACK" are strings. You need to map them to numeric values before comparing.

8. Logs Not Created or Empty
    - Symptom: Autograder shows missing points even though your script worked.
    - Fix: Double-check that you added the logging snippet to the top of your scripts and that you’re writing to the correct logs/*.log file. Each required marker must be written as specified.

9. GitHub Autograder Fails
    - Symptom: Points deducted even though everything seems correct locally.
    - Fix: Verify that file names and paths match instructions exactly. Confirm that all log markers are present. Push your code and logs before opening your Pull Request.

## :light_bulb: Pro Tips
- Always Inspect Raw JSON First

Before pulling fields, print the full JSON response once. This helps you confirm key names and structure.

- Pretty Print Early, Debug Easier

Use pprint when looking at nested JSON objects. It makes errors much easier to spot.

- Use Functions for Clarity

Even small scripts benefit from breaking into functions like get_joke() or draw_card(). It keeps your code organized and easier to test.

- Handle Errors Gracefully

Wrap API requests in try/except and log a clear error marker (LAB4_ERR ...). Professional scripts always fail predictably.

- Think in Loops and Conditions

Most real automation isn’t “one-and-done.” Practice using loops with exit conditions and conditionals that branch based on data.

- Map Your Data Once, Reuse It

Create a single dictionary for card values at the top of your script, then reuse it every round. It’s cleaner than rewriting logic each time.

- Keep Logs Human + Machine Friendly

Your log lines should be short enough for the autograder to parse, but also clear enough that you can debug by reading them.

- Stretch Goal: Make the Game Fun

Add suit symbols (♥, ♦, ♣, ♠) or use string formatting to display rounds cleanly. While not graded, polish makes your project stand out.

## Grading and Points Breakdown

| Step | Requirement | Points |
|------|-------------|--------|
| 2 | Log shows `[STEP 2] Dev Container Started` in `logs/lab4_devcontainer.log` | 5 |
| 3 | `logs/jokes_postman_export.log` contains markers for START, POSTMAN_EXPORT_RUN, HTTP_OK, RAW_PRINTED, END | 10 |
| 4 | `logs/jokes_json.log` shows JSON header set, HTTP_OK, JSON_LOADED, and PPRINT_OK | 10 |
| 5 | `logs/jokes_json.log` includes JOKE_FIELD_OK and JOKE_PRINTED | 5 |
| 6 | `logs/jokes_loop.log` shows LOOP_BEGIN, JOKE_FIELD_OK, and either LOOP_CONTINUE or LOOP_STOP | 10 |
| 7 | `logs/high_card.log` shows DECK_CREATE_OK with valid deck_id | 5 |
| 8 | `logs/high_card.log` shows card draws for player and cpu, comparison, and winner or tie for at least one round | 15 |
| 9 | Any script log includes an ERR marker for a handled error case | 5 |
| 10 | All source code, data artifacts, and logs are committed and pushed; Pull Request opened | 10 |
|    | **Total Points** | **75** |



## Submission Checklist
:green_checkmark: Repo Cloned
:green_checkmark: Dev Container Opened
