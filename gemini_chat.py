import requests
import json

# → 已填入你的真实 API Key，请妥善保管
API_KEY = "AIzaSyDvJXpJmeLMNg-g5LGXk2Y3sASrTVLJI9E"
MODEL = "models/gemini-1.5-flash-latest"

# 拼接请求 URL，使用 API_KEY 变量
API_URL = f"https://generativelanguage.googleapis.com/v1beta/{MODEL}:generateContent?key={API_KEY}"

def chat_with_gemini(prompt):
    headers = {"Content-Type": "application/json"}
    data = {
        "contents": [
            {"parts": [{"text": prompt}]}
        ]
    }

    try:
        print("向 Gemini 发送请求...")
        response = requests.post(API_URL, headers=headers, data=json.dumps(data), timeout=30)
        response.raise_for_status()
        result = response.json()
        # 解析返回的文本
        return result['candidates'][0]['content']['parts'][0]['text']
    except Exception as e:
        print("出错：", e)
        return "（请求失败）"

if __name__ == "__main__":
    while True:
        user_input = input("你想问 Gemini 什么？ ")
        if user_input.lower() in ["exit", "quit"]:
            break
        reply = chat_with_gemini(user_input)
        print("Gemini:", reply)
