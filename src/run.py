import os

import openai


openai.api_key = os.getenv("OPENAI_API_KEY")


if __name__ == "__main__":
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {
                "role": "assistant",
                "content": "please share one historically significant event that happened on September 30.",
            },
        ],
    )
    print(response)
