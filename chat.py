import os
from openai import OpenAI

# 设置环境变量 OPENAI_API_KEY
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

def chat_with_gpt(prompt: str):
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
    )
    return resp.choices[0].message.content

if __name__ == "__main__":
    user_input = input("你想问 GPT 什么？ ")
    print("GPT:", chat_with_gpt(user_input))
