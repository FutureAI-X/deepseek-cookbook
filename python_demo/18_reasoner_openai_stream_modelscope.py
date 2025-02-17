from openai import OpenAI

model_id = 'unsloth/DeepSeek-R1-Distill-Qwen-7B-GGUF'

client = OpenAI(
    base_url='https://ms-fc-e860840d-3699.api-inference.modelscope.cn/v1',
    api_key='<API Key>'
)

response=client.chat.completions.create(
    model=model_id,
    messages=[{"role":"user", "content":"9.11和9.8哪个大？请逐步推理"}],
    stream=True
)

for chunk in response:
    print(chunk.choices[0].delta.content, end='', flush=True)