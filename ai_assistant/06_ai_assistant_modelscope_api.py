import streamlit as st
from openai import OpenAI

client = OpenAI(api_key="f4885373-679d-4a77-87e1-f913989e1152", base_url="https://api-inference.modelscope.cn/v1/")
def generate_response(messages):
    response = client.chat.completions.create(
        model="deepseek-ai/DeepSeek-R1",
        messages=messages,
        stream=True
    )

    done_reasoning = False

    for chunk in response:
        delta = chunk.choices[0].delta
        if delta.reasoning_content:
            delta.content = delta.reasoning_content
        elif done_reasoning is False and delta.content:
            done_reasoning = True
            delta.content = "\n\n=== Final Answer ===\n\n" + delta.content
        yield chunk

st.title("😊AI助手 (ModelScope 推理API版)")

# 初始化消息列表
if "messages" not in st.session_state:
    st.session_state.messages = []

# 显示消息列表（应用启动时）
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 1.获取用户输入，并添加到消息列表中 2.复制用户输入作为助手回复
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