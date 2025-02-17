from openai import OpenAI

openai_api_base = "http://localhost:8000/v1"
openai_api_key= "EMPTY"

client = OpenAI(
    api_key=openai_api_key,
    base_url=openai_api_base,
)

response = client.chat.completions.create(
    model="deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "9.11和9.8哪个大"},
    ],
    temperature=0.0,
    max_tokens=512,
    stream=True
)

for chunk in response:
    print(chunk.choices[0].delta.content, end='', flush=True)