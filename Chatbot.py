# -*- coding: utf-8 -*-
import json
import re

class SimpleChatbot:
    def __init__(self):
        self.load_intents_from_file("data.json")

    def load_intents_from_file(self, file_path):
        with open(file_path, "r") as file:
            self.intents = json.load(file)

    def handle_message(self, message):
        intent = self.get_intent(message)
        if intent == "greeting":
            return self.get_random_response(self.intents["greeting"])
        elif intent == "farewell":
            return self.get_random_response(self.intents["farewell"])
        elif intent == "question":
            return self.get_random_response(self.intents["question"])
        elif intent == "calculate":
            return self.calculate_result(message)
        else:
            return "I'm sorry, I don't understand that."

    def get_intent(self, message):
        for intent, patterns in self.intents["intents"].items():
            for pattern in patterns:
                if re.search(pattern, message):
                    return intent
        return None

    def get_random_response(self, responses):
        import random
        return random.choice(responses)

    def calculate_result(self, message):
        for pattern in self.intents["intents"]["calculate"]:
            match = re.search(pattern, message)
            if match:
                expression = match.group(1)
                try:
                    result = eval(expression)
                    return f"The result of {expression} is {result}."
                except Exception as e:
                    return f"Error: {str(e)}"
        return "I'm sorry, I couldn't understand the calculation."

def main():
    chatbot = SimpleChatbot()

    print("Chatbot: Hello! I'm a simple chatbot. How can I help you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye! Have a great day!")
            break

        response = chatbot.handle_message(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()