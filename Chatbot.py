# -*- coding: utf-8 -*-
import random
import json
import os

class MyChatbot:
    def __init__(self):
        self.load_data()

    def load_data(self):
        # Get the full path to the data.json file
        script_dir = os.path.dirname(os.path.abspath(__file__))
        data_path = os.path.join(script_dir, 'data.json')

        # Load chatbot data from data.json file
        with open(data_path) as file:
            data = json.load(file)
            self.intents = data['intents']

    def get_response(self, user_input):
        user_input = user_input.lower()

        for intent in self.intents:
            for pattern in intent['patterns']:
                if self.match_pattern(user_input, pattern):
                    if intent['name'] == 'read_file':
                        self.load_data()
                        return "Data file loaded successfully!"
                    else:
                        return random.choice(intent['responses'])

        # If no match found, use the unknown intent responses
        unknown_intent = next((intent for intent in self.intents if intent['name'] == 'unknown'), None)
        return random.choice(unknown_intent['responses'])

    def match_pattern(self, user_input, pattern):
        # Check if the user input matches the pattern
        return user_input.startswith(pattern) or user_input.endswith(pattern)

def main():
    chatbot = MyChatbot()
    print("Chatbot: Hello! How can I assist you?")

    while True:
        user_input = input("You: ")
        if chatbot.match_pattern(user_input, 'bye'):
            print("Chatbot: Goodbye! Have a great day!")
            break

        response = chatbot.get_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()