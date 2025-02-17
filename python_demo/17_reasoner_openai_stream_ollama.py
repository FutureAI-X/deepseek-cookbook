from openai import OpenAI

client = OpenAI(api_key="ollama", base_url="http://localhost:11434/v1/")

messages = [{"role": "user", "content": "9.11和9.8哪个大？请逐步推理"}]

response = client.chat.completions.create(
    model="modelscope.cn/unsloth/DeepSeek-R1-Distill-Qwen-7B-GGUF:Q4_K_M",
    messages=messages,
    stream=True
)

# 查看消息格式
for chunk in response:
    print(chunk.choices[0].delta.content, end='', flush=True)