import sys
import json

DEFAULT_RESPONSES = {
    "hello": "Hi there! How can I help you?",
    "how are you": "I'm just a bot, but I'm doing great!",
    "bye": "Goodbye! Have a great day!",
    "what is your name": "I'm ChatBot, your virtual assistant.",
    "help": "You can ask me things like 'hello', 'how are you', or 'what is your name'."
}

def load_responses(file_path="responses.json"):
    """Load chatbot responses from a JSON file, falling back to default responses."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return DEFAULT_RESPONSES

def preprocess_input(user_input):
    """Preprocess user input to standardize format before looking up responses."""
    return user_input.strip().lower()

def chatbot_response(user_input, responses):
    """Retrieve chatbot response for the given user input."""
    processed_input = preprocess_input(user_input)
    return responses.get(processed_input, "I'm not sure how to respond to that.")

def chat_cli():
    """Run the chatbot in a command-line interface."""
    responses = load_responses()
    print("ChatBot: Hello! Type 'exit' to end the chat.")
    while True:
        try:
            user_input = input("You: ")
            processed_input = preprocess_input(user_input)
            if processed_input == "exit":
                print("ChatBot: Goodbye!")
                break
            response = chatbot_response(user_input, responses)
            print(f"ChatBot: {response}")
        except (KeyboardInterrupt, EOFError):
            print("\nChatBot: Goodbye!")
            break

def chat_batch():
    """Process chatbot responses in batch mode from standard input."""
    responses = load_responses()
    for line in sys.stdin:
        processed_input = preprocess_input(line)
        if processed_input == "exit":
            break
        print(f"ChatBot: {chatbot_response(processed_input, responses)}")

if __name__ == "__main__":
    if sys.stdin.isatty():
        chat_cli()
    else:
        chat_batch()

