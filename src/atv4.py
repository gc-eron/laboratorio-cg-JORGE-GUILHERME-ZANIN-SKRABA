import numpy as np
import streamlit as st
from PIL import Image

def ampliar(imagem, k=30):
    return imagem.repeat(k, axis=0).repeat(k, axis=1)

st.title("Atv 4: RGB")

# 1. Leitura da foto
st.header("1. Leitura da foto")
foto = Image.open("imagens/foto.jpg")

col1, col2 = st.columns(2)

img = np.array(foto)
col1.image(img)
col2.text(img.shape)

pixel = np.zeros((1,1,3), dtype=np.uint8)
pixel[0] = (40,73,56)
col1.image(ampliar(pixel))

col2.text("100, 100")
st.text(img[100,100])

# 2. Canais
st.header("2. Canais")
col1, col2 = st.columns(2)

col1.image(img[:, :, 0], caption="R")
# faça você: G e B na col1
so_r = img.copy()
so_r[:, :, 1] = 0
so_r[:, :, 2] = 0
col2.image(so_r, caption="só R")
# faça você: só G e só B na col2

col1.image(img[:, :, 1], caption="G")
# faça você: G e B na col1
so_r = img.copy()
so_r[:, :, 0] = 0
so_r[:, :, 2] = 0
col2.image(so_r, caption="só G")
# faça você: só G e só B na col2

col1.image(img[:, :, 2], caption="B")
# faça você: G e B na col1
so_r = img.copy()
so_r[:, :, 0] = 0
so_r[:, :, 1] = 0
col2.image(so_r, caption="só B")
# faça você: só G e só B na col2

# 3. Cubo e BGR
st.header("3. Cubo e BGR")
col1, col2 = st.columns(2)

col2 = st.image(img, channels="BGR")

quadrado = np.zeros((80, 80, 3), dtype=np.uint8)
quadrado[:, :] = (255, 255, 0)
col1.image(quadrado, caption="amarelo")

quadrado = np.zeros((80, 80, 3), dtype=np.uint8)
quadrado[:, :] = (255, 0, 255)
col1.image(quadrado, caption="magenta")

quadrado = np.zeros((80, 80, 3), dtype=np.uint8)
quadrado[:, :] = (0, 255, 255)
col1.image(quadrado, caption="ciano")

quadrado = np.zeros((80, 80, 3), dtype=np.uint8)
quadrado[:, :] = (0, 255, 0)
col1.image(quadrado, caption="verde")

# 4. Tons de cinza
st.header("4. Tons de cinza")
col1, col2 = st.columns(2)

r = img[:, :, 0].astype(float)
g = img[:, :, 1].astype(float)
b = img[:, :, 2].astype(float)
soma = r + g + b
media = (soma / 3).astype(np.uint8)
col1.image(media, caption="média")

soma = r*0.299 + g*0.587 + b*0.114
ponderada = (soma / 3).astype(np.uint8)
col2.image(ponderada, caption="ponderada")