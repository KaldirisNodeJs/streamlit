# titulo
# input do chat
# a cada mensagem enviada:
    # mostrar a mensagem que o usuario enviou no chat
    # enviar essa mensagem para a IA responder
    # aparece na tela a resposta da IA

# streamlit - frontend e backend

# RODAR:  streamlit run main.py

import streamlit as st
import time
from openai import OpenAI

with st.spinner(text='Carregando...'):
   time.sleep(1)
   # st.success('Pronto.')

key = st.secrets["OPEN_IA_KEY"]

modelo = OpenAI(api_key=key)

st.write("### KALDIRIS - ChatBot Versão 3.0") # markdown

# session_state = memoria do streamlit
if not "lista_mensagens" in st.session_state:
    st.session_state["lista_mensagens"] = []

# adicionar uma mensagem
# st.session_state["lista_mensagens"].append(mensagem)

# exibir o histórico de mensagens
for mensagem in st.session_state["lista_mensagens"]:
    role = mensagem["role"]
    content = mensagem["content"]
    st.chat_message(role).write(content)


mensagem_usuario = st.chat_input("Escreva sua mensagem aqui")


if mensagem_usuario:
    # user -> ser humano
    # assistant -> inteligencia artificial
    st.chat_message("user").write(mensagem_usuario)
    mensagem = {"role": "user", "content": mensagem_usuario}
    st.session_state["lista_mensagens"].append(mensagem)

    # resposta da IA
    resposta_modelo = modelo.chat.completions.create(
        messages=st.session_state["lista_mensagens"],
        model="gpt-3.5-turbo"
    )
    
    resposta_ia = resposta_modelo.choices[0].message.content

    # exibir a resposta da IA na tela  gffg
    st.chat_message("assistant").write(resposta_ia)
    mensagem_ia = {"role": "assistant", "content": resposta_ia}
    st.session_state["lista_mensagens"].append(mensagem_ia)


