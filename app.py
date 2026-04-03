import streamlit as st
import google.generativeai as genai

# Configuração da página
st.set_page_config(page_title="Analista Pro IA", layout="centered")
st.title("⚽ 🎾 Analista Esportiva Inteligente")

# Sua chave já integrada
minha_chave = "AIzaSyDFmaFopymE7AOsAKe9kq9EHMUqzIvFkhU"

# Configuração revisada da API
genai.configure(api_key=minha_chave)

# Mudamos para uma chamada mais robusta do modelo
model = genai.GenerativeModel(model_name='gemini-1.5-flash')

if "messages" not in st.session_state:
    st.session_state.messages = []

# Exibe o histórico
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Entrada do usuário
if prompt := st.chat_input("Ex: Qual a expectativa de gols para o jogo do Santos hoje?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Resposta da IA
    try:
        # Instrução para focar em insights esportivos
        contexto = "Você é um assistente especialista em análise esportiva, foco em futebol e tênis. " + prompt
        response = model.generate_content(contexto)
        
        with st.chat_message("assistant"):
            st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
    except Exception as e:
        st.error(f"Erro na conexão: {e}")
        st.info("Dica: Se o erro persistir, tente atualizar a página do Streamlit.")
