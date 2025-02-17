from openai import OpenAI

client = OpenAI(
    api_key="<API Key>",
    base_url="https://api.deepseek.com/beta",
)

messages = [
    {"role": "user", "content": "写一段统计单词中某个字母个数的代码"},
    {"role": "assistant", "content": "```python\n", "prefix": True}
]

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=messages,
    stop=["```"],
)

print(response.to_json())