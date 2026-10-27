import numpy as np
import streamlit as st

def ampliar(imagem, k=30):
    return imagem.repeat(k, axis=0).repeat(k, axis=1)

st.title("Bandeira de Londrina")

bandeira = np.zeros((15, 21, 3), dtype=np.uint8)
bandeira[:] = (200, 16, 46)

bandeira[2:5, 10] = (235, 235, 235)
bandeira[3, 9:12] = (235, 235, 235)

bandeira[10:13, 10] = (235, 235, 235)
bandeira[11, 9:12] = (235, 235, 235)

bandeira[6:9, 6] = (235, 235, 235)
bandeira[7, 5:8] = (235, 235, 235)

bandeira[6:9, 14] = (235, 235, 235)
bandeira[7, 13:16] = (235, 235, 235)

st.image(ampliar(bandeira))