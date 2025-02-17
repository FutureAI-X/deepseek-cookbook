from openai import OpenAI

client = OpenAI(
    api_key="<API Key>",
    base_url="https://api.deepseek.com/beta"
)

response = client.completions.create(
    model="deepseek-chat",
    prompt="def count_letter(word, letter):",
    echo=True,
    max_tokens=128
)

print(response.choices[0].text)