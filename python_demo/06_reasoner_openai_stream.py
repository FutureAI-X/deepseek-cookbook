from openai import OpenAI

client = OpenAI(api_key="<API Key>", base_url="https://api.deepseek.com")

messages = [{"role": "user", "content": "9.11和9.8哪个大"}]

response = client.chat.completions.create(
    model="deepseek-reasoner",
    messages=messages,
    stream=True
)

done_reasoning = False

for chunk in response:
    reasoning_chunk = chunk.choices[0].delta.reasoning_content
    answer_chunk = chunk.choices[0].delta.content
    if reasoning_chunk != '' and reasoning_chunk is not None:
        print(reasoning_chunk, end='',flush=True)
    elif answer_chunk != '' and answer_chunk is not None:
        if not done_reasoning:
            print('\n\n=== Final Answer ===\n\n')
            done_reasoning = True
        print(answer_chunk, end='',flush=True)