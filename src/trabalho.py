import cv2
import numpy as np
import streamlit as st
from PIL import Image

st.title("Trabalho de Computação Gráfica")
foto = Image.open("imagens/foto.jpg")
img = np.array(foto)

st.header("1. Saturação")
col1, col2 = st.columns(2)
hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

col1.image(img, caption="img")

fator = st.slider("Saturação", 0.0, 2.0, 1.5)
s = hsv[:, :, 1].astype(float)
s = s * fator
s = np.clip(s, 0, 255)
hsv2 = hsv.copy()
hsv2[:, :, 1] = s
col2.image(cv2.cvtColor(hsv2, cv2.COLOR_HSV2RGB), caption="saturada")

st.header("2. Negativo")
col1, col2 = st.columns(2)

col1.image(img, caption="img")
nova = img.copy()
negativo = 255 - img
col2.image(negativo, caption="negativo")

st.header("3. Recorte")
col1, col2 = st.columns(2)
col1.image(img, caption="img")

altura, largura = img.shape[0], img.shape[1]
y = st.slider("y", 0, altura - 1, altura // 4)
x = st.slider("x", 0, largura - 1, largura // 4)
t = st.slider("tamanho", 10, largura, largura // 3)
recorte = img[y:y + t, x:x + t]
col2.image(recorte, caption="recorte")

st.header("4. Espelhamento")
col1, col2 = st.columns(2)

horizontal = img[:,::-1]
vertical = img[::-1,:]

col1.image(horizontal, caption="Espelhamento Horizontal")
col2.image(vertical, caption="Espelhamento Vertical")

st.header("5. Só uma cor")
col1, col2 = st.columns(2)

h_min, h_max = st.slider("Faixa de H", 0, 179, (140, 179))
mascara = cv2.inRange(hsv, (h_min, 60, 40), (h_max, 255, 255))
cinza = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
fundo = cv2.cvtColor(cinza, cv2.COLOR_GRAY2RGB)
resultado = fundo.copy()
dentro = mascara == 255
resultado[dentro] = img[dentro]
st.image(resultado)
