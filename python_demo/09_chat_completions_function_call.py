from openai import OpenAI

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "获取天气情况",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "城市名称",
                    }
                },
                "required": ["location"]
            },
        }
    },
]

client = OpenAI(
    api_key="<API Key>",
    base_url="https://api.deepseek.com",
)

def send_messages(messages):
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=messages,
        tools=tools
    )
    return response.choices[0].message

messages = [{"role": "user", "content": "杭州今天天气怎么样?"}]
message = send_messages(messages)
print(f"模型第一次返回的消息：{message.to_json()}")

tool = message.tool_calls[0]
messages.append(message)

messages.append({"role": "tool", "tool_call_id": tool.id, "content": "24℃"})
message_second = send_messages(messages)
print(f"模型第二次返回的消息：{message_second.to_json()}")

print("========================")
print(messages)