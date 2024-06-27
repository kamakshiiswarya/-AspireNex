# Simple Chatbot

import re

# Predefined rules and responses
rules = {
    r"hello|hi|hey": "Hello! How can I assist you today?",
    r"what is your name": "My name is Chatty, nice to meet you!",
    r"how are you": "I'm doing well, thanks for asking!",
    r"what can you do": "I can answer questions, provide information, and chat with you!",
    r"goodbye|bye|see you": "Goodbye! It was nice chatting with you.",
    r"default": "I didn't understand that. Can you please rephrase?"
}

# Chatbot function
def chatbot(user_input):
    user_input = user_input.lower()
    for pattern, response in rules.items():
        if re.match(pattern, user_input):
            return response
    return rules["default"]

# Main loop
while True:
    user_input = input("You: ")
    response = chatbot(user_input)
    print("Chatty: " + response)
