import transformers

chat_tokenizer_dir = "./"

tokenizer = transformers.AutoTokenizer.from_pretrained(chat_tokenizer_dir, trust_remote_code=True)

result = tokenizer.encode("你好！很高兴见到你，有什么我可以帮忙的吗？")
print(f"Token 化的结果是：{result}")
print(f"Token 用量：{len(result)}")
