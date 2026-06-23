print("🤖 Welcome to CodSoft AI Chatbot")
print("Type 'bye' to exit.\n")

while True:
    user = input("You: ").lower()

    if user == "hello":
        print("Bot: Hello! How are you?")
    elif user == "hi":
        print("Bot: Hi! Nice to meet you.")
    elif user == "how are you":
        print("Bot: I am fine. Thanks for asking!")
    elif user == "your name":
        print("Bot: I am CodSoft AI Chatbot.")
    elif user == "bye":
        print("Bot: Goodbye! Have a great day.")
        break
    else:
        print("Bot: Sorry, I don't understand.")