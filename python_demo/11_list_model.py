from openai import OpenAI

# for backward compatibility, you can still use `https://api.deepseek.com/v1` as `base_url`.
client = OpenAI(api_key="<API Key>", base_url="https://api.deepseek.com")
print(client.models.list())