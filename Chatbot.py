# -*- coding: utf-8 -*-
import json
import re
import tkinter as tk
from tkinter import scrolledtext

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

class SimpleChatbotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Chatbot GUI")

        self.chatbot = SimpleChatbot()

        self.chat_log = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10)
        self.chat_log.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

        self.user_input = tk.Entry(root, width=30)
        self.user_input.grid(row=1, column=0, padx=10, pady=10)

        self.send_button = tk.Button(root, text="Send", command=self.send_message)
        self.send_button.grid(row=1, column=1, padx=10, pady=10)

        # Display initial greeting
        self.chat_log.insert(tk.END, "Chatbot: Hello! I'm a simple chatbot. How can I help you today?\n")

    def send_message(self):
        user_message = self.user_input.get()
        self.chat_log.insert(tk.END, "You: " + user_message + "\n")
        if user_message.lower() == "exit":
            response = "Chatbot: Goodbye! Have a great day!"
            self.chat_log.insert(tk.END, response + "\n")
            self.root.after(2000, self.root.destroy)
        else:
            response = self.chatbot.handle_message(user_message)
            self.chat_log.insert(tk.END, "Chatbot: " + response + "\n")

def main():
    root = tk.Tk()
    chatbot_gui = SimpleChatbotGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
