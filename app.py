import streamlit as st
import google.generativeai as genai

# Configuração da página
st.set_page_config(page_title="Analista Pro IA", layout="centered")
st.title("⚽ 🎾 Analista Esportiva Inteligente")

# Sua chave
minha_chave = "AIzaSyDFmaFopymE7AOsAKe9kq9EHMUqzIvFkhU"

# Configuração da API
genai.configure(api_key=minha_chave)

# Tenta carregar o modelo de forma estável
try:
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error(f"Erro ao carregar o modelo: {e}")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Exibe o histórico
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Entrada do usuário
if prompt := st.chat_input("Como posso ajudar na análise hoje?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Resposta da IA
    try:
        # Forçamos a geração de conteúdo de forma simples
        response = model.generate_content(
            prompt,
            generation_config=genai.types.GenerationConfig(
                candidate_count=1,
                max_output_tokens=1000,
                temperature=0.7,
            ),
        )
        
        with st.chat_message("assistant"):
            if response.text:
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})
            else:
                st.warning("A IA não retornou texto. Tente reformular a pergunta.")
                
    except Exception as e:
        st.error(f"Erro na conexão: {e}")
