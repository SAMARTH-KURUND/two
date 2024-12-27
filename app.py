import nltk


from nltk.chat.util import Chat, reflections

# Download required resources
nltk.download('punkt')

# Define pairs for the chatbot (patterns and responses)
pairs = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey! How can I assist you?']),
    (r'what is your name?', ['I am a chatbot created by SAMARTH KURUND.']),
    (r'how are you?', ['I am doing great, thank you! How about you?']),
    (r'quit|exit', ['Goodbye! Take care.']),
    (r'I need help with python', ['Sure! How can I assist you with %1?']),
    (r'what is (.*)', ['I’m not sure, but I can look it up for you!']),
    (r'(.*)', ['I’m sorry, I didn’t understand that. Could you rephrase?']),
]

# Create the chatbot
chatbot = Chat(pairs, reflections)


# Function to start the chatbot conversation
def start_chat():
    print("Chatbot: Hello! How can I assist you today? (Type 'exit' to end the conversation.)")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Chatbot: Goodbye! Take care.")
            break
        response = chatbot.respond(user_input)
        print(f"Chatbot: {response}")


# Start the chatbot
if __name__ == "__main__":

    start_chat()
start_chat()

