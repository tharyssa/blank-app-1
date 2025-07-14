import streamlit as st

st.title("PRO life")
st.header("Folders")

st.image("/workspaces/blank-app-1/saude1.png" , caption="Saúde")
st.image("/workspaces/blank-app-1/progresso.png", caption="Progresso")
st.image("/workspaces/blank-app-1/alimentacao.png", caption="Alimentação")
st.image("/workspaces/blank-app-1/rotina.png", caption="Rotina")

if st.button(" crie sua nova rotina"):
    st.write("Você clicou no botão!")

st.header("Minhas pastas")    