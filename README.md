# Simple Rule-Based Chatbot

A beginner Python chatbot that responds to user messages using keyword
matching — no external libraries or AI models, just core Python logic
(dictionaries, loops, and conditionals).

## What it does
- Takes user input in the terminal
- Matches keywords (like "hello", "name", "help") to pre-written responses
- Picks a random response from a list for variety
- Exits when the user types "bye"

## How to run
```bash
python3 chatbot.py
```

## Example
```
ChatBot: Hello! Type 'bye' to exit.
You: hello
ChatBot: Hi there!
You: how are you
ChatBot: I'm just a program, but I'm doing great!
You: bye
ChatBot: See you later!
```

## What I learned
- Using dictionaries to map keywords to response lists
- Writing clean functions with a single responsibility
- Basic control flow with `while` loops and `if` conditions
- This is a stepping stone toward real NLP/AI chatbots — a natural next
  step would be adding intent classification with a simple ML model.

## Author
Ephraim Solomon
