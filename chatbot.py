# chatbot.py

def chatbot():
    print("🤖 Chatbot: Hello! I am your assistant. Type 'exit' to quit.")

    while True:
        user_input = input("👤 You: ").lower()  # lowercase for easy comparison

        if user_input == "hello":
            print("🤖 Chatbot: Hi there! How can I help you?")
        elif user_input == "hi":
            print("🤖 Chatbot: Hello! How are you today?")
        elif "how are you" in user_input:
            print("🤖 Chatbot: I'm just a bot, but I'm doing great! 😊")
        elif "your name" in user_input:
            print("🤖 Chatbot: I’m CodBot, your friendly assistant.")
        elif "help" in user_input:
            print("🤖 Chatbot: I can answer basic questions like greetings, about me, etc.")
        elif user_input == "bye":
            print("🤖 Chatbot: Goodbye! Have a great day! 👋")
            break
        elif user_input == "exit":
            print("🤖 Chatbot: Chat ended.")
            break
        else:
            print("🤖 Chatbot: Sorry, I didn't understand that. Try something else.")

# Run chatbot
if __name__ == "__main__":
    chatbot()
