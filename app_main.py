import pandas as pd
import numpy as np
import streamlit as st
import plotly.graph_objects as go
from app_functions import *

# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="ODA", page_icon=":eyes:", layout="wide")


df = get_data_vac( path_vac )
df_selection = set_feature( df )
introd()

menu = st.selectbox("Começar Análise Exploratória - Dados Campanha de Vacinação Contra COVID-19 em Florianópolis",
                        ("Bem-vindo!", "Como usar essa Ferramenta?",
                         "1 - Campanha de Vacinação",
                         "2 - Caracteristícas dos Vacinados"
                         ))


if menu == 'Bem-vindo!':
    bem_vindo()
elif menu == 'Como usar essa Ferramenta?':
    como_usar()
elif menu == '1 - Campanha de Vacinação':
    campanha1( df_selection )
elif menu == '2 - Caracteristícas dos Vacinados':
    caracteristicas2_blocoA( df_selection )
    caracteristicas2_blocoB(df_selection)