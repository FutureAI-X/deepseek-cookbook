from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    base_url="https://api.deepseek.com",
    api_key="<API Key>",
    model="deepseek-chat",
    temperature=0
)

messages = [
    (
        "system",
        "You are a helpful assistant that translates English to Chinese. Translate the user sentence.",
    ),
    ("human", "I love this course"),
]

ai_msg = llm.invoke(messages)

print(ai_msg)