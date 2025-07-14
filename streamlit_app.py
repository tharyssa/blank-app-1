import streamlit as st

st.title("PRO life")
st.header("Folders")

st.image("saude1.png" , caption="Saúde")
st.image("progresso.png", caption="Progresso")
st.image("alimentacao.png", caption="Alimentação")
st.image("rotina.png", caption="Rotina")

if st.button(" crie sua nova rotina"):
    st.write("Você clicou no botão!")

st.header("Minhas pastas")    