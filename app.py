import openai
import os

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")  # Store your API key in an environment variable

def chat_with_gpt4_turbo(messages):
    """
    Function to interact with the GPT-4 Turbo model via OpenAI's API.
    Parameters:
        messages (list): Conversation history as a list of dictionaries.
    Returns:
        str: Assistant's response.
    """
    try:
        # Call the OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-4-turbo",  # Use GPT-4 Turbo
            messages=messages,
            temperature=0.7,  # Adjust for creativity
            max_tokens=800,   # Control response length
            n=1  # Generate one response
        )
        # Extract and return the assistant's reply
        return response.choices[0].message["content"]
    except openai.error.OpenAIError as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    print("ChatGPT GPT-4 Turbo Client. Type 'exit' to quit.\n")

    # Initialize conversation history
    conversation = [
        {"role": "system", "content": "You are a helpful and knowledgeable assistant."}
    ]

    while True:
        # Get user input
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        # Append user's message to the conversation
        conversation.append({"role": "user", "content": user_input})

        # Get GPT-4 Turbo's response
        assistant_reply = chat_with_gpt4_turbo(conversation)
        print("ChatGPT:", assistant_reply)

        # Append assistant's reply to the conversation
        conversation.append({"role": "assistant", "content": assistant_reply})