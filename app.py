import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Analista Pro IA", layout="centered")
st.title("⚽ 🎾 Analista Esportiva Inteligente")

# Sua chave
minha_chave = "AIzaSyDFmaFopymE7AOsAKe9kq9EHMUqzIvFkhU"
genai.configure(api_key=minha_chave)

# USANDO O MODELO GEMINI-PRO (MAIS ESTÁVEL PARA API v1)
try:
    model = genai.GenerativeModel('gemini-pro')
except Exception as e:
    st.error(f"Erro ao carregar o modelo: {e}")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Como posso ajudar na análise hoje?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    try:
        # Gerando a resposta de forma simples e direta
        response = model.generate_content(prompt)
        
        with st.chat_message("assistant"):
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
                
    except Exception as e:
        st.error(f"Erro na conexão: {e}")
        st.info("Dica: Se o erro 404 persistir, sua chave pode estar vinculada a uma região diferente ou versão legada da API.")
