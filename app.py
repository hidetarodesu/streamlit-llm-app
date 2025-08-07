import streamlit as st

from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.5
    )


st.title("専門家呼び出しアプリ")
st.write("このアプリは、専門家の知識を活用して質問に答えることを目的としています。")
st.write("以下質問したい専門家を選択してください。")
selected_expert = st.radio("専門家を選択", ["料理の専門家", "旅行プランの専門家"])
st.divider()

st.write("以下に質問を入力してください。")
question = st.text_input("質問")

def expert_response(selected_expert, question):
    messages = [SystemMessage(content=f"あなたは{selected_expert}です。"),HumanMessage(content=question)]
    response = llm(messages)
    return response.content

if st.button("質問する"):
    result = expert_response(selected_expert, question)
    st.write(f"{selected_expert}の回答:", result)