import streamlit as st

st.title("Minha Página Interativa")
st.header("Bem-vindo ao meu primeiro app!")

nome = st.text_input("Qual é o seu nome?")
idade = st.number_input("Quantos anos você tem?", min_value=1, max_value=120)
senha = st.text_input("Digite sua senha", type="password")

if st.button("Enviar"):
    st.write("Olá,", nome + "!")
    st.write("Você tem", idade, "anos.")
    st.write("Sua senha foi recebida com sucesso.")
    
tecnologia = st.checkbox("Você gosta de tecnologia?")
nota_matematica = st.slider("Quanto você precisa se organizar", 0, 10)

st.write("Obrigado por usar meu app.")