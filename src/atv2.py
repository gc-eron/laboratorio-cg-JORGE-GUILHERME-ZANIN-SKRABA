import numpy as np
import streamlit as st

def ampliar(imagem, k=30):
    return imagem.repeat(k, axis=0).repeat(k, axis=1)

st.title("Bandeira Breaking Bad")

bandeira = np.zeros((5,9,3), dtype=np.uint8)
bandeira[0] = (80, 150, 255) 
bandeira[1] = (255,205,205)
bandeira[2] = (255, 255, 255)
bandeira[3] = (255,205,205)
bandeira[4] = (80, 150, 255)

st.image(ampliar(bandeira))

st.write("Azul: Metanfetamina")
st.write("Rosa: Jesse Pinkman")
st.write("Branco: Walter White")