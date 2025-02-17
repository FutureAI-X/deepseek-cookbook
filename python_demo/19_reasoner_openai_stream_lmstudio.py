from openai import OpenAI

model_id = 'deepseek-r1-distill-qwen-7b'

client = OpenAI(
    base_url='http://127.0.0.1:1234/v1',
    api_key='lmstudio'
)

response = client.chat.completions.create(
    model=model_id,
    messages=[{"role":"user", "content":"9.11和9.8哪个大？请逐步推理"}],
    stream=True
)

for chunk in response:
    print(chunk.choices[0].delta.content, end='', flush=True)