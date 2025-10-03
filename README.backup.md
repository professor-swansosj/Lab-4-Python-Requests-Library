# Lab 4 Python Requests Library

## :triangular_flag_on_post: Learning Goals
- **Understand the role of the Python `requests` ** as a higher-level way to interact with HTTP APIs compared to tools like cURL or Postman
- **Write a Python script that performs an API request**, receives JSON data, and parses it into usable Python objects (dictionaries, lists)
- **Extract specific fields from JSON responses**, focusing only on the relevant data (e.g., pulling just the `joke` string from the Dad Jokes API).
- **Implement basic program flow with loops and conditionals** to repeatedly query an API until a condition is met (e.g., user input “yes, I laughed”)
- **Practice user interaction in scripts**, combining automated API calls with input prompts to create a simple conversational experience
- **Use an API that requires multiple calls in sequence** (e.g., shuffle a deck, then draw a card using the Deck of Cards API)
- **Apply program logic to simulate a simple game**, comparing card values between user and computer, and repeating the game loop until the user quits
- **Strengthen skills with functions and modular code design** (e.g., one function for drawing a joke, another for evaluating game outcomes)
- **Build confidence bridging HTTP concepts into Python programming**, setting the stage for using APIs in real-world network automation

## :globe_with_meridians: Overview:
In this lab, you will build on your experience with APIs by moving from cURL and Postman into Python programming with the `requests` library. Instead of manually sending requests from the command line or a GUI, you’ll write scripts that call APIs, parse JSON responses, and interact with users. This is the same process professional developers and network engineers use to automate tasks and integrate external services into their workflows.

You’ll start by writing a script that connects to the Dad Jokes API, pulls a random joke, and displays it in the terminal. From there, you’ll add user interaction so the program keeps fetching new jokes until you say you’ve laughed, ending with a friendly message. Next, you’ll tackle the Deck of Cards API, where you’ll generate a standard Vegas-style deck and write a simple game: both you and the computer draw one card, and the higher card wins. The script will loop so you can play multiple rounds. By the end of the lab, you’ll have combined API calls, JSON parsing, loops, and user input to create two functional programs that demonstrate how Python can make APIs practical and fun.

### Introduction to the Python Requests Library
The Python `requests` library is one of the most popular tools for working with web APIs because it makes sending HTTP requests and handling responses simple and intuitive. Instead of typing long cURL commands or clicking through Postman, you can write just a few lines of Python code to perform the same actions. The library handles all the details of connecting to a server, sending headers, and formatting data, so you can focus on using the results in your program.

With `requests`, you can send a GET request to an API, receive a response in JSON format, and immediately work with it as Python data—no extra parsing steps required. This allows you to integrate APIs directly into scripts, automate repetitive tasks, or even build larger applications. In this lab, you’ll use `requests` to call real APIs, extract meaningful data, and combine it with user interaction, giving you a taste of how developers and engineers use APIs in real-world automation projects.

### Making Your First API Call in Python
Your first step with the `requests` library is to send a simple GET request to an API endpoint and see what comes back. This is very similar to using cURL, but instead of typing a command into the terminal, you’ll write a short Python script. A basic request looks like this:

```python

import requests

response = requests.get("https://api.github.com")
print(response.text)

```

In this example, `requests.get()` sends the HTTP request, and the response object contains everything the server sends back. Printing `response.text` shows the raw data, which might include JSON, HTML, or plain text depending on the API. You can also check `response.status_code` to confirm whether the request was successful (a `200` code means “OK”).

This simple call demonstrates how Python can take the place of cURL or Postman: the same concepts of methods, headers, and responses apply, but now you can store the data, process it, and build interactive programs around it.

### Working with JSON Responses
Most modern APIs return data in JSON format, which is easy for both humans and programs to read. In Python, the requests library makes it straightforward to work with this kind of response. Instead of dealing with raw text, you can call the .json() method on the response object to automatically convert the data into Python types like dictionaries and lists.

```python

import requests

response = requests.get("https://icanhazdadjoke.com/", headers={"Accept": "application/json"})
data = response.json()
print(data)

```

The variable `data` now holds a Python dictionary, so you can access specific fields using keys. If the JSON includes `{"joke": "I'm afraid for the calendar. Its days are numbered."}`, you can print just the joke with `print(data["joke"])`. This ability to pull out exactly the values you need is what makes JSON so powerful when combined with Python—it allows your scripts to interact with APIs in a precise and programmable way.

### Dad Jokes Script: Fetching and Parsing Jokes
Now that you know how to send a request and parse JSON, you’ll create your first full script using the Dad Jokes API. The goal is to make the program interactive: it should fetch a random joke, display it in the terminal, and then ask you if you laughed. If you didn’t, the script should loop back, call the API again, and print another joke. This continues until you confirm that you laughed, at which point the program ends with a friendly message such as “Glad I could make you laugh today!”

This exercise gives you practice combining three important skills: making API calls with requests, extracting specific fields from JSON responses (in this case, the "joke" key), and using control flow in Python (loops and conditionals) to build interactive behavior. By the end of this step, you’ll have a working script that goes beyond just printing raw data—it creates a simple, user-driven experience powered by an API.

### Adding User Interaction and Loops
User interaction turns a one-off API call into a simple application. In Python, `input()` lets you capture what the user types (e.g., “Did you laugh? yes/no”), and conditionals (`if/elif/else`) decide what to do next based on that response. Pair this with a loop (`while True:` or a boolean flag) and you can repeat actions—like fetching another joke—until a stopping condition is met. This pattern is the backbone of many automation scripts: prompt → act → evaluate → repeat or exit.

Good interaction also means handling messy reality. Users mistype, press Enter without answering, or provide unexpected input. Normalize responses (e.g., `.strip().lower()`), validate them, and give clear feedback before continuing. Keep network calls inside functions so the loop stays readable (`get_joke()`, `user_laughed()`), and separate concerns: one function fetches data, another renders output, a third decides whether to continue. This structure makes your script easier to test and extend later (for example, swapping the Dad Jokes API for another source without rewriting your loop).

### Deck of Cards Script: Creating and Using a Deck
The Deck of Cards API is slightly more complex than the Dad Jokes API because it requires multiple steps to use. First, you’ll make a request to create a new shuffled deck. The API responds with a JSON object that includes a unique deck_id—this value identifies your deck and must be included in later requests. With that ID, you can then draw cards one at a time or in groups. Each draw returns details such as the card’s value, suit, and an image URL.

This exercise shows you how APIs often work in sequences: one call sets up state (shuffling a deck), and another call manipulates that state (drawing cards). By parsing JSON and storing values like `deck_id`, your script can maintain a conversation with the API instead of just asking for a single piece of data. Think of `deck_id` as a session token that keeps your deck consistent across requests. Understanding this flow prepares you for real-world APIs where actions are chained together and responses from one request become inputs for the next.

### Building the Simple Highest Card Game
You’ll turn API calls into a tiny game loop: the script draws one card for the player and one for the computer from the same deck, compares their ranks, announces the winner, and then asks whether to play again. The key idea is mapping card faces to numeric ranks so comparison is trivial—e.g., `{"2":2, ..., "10":10, "JACK":11, "QUEEN":12, "KING":13, "ACE":14}`. After you create a shuffled deck and store its `deck_id`, each round simply draws two cards via the API, translates their `"value"` fields using your rank map, and compares integers. Handle ties by declaring a draw and offering a rematch.

Keep the logic clean by separating concerns: one function draws `n` cards and returns parsed results; another converts card values to ranks; a third compares and prints the outcome. The outer loop manages user input (`play again?`), normalizing responses and exiting gracefully. This structure mirrors real automation patterns—API interaction at the edges, pure decision logic in the middle—so it’s easy to test, reason about, and extend later (for example, switching from single-card to multi-card totals).

### Error Handling and Edge Cases
APIs fail in creative ways, so your scripts should assume things can go wrong and recover gracefully. Network calls may timeout, return non-200 status codes (401/403 auth errors, 404 not found, 429 rate limit, 5xx server errors), or respond with malformed/empty JSON. In Python, wrap requests in `try/except`, set a timeout, and check `response.ok` or call `response.raise_for_status()` to surface errors early. When parsing JSON, guard lookups with `.get("key")` or handle `KeyError/ValueError` to avoid crashes if fields are missing. For retryable errors (timeouts, transient 5xx), use a limited retry with small delays (or exponential backoff). Log a clear message and fall back safely if recovery fails.

For your labs’ logic, protect the loop. Cap the number of joke fetches so a broken API doesn’t create an infinite loop; handle unexpected user input by normalizing and reprompting; and allow a clean exit (e.g., user types `q` or presses Ctrl+C). With the Deck of Cards flow, watch for an exhausted deck (no cards remaining), a missing/invalid `deck_id`, or partial draws; detect these conditions and reshuffle or recreate the deck as needed. When comparing card ranks, validate that values are known (e.g., face cards map correctly) and handle ties predictably. Good error handling isn’t just defensive—it makes your program’s behavior predictable and explainable, which is exactly what you want in automation.

---

## :card_file_box: File Structure:

'''
file structure
'''

---

## Components
text

### 1. **Component 1**
text

### 2. **Component 2**
text

### 3. **Component 3**
text

## :memo: Instructions
1. text
2. text
3. text

## :page_facing_up: Logging
text

## :green_checkmark: Grading Breakdown
- x pts: 
- x pts:
- x pts: