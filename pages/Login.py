import streamlit as st

st.title("Login")
st.header("Bem-vindo")

nome = st.text_input("Digite seu nome ")
senha = st.text_input("Crie sua senha", type="password")

if st.button("Enviar"):
    st.write("Olá,", nome + "!")
    st.write("Sua senha foi recebida com sucesso.")
    

st.write("Obrigado por usar meu app.")