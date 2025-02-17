import json
from openai import OpenAI

client = OpenAI(
    api_key="<API Key>",
    base_url="https://api.deepseek.com",
)

system_prompt = """
The user will provide some exam text. Please parse the "question" and "answer" and output them in JSON format. 

EXAMPLE INPUT: 
世界上最高的山峰是哪座？珠穆朗玛峰

EXAMPLE JSON OUTPUT:
{
    "question": "世界上最高的山峰是哪座？",
    "answer": "珠穆朗玛峰"
}
"""

user_prompt = "世界上最长的河流是哪一条？尼罗河"

messages = [{"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}]

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=messages,
    response_format={
        'type': 'json_object'
    }
)

print(json.loads(response.choices[0].message.content))