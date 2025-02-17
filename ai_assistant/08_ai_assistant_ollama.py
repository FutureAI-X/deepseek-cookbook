import streamlit as st
from openai import OpenAI

client = OpenAI(api_key="ollama", base_url="http://localhost:11434/v1/")

def generate_response(messages):
    response = client.chat.completions.create(
        model="modelscope.cn/unsloth/DeepSeek-R1-Distill-Qwen-7B-GGUF:Q4_K_M",
        messages=messages,
        stream=True
    )
    return response


st.title("AI 助手 (Ollama) 😊")

# 初始化消息列表
if "messages" not in st.session_state:
    st.session_state.messages = []

# 显示消息列表（应用启动时）
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("请输入内容")

if prompt:
    # 打印用户输入
    with st.chat_message("user"):
        st.markdown(prompt)
    # 将用户输入添加到消息列表中
    st.session_state.messages.append({"role": "user", "content": prompt})

    stream = generate_response(st.session_state.messages)
    # 打印助手回复
    with st.chat_message("assistant"):
        response = st.write_stream(stream)
    # 将助手回复添加到消息列表中
    st.session_state.messages.append({"role": "assistant", "content": response})