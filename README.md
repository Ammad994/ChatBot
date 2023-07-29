# Simple Chatbot

This is a simple chatbot implemented in Python that uses a JSON file to store intents and responses.

## Overview

This chatbot is designed to handle basic greetings, farewells, general questions, and simple calculations. It uses regular expressions to match user input with predefined patterns in the JSON file to determine the intent of the user's message and respond accordingly.

## Requirements

- Python 3.x
- tkinter (for GUI)

## Installation

1. Clone the repository:

git clone "https://github.com/Ammad994/ChatBot.git"
cd simple-chatbot

2. Create a virtual environment (optional but recommended):

python -m venv venv
source venv/bin/activate # For Windows, use venv\Scripts\activate


3. Install the required packages:

pip install -r requirements.txt

## Usage

1. Run the chatbot in the terminal:

python chatbot.py


2. The chatbot will greet you and prompt you to enter your message. Type your message and press Enter to see the chatbot's response. To exit the chatbot, type "exit".

3. To use the chatbot with a graphical user interface (GUI), run the GUI version:

python chatbot_gui.py

4. The GUI version will open a window with a chat interface. Type your message in the input box and click the "Send" button to see the chatbot's response. Click the "Clear" button to clear the chat history. To exit the chatbot, click the "Exit" button.

## Customization

You can customize the chatbot's responses by editing the `data.json` file. The JSON file contains different intents, each with corresponding patterns and responses. You can add new intents or modify existing ones to tailor the chatbot's behavior to your needs.

## JSON Format

The `data.json` file contains the following structure:

```json
{
  "intents": {
    "greeting": {
      "patterns": ["hello", "hi", "hey"],
      "responses": ["Hello! How can I assist you?", "Hi there! How can I help?"]
    },
    "farewell": {
      "patterns": ["bye", "goodbye"],
      "responses": ["Goodbye! Have a great day!", "See you later!"]
    },
    "question": {
      "patterns": ["what", "when", "why", "how", "where"],
      "responses": ["I'm not sure. Can you provide more information?", "I'll do my best to help. What specifically do you want to know?"]
    },
    "calculate": {
      "patterns": ["calculate (.+)"],
      "responses": ["The result of {0} is {1}."]
    }
  }
}



Feel free to modify the patterns and responses to enhance the chatbot's capabilities.

