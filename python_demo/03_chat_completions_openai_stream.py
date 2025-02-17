from openai import OpenAI
import time

client = OpenAI(api_key="<API Key>", base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "你好"},
  ],
    max_tokens=1024,
    temperature=0.7,
    stream=True
)

for chunk in response:
    # 获取数据内容
    delta = chunk.choices[0].delta
    content = delta.content if hasattr(delta, 'content') else ""

    # 增加 0.2 秒的阻断，方便查询流式输出效果
    time.sleep(0.2)

    print(content, end='', flush=True)