import sys

def chatbot_response(user_input):
    responses = {
        "hello": "Hi there! How can I help you?",
        "how are you": "I'm just a bot, but I'm doing great!",
        "bye": "Goodbye! Have a great day!",
        "what is your name": "I'm ChatBot, your virtual assistant."
    }
    return responses.get(user_input.lower(), "I'm not sure how to respond to that.")

def chat_cli():
    print("Hello and Welcome to ChatBot.ai!")
    print("ChatBot: Hello! Type 'exit' to end the chat.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("ChatBot: Goodbye!")
            break
        response = chatbot_response(user_input)
        print(f"ChatBot: {response}")

if __name__ == "__main__":
    if sys.stdin.isatty():
        chat_cli()
    else:
        print("Error: This chatbot requires an interactive environment.")


        
