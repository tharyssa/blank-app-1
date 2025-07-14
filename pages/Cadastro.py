import streamlit as st

st.title("Minha Página Interativa")
st.header("Bem-vindo ao meu primeiro app!")

nome = st.text_input("Qual é o seu nome?")
idade = st.number_input("Quantos anos você tem?", min_value=1, max_value=120)
cor = st.selectbox("Qual sua cor favorita?", ["Vermelho", "Verde", "Azul", "Amarelo"])

if st.button("Enviar"):
    st.write("Olá,", nome + "!")
    st.write("Você tem", idade, "anos.")
    st.write("Sua cor favorita é:", cor)
    
tecnologia = st.checkbox("Você gosta de tecnologia?")
nota_matematica = st.slider("Quanto você gosta de matemática?", 0, 10)

st.write("Obrigado por usar meu app.")