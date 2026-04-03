import streamlit as st
import google.generativeai as genai

# Configuração da página
st.set_page_config(page_title="Analista Pro IA", layout="centered")
st.title("⚽ 🎾 Analista Esportiva Inteligente")

# COLE SUA CHAVE ABAIXO ENTRE AS ASPAS
minha_chave = "SUA_CHAVE_AQUI"

genai.configure(api_key=minha_chave)
model = genai.GenerativeModel('gemini-1.5-flash')

if "messages" not in st.session_state:
    st.session_state.messages = []

# Exibe o histórico de conversa
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Entrada do usuário
if prompt := st.chat_input("Ex: Como está o jogo do Santos?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Resposta da IA
    try:
        response = model.generate_content(prompt)
        with st.chat_message("assistant"):
            st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
    except Exception as e:
        st.error(f"Erro na API: {e}")
