from openai import OpenAI
client = OpenAI(api_key="<API Key>", base_url="https://api.deepseek.com")

messages = [{"role": "user", "content": "9.11和9.8哪个大"}]

response = client.chat.completions.create(
    model="deepseek-reasoner",
    messages=messages,
    stream=False
)

print(f"返回体：{response.to_json()}")

reasoning_content = response.choices[0].message.reasoning_content
print(f"思维链：{reasoning_content}")

content = response.choices[0].message.content
print(f"最终输出：{content}")