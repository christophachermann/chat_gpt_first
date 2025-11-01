from openai import OpenAI
import os

# Lade den API-Key aus der Umgebungsvariablen
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("API key not found. Please set OPENAI_API_KEY before running the script.")

client = OpenAI(api_key=api_key)

def chat_with_gpt(prompt):
    """Send a prompt to GPT and return its response text."""
    response = client.responses.create(
        model="gpt-5",
        input=prompt
    )
    return response.output[0].content[0].text  # Access correct text field

if __name__ == "__main__":
    print("Chatbot started. Type 'quit', 'exit', or 'bye' to stop.\n")
    while True:
        user_input = input("You: ")

        if user_input.lower() in ["quit", "exit", "bye"]:
            print("Chatbot: Goodbye! 👋")
            break

        response = chat_with_gpt(user_input)
        print("Chatbot:", response)