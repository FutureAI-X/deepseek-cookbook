from openai import OpenAI

client = OpenAI(api_key="<API Key>", base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "你好"},
  ],
    max_tokens=1024,
    temperature=0.7,
    stream=False
)

print(response.to_json())