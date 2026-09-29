
import random
from datetime import datetime

# Welcome message
print("=" * 40)
print("       Welcome to PyBot!")
print("=" * 40)

print("Type 'help' to see what I can do.")
print("Type 'bye' to exit.\n")

# Ask user's name
name = input("Bot: What is your name? ").strip()

if name == "":
    name = "Friend"

print(f"Bot: Nice to meet you, {name}!")

# Main chatbot loop
while True:

    user_input = input(f"\n{name}: ").lower().strip()

    # Greetings
    if user_input in ["hello", "hi", "hey"]:
        print("Bot:", random.choice([
            "Hello! How are you?",
            "Hey there!",
            "Hi! Nice to talk to you."
        ]))

    # Ask how the bot is feeling
    elif "how are you" in user_input:
        print("Bot: I'm doing great! Thanks for asking.")

    # Ask the bot's name
    elif "your name" in user_input:
        print("Bot: My name is PyBot!")

    # Ask for the user's name
    elif "my name" in user_input:
        print(f"Bot: Your name is {name}!")

    # Ask for the current time
    elif "time" in user_input:
        current_time = datetime.now().strftime("%I:%M %p")
        print(f"Bot: The current time is {current_time}.")

    # Ask for today's date
    elif "date" in user_input:
        current_date = datetime.now().strftime("%d-%m-%Y")
        print(f"Bot: Today's date is {current_date}.")

    # Tell a joke
    elif "joke" in user_input:
        print("Bot:", random.choice([
            "Why do programmers prefer dark mode? "
            "Because light attracts bugs!",
            "Why did the computer go to the doctor? "
            "Because it had a virus!",
            "Why was the Python programmer confused? "
            "Because he couldn't find his variables!"
        ]))

    # Ask for help
    elif user_input == "help":
        print("\nBot: Here are the things I can do:")
        print("1. Say hello")
        print("2. Tell you my name")
        print("3. Tell you the current time")
        print("4. Tell you today's date")
        print("5. Tell you a joke")
        print("6. Say goodbye")

    # Say thank you
    elif "thank" in user_input:
        print("Bot: You're welcome!")

    # Exit chatbot
    elif user_input in ["bye", "exit", "quit"]:
        print(f"Bot: Goodbye, {name}! Have a great day!")
        break

    # Default response
    else:
        print("Bot: Sorry, I don't understand that yet.")
        print("Bot: Type 'help' to see what I can do.")

print("\nChatbot closed.")
