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

if st.button(" crie sua nova rotina"):
    st.write("Você clicou no botão!")

st.markdown(":blue[o texto é azul]") 


left, middle, right = st.columns(3, vertical_alignment="bottom")

left.text_input("Write something")
middle.button("Click me", use_container_width=True)
right.checkbox("Check me")