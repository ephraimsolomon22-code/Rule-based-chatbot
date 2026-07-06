"""
Simple Rule-Based Chatbot
A beginner-friendly chatbot that responds to user input using
keyword matching and pattern rules (no AI/ML model — pure logic).

Author: Ephraim Solomon
"""

import random

# Dictionary of keywords mapped to possible responses
responses = {
    "hello": ["Hi there!", "Hello!", "Hey, how can I help you today?"],
    "how are you": [" I'm doing great!", "Feeling good, thanks for asking!"],
    "name": ["I'm chibi, your friendly rule-based assistant.", "You can call me Chi."],
    "bye": ["Goodbye! Have a great day!", "See you later!", "Bye! Take care."],
    "help": ["I can chat about simple things. Try asking my name, how I am, or say hello!"],
    "study": ["Studying is the key to success. What subject are you working on?"],
    "korea": ["Korea has an amazing tech scene! Are you preparing for GKS?"],
    "japan": ["Japan is known for its innovation. MEXT scholarship, perhaps?"],
}

default_responses = [
    "I'm not sure I understand. Can you rephrase that?",
    "Hmm, I don't have a response for that yet.",
]


def get_response(user_input):
    """Check user input for known keywords and return a matching response."""
    user_input = user_input.lower()

    for keyword, reply_list in responses.items():
        if keyword in user_input:
            return random.choice(reply_list)

    return random.choice(default_responses)


def chat():
    """Main loop to run the chatbot in the terminal."""
    print("ChatBot: Hello! Type 'bye' to exit.")

    while True:
        user_input = input("You: ")

        if "bye" in user_input.lower():
            print("ChatBot:", random.choice(responses["bye"]))
            break

        reply = get_response(user_input)
        print("ChatBot:", reply)


if __name__ == "__main__":
    chat()
