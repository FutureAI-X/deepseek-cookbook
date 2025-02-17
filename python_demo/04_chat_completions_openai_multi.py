from openai import OpenAI

client = OpenAI(api_key="<API Key>", base_url="https://api.deepseek.com")

# Round1
messages = [{"role": "user", "content": "第二个是什么？"}]

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=messages
)

messages.append(response.choices[0].message)

print(messages)