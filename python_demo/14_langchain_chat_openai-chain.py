from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

llm = ChatOpenAI(
    base_url="https://api.deepseek.com",
    api_key="<API Key>",
    model_name="deepseek-chat",
    temperature=0
)

prompt = ChatPromptTemplate(
    [
        (
            "system",
            "You are a helpful assistant that translates {input_language} to {output_language}.",
        ),
        ("human", "{input}"),
    ]
)

chain = prompt | llm

response = chain.invoke(
    {
        "input_language": "English",
        "output_language": "German",
        "input": "I love this course",
    }
)

print(response)