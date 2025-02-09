import streamlit as st

st.title("AI 助手 (Mirror) 😊")

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

    response = f"Mirror：{prompt}"
    # 打印助手回复
    with st.chat_message("assistant"):
        st.markdown(response)
    # 将助手回复添加到消息列表中
    st.session_state.messages.append({"role": "assistant", "content": response})