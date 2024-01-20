from datetime import datetime

import openai

class TimeBasedGreetingPlugin:
    def __init__(self, api_key):
        openai.api_key = api_key

    def get_greeting(self):
        current_hour = datetime.now().hour
        if 5 <= current_hour < 12:
            return "Good morning!"
        elif 12 <= current_hour < 18:
            return "Good afternoon!"
        else:
            return "Good evening!"

    def send_message_to_chatgpt(self, message):
        greeting = self.get_greeting()
        response = openai.Completion.create(
            model="gpt-3.5-turbo-instruct",  # or the latest model
            prompt=f"{greeting} {message}",
            max_tokens=50
        )
        return response.choices[0].text.strip()