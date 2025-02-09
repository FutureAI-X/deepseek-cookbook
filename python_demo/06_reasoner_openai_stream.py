from openai import OpenAI

client = OpenAI(api_key="sk-caa51fb1e83942b7a48076fabac307ab", base_url="https://api.deepseek.com")

messages = [{"role": "user", "content": "9.11和9.8哪个大"}]

response = client.chat.completions.create(
    model="deepseek-reasoner",
    messages=messages,
    stream=True
)

reasoning_content = ""
content = ""

for chunk in response:
    delta = chunk.choices[0].delta
    if delta.reasoning_content:
        reasoning_content += delta.reasoning_content
        print(delta.reasoning_content, end='', flush=True)
    elif delta.content:
        content += delta.content
        print(delta.content, end='', flush=True)

print("")
print(f"reasoning_content:{reasoning_content}")
print(f"content:{content}")