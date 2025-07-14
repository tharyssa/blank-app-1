import streamlit as st

st.title("Minha Página Interativa")
st.header("Bem-vindo ao meu primeiro app!")

nome = st.text_input("Digite o nome para cadastro?")
idade = st.number_input("Quantos anos você tem?", min_value=1, max_value=120)
senha = st.text_input("Crie sua senha", type="password")

if st.button("Enviar"):
    st.write("Olá,", nome + "!")
    st.write("Você tem", idade, "anos.")
    st.write("Sua senha foi recebida com sucesso.")
    
rotina = st.checkbox("Você tem alguma rotina?")
organizacao = st.slider("Quanto você precisa se organizar?", 0, 10)

st.write("Obrigado por usar meu app.")