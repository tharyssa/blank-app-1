import streamlit as st

st.title("PRO life")
st.header("Folders")

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.image("saude1.png" , caption="Saúde")

with col2:
    st.image("progresso.png", caption="Progresso")

with col3:
    st.image("alimentacao.png", caption="Alimentação")

with col4:
    st.image("rotina.png", caption="Rotina")

middle, right = st.columns([2, 1], vertical_alignment="bottom")

middle.button("Crie sua rotina", use_container_width=True)

st.header("Minhas pastas")

col1, col2 = st.columns(2)
with col1:
    st.image("estudos.png", caption="Estudos")
with col2: 
    st.image("treinos.png", caption="Treinos")   

col1, col2 = st.columns(2)
with col1:
    st.image("rotina2.png", caption="Rotina")
with col2: 
    st.image("trabalho.png", caption="Trabalho")  

st.image("imagem.png")       
st.header("Seu progresso:")
st.image("progresso2.png")

