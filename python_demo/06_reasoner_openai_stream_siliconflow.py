from openai import OpenAI

client = OpenAI(api_key="sk-mriefpscmvqlyjfhwvtrryjubgvthnvccnwgsqriiagsqgvm", base_url="https://api.siliconflow.cn/v1")

messages = [{"role": "user", "content": "9.11和9.8哪个大"}]

response = client.chat.completions.create(
    model="deepseek-ai/DeepSeek-R1",
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