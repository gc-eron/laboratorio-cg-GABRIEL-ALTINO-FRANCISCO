import cv2
import numpy as np
import streamlit as st
from PIL import Image

st.title("Trabalho de Computação Gráfica")
st.write("Gabriel Altino Francisco")
st.divider()


foto = Image.open("imagens/image.png")
img = np.array(foto)                         
hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)   


st.header("1. Saturação")

col1, col2 = st.columns(2)
fator_sat = col1.slider("Fator de saturação", 0.0, 3.0, 1.0, step=0.05, key="sat")

s = hsv[:, :, 1].astype(float) * fator_sat
s = np.clip(s, 0, 255)

hsv_sat = hsv.copy()
hsv_sat[:, :, 1] = s.astype(np.uint8)
img_sat = cv2.cvtColor(hsv_sat, cv2.COLOR_HSV2RGB)

col1.image(img,     caption="Original",          use_container_width=True)
col2.image(img_sat, caption=f"Saturação × {fator_sat:.2f}", use_container_width=True)

st.divider()

st.header("2. Gerador de Padrão")

def ampliar(imagem, k=4):
    return imagem.repeat(k, axis=0).repeat(k, axis=1)

k_padrao = st.slider("k (parâmetro do padrão)", 1, 20, 12, key="padrao")
y, x = np.indices((64, 64))

padrao_cinza = (((x + y + k_padrao) * (y * k_padrao)) % 256).astype(np.uint8)

st.image(ampliar(padrao_cinza), caption="Padrão em cinza")

st.divider()

st.header("3. Canais RGB")

r = img[:, :, 0]
g = img[:, :, 1]
b = img[:, :, 2]

# Em tons de cinza

# Em cor
st.subheader("Canais em cor")
so_r = img.copy(); so_r[:, :, 1] = 0; so_r[:, :, 2] = 0
so_g = img.copy(); so_g[:, :, 0] = 0; so_g[:, :, 2] = 0
so_b = img.copy(); so_b[:, :, 0] = 0; so_b[:, :, 1] = 0

c1, c2, c3 = st.columns(3)
c1.image(so_r, caption="Só vermelho",  use_container_width=True)
c2.image(so_g, caption="Só verde",     use_container_width=True)
c3.image(so_b, caption="Só azul",      use_container_width=True)

st.subheader("Canais em tons de cinza")
c1, c2, c3 = st.columns(3)
c1.image(r, caption="Canal R", use_container_width=True)
c2.image(g, caption="Canal G", use_container_width=True)
c3.image(b, caption="Canal B", use_container_width=True)





st.divider()

st.header("4. Tons de Cinza")

rf = img[:, :, 0].astype(float)
gf = img[:, :, 1].astype(float)
bf = img[:, :, 2].astype(float)

cinza_media     = ((rf + gf + bf) / 3).astype(np.uint8)
cinza_ponderada = (0.299 * rf + 0.587 * gf + 0.114 * bf).astype(np.uint8)

col1, col2, col3 = st.columns(3)
col1.image(img,              caption="Original",                  use_container_width=True)
col2.image(cinza_media,      caption="Média simples (R+G+B)/3",   use_container_width=True)
col3.image(cinza_ponderada,  caption="Luminância ponderada",       use_container_width=True)

st.divider()


st.header("5. Brilho e Matiz no HSV")

col1, col2 = st.columns(2)

# Brilho (canal V)
fator_brilho = col1.slider("Brilho (fator × V)", 0.0, 3.0, 1.0, step=0.05, key="brilho")
v = hsv[:, :, 2].astype(float) * fator_brilho
v = np.clip(v, 0, 255)

hsv_brilho = hsv.copy()
hsv_brilho[:, :, 2] = v.astype(np.uint8)
img_brilho = cv2.cvtColor(hsv_brilho, cv2.COLOR_HSV2RGB)

col1.image(img,        caption="Original",                      use_container_width=True)
col1.image(img_brilho, caption=f"Brilho × {fator_brilho:.2f}", use_container_width=True)

giro = col2.slider("Giro do matiz (graus)", 0, 360, 0, step=1, key="matiz")
h = hsv[:, :, 0].astype(int)
h = (h + giro // 2) % 180

hsv_matiz = hsv.copy()
hsv_matiz[:, :, 0] = h.astype(np.uint8)
img_matiz = cv2.cvtColor(hsv_matiz, cv2.COLOR_HSV2RGB)

col2.image(img,       caption="Original",                   use_container_width=True)
col2.image(img_matiz, caption=f"Matiz girado em {giro}°",  use_container_width=True)
