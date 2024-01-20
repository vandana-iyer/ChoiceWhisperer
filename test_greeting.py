# test_plugin.py
import greeting
import os

def main():
    # Replace 'your_api_key_here' with your actual OpenAI API key
    api_key = os.environ['OPENAI_CHOICE_WHISPERER_KEY']  # It's recommended to use an environment variable in production

    # Create an instance of your plugin
    plugin = greeting.TimeBasedGreetingPlugin(api_key)

    # Example message to send
    test_message = "How should I dress for the weather today?"

    # Get the response from the plugin
    response = plugin.send_message_to_chatgpt(test_message)
    print("Response from ChatGPT:", response)

if __name__ == "__main__":
    main()
