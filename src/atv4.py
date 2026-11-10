import numpy as np
import streamlit as st
from PIL import Image

st.title("Atv 4: RGB")

# 1. Leitura da foto
st.header("1. Leitura da foto")
col1, col2 = st.columns(2)

foto = Image.open("imagens/image.png")
img = np.array(foto)
col1.image(img)
col2.write(img.shape)
col2.write(img[100, 100])

# 2. Canais
st.header("2. Canais")
col1, col2 = st.columns(2)

# col1: cada canal em tons de cinza
col1.image(img[:, :, 0], caption="R")
col1.image(img[:, :, 1], caption="G")
col1.image(img[:, :, 2], caption="B")

# col2: cada canal em cor
so_r = img.copy()
so_r[:, :, 1] = 0
so_r[:, :, 2] = 0
col2.image(so_r, caption="só R")

so_g = img.copy()
so_g[:, :, 0] = 0
so_g[:, :, 2] = 0
col2.image(so_g, caption="só G")

so_b = img.copy()
so_b[:, :, 0] = 0
so_b[:, :, 1] = 0
col2.image(so_b, caption="só B")

# 3. Cubo e BGR
st.header("3. Cubo e BGR")
col1, col2 = st.columns(2)

# col1: quatro vértices do cubo
quadrado = np.zeros((80, 80, 3), dtype=np.uint8)
col1.text(quadrado[0, 0])
quadrado[:, :] = (255, 255, 0)
col1.text(quadrado[0, 0])
col1.image(quadrado, caption="amarelo")

for cor, nome in [((0, 255, 255), "ciano"),
                  ((255, 0, 255), "magenta"),
                  ((255, 255, 255), "branco")]:
    quadrado = np.zeros((80, 80, 3), dtype=np.uint8)
    quadrado[:, :] = cor
    col1.image(quadrado, caption=nome)

# col2: a foto exibida como BGR
col2.image(img, channels="BGR", caption="foto como BGR")

# 4. Tons de cinza
st.header("4. Tons de cinza")
col1, col2 = st.columns(2)

r = img[:, :, 0].astype(float)
g = img[:, :, 1].astype(float)
b = img[:, :, 2].astype(float)

#média
soma = r + g + b
media = (soma / 3).astype(np.uint8)
col1.image(media, caption="média")

#média ponderada
ponderada = (0.299 * r + 0.587 * g + 0.114 * b).astype(np.uint8)
col2.image(ponderada, caption="ponderada")