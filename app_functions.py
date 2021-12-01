#bibliotecas:
import pandas as pd
import numpy as np
import streamlit as st
import plotly.graph_objects as go
from app_variables import *



@st.cache(allow_output_mutation=True)
def get_data_vac( path_vac ):
    df = pd.read_csv( path_vac, sep=",", encoding="ISO-8859-1" )
    return df

def set_feature( df ):
    df['1° Dose']        = np.where(df['nova_dose'] == '1 Dose', 1, 0)
    df['2° Dose']        = np.where(df['nova_dose'] == '2 Dose', 1, 0)
    df['Dose Única']     = np.where(df['nova_dose'] == 'Dose Unica', 1, 0)
    df['Dose Adicional'] = np.where(df['nova_dose'] == 'Dose Adicional', 1, 0)

    df['AstraZeneca'] = np.where(df['vacina_nome'] == 'AstraZeneca', 1, 0)
    df['Pfizer']      = np.where(df['vacina_nome'] == 'Pfizer', 1, 0)
    df['Coronavac']   = np.where(df['vacina_nome'] == 'Coronavac', 1, 0)
    df['Janssen']     = np.where(df['vacina_nome'] == 'Janssen', 1, 0)

    df['Feminino']  = np.where(df['paciente_enumsexobiologico'] == 'Feminino', 1, 0)
    df['Masculino'] = np.where(df['paciente_enumsexobiologico'] == 'Masculino', 1, 0)

    df['BRANCA']         = np.where(df['paciente_racacor_valor'] == 'BRANCA', 1, 0)
    df['PRETA']          = np.where(df['paciente_racacor_valor'] == 'PRETA', 1, 0)
    df['PARDA']          = np.where(df['paciente_racacor_valor'] == 'PARDA', 1, 0)
    df['AMARELA']        = np.where(df['paciente_racacor_valor'] == 'AMARELA', 1, 0)
    df['INDIGENA']       = np.where(df['paciente_racacor_valor'] == 'INDIGENA', 1, 0)
    df['SEM INFORMACAO'] = np.where(df['paciente_racacor_valor'] == 'SEM INFORMACAO', 1, 0)

    df["Total Doses"] = df["1° Dose"] + df["2° Dose"] + df["Dose Única"] + df["Dose Adicional"]

    df_selection = df

    return df_selection

def introd():
    st.markdown('<style>body{background-color: #fbfff0}</style>', unsafe_allow_html=True)
    st.markdown(html_title, unsafe_allow_html=True)
    st.markdown(""" <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        </style> """, unsafe_allow_html=True)
    col1, col2, col3, col4, col5 = st.columns([1, 20, 1, 20, 1])
    with col1:
        st.write("")
    with col2:
        st.markdown(html_card_header_0A1, unsafe_allow_html=True)
        st.markdown(html_card_body_0A1, unsafe_allow_html=True)
    with col3:
        st.write("")
    with col4:
        st.markdown(html_card_header_0A2, unsafe_allow_html=True)
        st.markdown('<style>body{background-color: ##F5F5F5}</style>', unsafe_allow_html=True)
        st.markdown("""[Código Aberto no Github](https://github.com/MateusOF5512/TesteHeroku)""")
        st.markdown(
                """[Dados sobre o CENSO IBGE 2010](https://cidades.ibge.gov.br/brasil/sc/florianopolis/pesquisa/23/24304?indicador=29455)""")
        st.markdown(
                """[Dados sobre a Campanha de Vacinação Contra Covid-19](https://opendatasus.saude.gov.br/dataset/covid-19-vacinacao)""")
    with col5:
        st.write("")

    return None

def bem_vindo():
    return None


def como_usar():
    return None

def campanha1( df_selection ):
    st.markdown("""---""")
    st.markdown(html_header_01, unsafe_allow_html=True)
    st.markdown("""---""")
    st.markdown(html_subheader_11, unsafe_allow_html=True)
    st.markdown("""###""")

    # DECLARAÇÂO DE VARIAVEIS GERAIS - 1.1A -
    popul_residente = int(516524)
    imun_rebanho = int(387393)
    vacinados_1dose = int(df_selection['1° Dose'].sum())
    vacinados_completo = int(df_selection['2° Dose'].sum() + df_selection['Dose Única'].sum())

    pop_sem_1dose = (popul_residente - vacinados_1dose)
    pop_sem_2dose = (popul_residente - vacinados_completo)

    with st.container():
        col1A, col2A, col3A, col4A, col5A, col6A, col7A, col8A, col9A = st.columns([1, 15, 1, 15, 1, 15, 1, 15, 1])
        with col1A:
            st.write("")
        with col2A:
            st.markdown(html_card_header_1A1, unsafe_allow_html=True)
            # DECLARAÇÂO DE VARIAVEIS - 1.1B - Vacinados com 1° Dose: ---------------------------------------
            labels2 = ['População com 1° Dose', "População sem 1° Dose:"]
            colors2 = ['#4169E1', 'gray']
            # PLOTAGEM GRÀFICO DE PIZZA - 1.1B: --------------------------------------------------------------
            fig1 = go.Figure(data=[go.Pie(labels=labels2,
                                          values=[vacinados_1dose, pop_sem_1dose],
                                          textinfo='percent',
                                          showlegend=False,
                                          marker=dict(colors=colors2,
                                                      line=dict(color='#000010', width=2)))])
            fig1.update_traces(hole=.4, hoverinfo="label+percent+value")
            fig1.update_layout(autosize=False,
                               width=275, height=150, margin=dict(l=20, r=20, b=20, t=30),
                               paper_bgcolor="#F8F8FF", font={'size': 20})
            st.plotly_chart(fig1)
        with col3A:
            st.write("")
        with col4A:
            st.markdown(html_card_header_1A2, unsafe_allow_html=True)
            fig2 = go.Figure()
            fig2.add_trace(go.Indicator(
                mode="gauge+number+delta",
                value=vacinados_1dose,
                domain={'x': [0, 1], 'y': [0, 1]},
                delta={'reference': imun_rebanho, 'increasing': {'color': "Purple"}},
                gauge={
                    'axis': {'range': [0, 520000], 'tickwidth': 2, 'tickcolor': "#4169E1"},
                    'bordercolor': "#4169E1",
                    'bar': {'color': "#4169E1"},
                    'bgcolor': "lightgray",
                    'borderwidth': 2,
                    'steps': [
                        {'range': [0, imun_rebanho], 'color': "#ADD8E6"}],
                    'threshold': {
                        'line': {'color': "red", 'width': 4},
                        'thickness': 0.75,
                        'value': imun_rebanho}}))
            fig2.update_layout(autosize=False,
                               width=275, height=150, margin=dict(l=20, r=20, b=20, t=30),
                               paper_bgcolor="#F8F8FF", font={'size': 20})
            st.plotly_chart(fig2)
        with col5A:
            st.write("")
        with col6A:
            st.markdown(html_card_header_1A3, unsafe_allow_html=True)
            fig3 = go.Figure()
            fig3.add_trace(go.Indicator(
                mode="gauge+number+delta",
                value=vacinados_completo,
                domain={'x': [0, 1], 'y': [0, 1]},
                delta={'reference': imun_rebanho, 'increasing': {'color': "Purple"}},
                gauge={
                    'axis': {'range': [0, 520000], 'tickwidth': 2, 'tickcolor': "#D70270"},
                    'bordercolor': "#D70270",
                    'bar': {'color': "#D70270"},
                    'bgcolor': "lightgray",
                    'borderwidth': 2,
                    'steps': [
                        {'range': [0, imun_rebanho], 'color': "#FFC0CB"}],
                    'threshold': {
                        'line': {'color': "red", 'width': 4},
                        'thickness': 0.7,
                        'value': imun_rebanho}}))
            fig3.update_layout(autosize=False,
                               width=275, height=150, margin=dict(l=20, r=20, b=20, t=30),
                               paper_bgcolor="#F8F8FF", font={'size': 20})
            st.plotly_chart(fig3)
        with col7A:
            st.write("")
        with col8A:
            st.markdown(html_card_header_1A4, unsafe_allow_html=True)
            # DECLARAÇÂO DE VARIAVEIS - 1.1D - Vacinados Completamente: ---------------------------------------
            labels3 = ['Vacinados Completamente', 'Vacinados Incompletamente']
            colors3 = ['#D70270', 'gray']

            # PLOTAGEM GRÀFICO DE PIZZA - 1.1D: ---------------------------------------------------------------
            fig4 = go.Figure(data=[go.Pie(labels=labels3,
                                          values=[vacinados_completo, pop_sem_2dose],
                                          textinfo='percent', textfont_size=20,
                                          showlegend=False,
                                          marker=dict(colors=colors3,
                                                      line=dict(color=' #000010', width=2)))])
            fig4.update_traces(hole=.4, hoverinfo="label+percent+value")
            fig4.update_layout(autosize=False,
                               width=275, height=150, margin=dict(l=20, r=20, b=20, t=30),
                               paper_bgcolor="#F8F8FF", font={'size': 20})
            st.plotly_chart(fig4)
        with col9A:
            st.write("")

    with st.container():
        col1B, col2B, col3B, col4B, col5B = st.columns([1, 20, 1, 20, 1, ])
        with col1B:
            st.write("")
        with col2B:
            st.markdown(html_card_header_1B11, unsafe_allow_html=True)
            df1 = df_selection[["nova_dose", "AstraZeneca", "Pfizer", "Coronavac", "Janssen"]]
            df = df1.groupby(['nova_dose']).sum().reset_index()

            values = ['1° Dose', '2° Dose', 'Dose Única', 'Dose Adicional']
            y_Pfizer = [df['Pfizer'][0], df['Pfizer'][1], df['Pfizer'][3], df['Pfizer'][2]]
            y_AstraZeneca = [df['AstraZeneca'][0], df['AstraZeneca'][1], df['AstraZeneca'][3], df['AstraZeneca'][2]]
            y_Coronavac = [df['Coronavac'][0], df['Coronavac'][1], df['Coronavac'][3], df['Coronavac'][2]]
            y_Janssen = [df['Janssen'][0], df['Janssen'][1], df['Janssen'][3], df['Janssen'][2]]

            # 1.3A - Vacinas Aplicadas por Dose - PLOTAGEM GRÀFICO DE BARRA -----------------------------------------
            fig1 = go.Figure()
            fig1.add_trace(go.Bar(name='AstraZeneca', x=values, y=y_AstraZeneca,
                                  text=y_AstraZeneca, textposition='auto',
                                  marker_color=['#D70270', '#D70270', '#D70270', '#D70270', '#D70270']))  # magenta
            fig1.add_trace(go.Bar(name='Pfizer', x=values, y=y_Pfizer,
                                  text=y_Pfizer, textposition='auto',
                                  marker_color=['#4169E1', '#4169E1', '#4169E1', '#4169E1', '#4169E1']))  # royalazul
            fig1.add_trace(go.Bar(name='Coronavac', x=values, y=y_Coronavac,
                                  text=y_Coronavac, textposition='auto',
                                  marker_color=['#8A2BE2', '#8A2BE2', '#8A2BE2', '#8A2BE2', '#8A2BE2']))  # Purple
            fig1.add_trace(go.Bar(name='Janssen', x=values, y=y_Janssen,
                                  text=y_Janssen, textposition='auto',
                                  marker_color=['#00FFFF', '#00FFFF', '#00FFFF', '#00FFFF', '#00FFFF']))
            fig1.update_layout(legend_font_size=12,
                               barmode='stack',
                               paper_bgcolor="#F8F8FF", plot_bgcolor="#F8F8FF",
                               font={'color': "#4169E1", 'family': "sans-serif"}, height=175, width=550,
                               margin=dict(l=2, r=2, b=4, t=4),
                               legend=dict(orientation="v",
                                           yanchor="top",
                                           y=0.99,
                                           xanchor="right",
                                           x=0.99))
            fig1.update_xaxes(
                title_text='Doses Aplicadas',
                title_font=dict(family='Sans-serif', size=12),
                tickfont=dict(family='Sans-serif', size=9))
            fig1.update_yaxes(
                title_text="Número de Vacinados",
                title_font=dict(family='Sans-serif', size=12),
                tickfont=dict(family='Sans-serif', size=9),
                nticks=7, showgrid=True, gridwidth=0.5, gridcolor='#D3D3D3')
            st.plotly_chart(fig1)

            st.markdown(html_card_header_1B12, unsafe_allow_html=True)
            # PREPARAÇÂO DOS DADOS - 1.3B - Vacinas Aplicadas por Dose: -------------------------------------
            y_Pfizer = int(df_selection['Pfizer'].sum())
            y_Coronavac = int(df_selection['Coronavac'].sum())
            y_Janssen = int(df_selection['Janssen'].sum())
            y_AstraZeneca = int(df_selection['AstraZeneca'].sum())

            values = ["AstraZeneca", "Pfizer", "Coronavac", "Janssen", ]
            y = [y_AstraZeneca, y_Pfizer, y_Coronavac, y_Janssen, ]

            # ------------------- PLOTAGEM GRÀFICO DE BARRA - 1.3B - Proporção das Vacinas Aplicadas:
            fig2 = go.Figure()
            fig2.add_trace(go.Funnel(
                y=values, x=y,
                textposition="inside",
                textinfo="value+percent total",
                opacity=1, marker={"color": ["#D70270", "#4169E1", "#8A2BE2", "#00FFFF", "#ADFF2F"],
                                   "line": {"width": [2, 2, 2, 2, 2, 2],
                                            "color": ["black", "black", "black", "black", "black"]}},
                connector={"line": {"color": "black", "dash": "solid", "width": 2}}))
            fig2.update_layout(paper_bgcolor="#F8F8FF", plot_bgcolor="#F8F8FF",
                               font={'color': "#4169E1", 'family': "sans-serif"}, height=175, width=550,
                               margin=dict(l=2, r=2, b=4, t=4))
            st.plotly_chart(fig2)
    with col3B:
        st.write("")
    with col4B:
        st.markdown(html_card_header_1B2, unsafe_allow_html=True)
        df_new = df_selection.groupby(['paciente_id']).sum().reset_index()

        conditions = [
            (df_new['1° Dose'] >= 1) & (df_new['2° Dose'] == 0),
            (df_new['1° Dose'] >= 1) & (df_new['2° Dose'] >= 1),
            (df_new['Dose Única'] >= 1)]
        values = ['Incompleta', 'Completa', 'Completa']
        df_new['Imunizacao'] = np.select(conditions, values)

        df_new = df_new[["paciente_id", "Total Doses",
                         "1° Dose", "2° Dose", "Dose Única", "Dose Adicional", "Imunizacao",
                         "AstraZeneca", "Pfizer", "Coronavac", "Janssen",
                         ]]
        df_new.columns = ["Identificador Paciente", "Total Doses",
                          "1° Dose", "2° Dose", "Dose Única", "Dose Adicional", "Imunização",
                          "AstraZeneca", "Pfizer", "Coronavac", "Janssen",
                          ]
        st.dataframe(data=df_new, width=550, height=400)

    with col5B:
        st.write("")

    st.markdown("""---""")
    st.markdown(html_subheader_12, unsafe_allow_html=True)
    st.markdown("""###""")

    row_spacer1, row_1, row_spacer2 = st.columns([1, 10, 1])
    with row_1:
        st.markdown("")
        see_data = st.expander('Filtro Avançado')
        with see_data:
            intervalo = st.radio(label="Selecione o Tipo de Intervalo",
                                 options=('Dia', "Mês"))
            tipo_vizu = st.radio(label="Selecione o Tipo de Vizualização",
                                 options=('Gráfico de Linha', "Gráfico de Área"))
    # ---------------------------------------------------------------------------------
    with st.container():
        col1B, col2B, col3B, col4B, col5B = st.columns([1, 20, 1, 20, 1, ])
        with col1B:
            st.write("")
        with col2B:
            if intervalo == 'Dia':
                df_area = df_selection.groupby(['vacina_dataaplicacao']).sum().reset_index()

                # 1.2B - Variação Diária da Aplicação das Doses - PLOTAGEM GRÀFICO DE AREA --------------------------------
                fig2 = go.Figure()
                fig2.add_trace(go.Scatter(
                    x=df_area['vacina_dataaplicacao'],
                    y=df_area['1° Dose'],
                    name='1° Dose',
                    mode='lines',
                    line=dict(width=1, color='#4169E1'),
                    stackgroup='one'))
                fig2.add_trace(go.Scatter(
                    x=df_area['vacina_dataaplicacao'],
                    y=df_area['2° Dose'],
                    name='2° Dose',
                    mode='lines',
                    line=dict(width=1, color='#D70270'),
                    stackgroup='two'))
                fig2.add_trace(go.Scatter(
                    x=df_area['vacina_dataaplicacao'],
                    y=df_area['Dose Única'],
                    name='Dose Única',
                    mode='lines',
                    line=dict(width=1, color='#00FFFF'),
                    stackgroup='three'))
                fig2.add_trace(go.Scatter(
                    x=df_area['vacina_dataaplicacao'],
                    y=df_area['Dose Adicional'],
                    name='Dose Adicional',
                    mode='lines',
                    line=dict(width=1, color='#8A2BE2'),
                    stackgroup='four'))
                fig2.update_layout(legend_font_size=10,
                                   paper_bgcolor="#F8F8FF", plot_bgcolor="#F8F8FF",
                                   font={'color': "#4169E1", 'family': "sans-serif"}, height=250, width=550,
                                   margin=dict(l=2, r=2, b=4, t=4),
                                   legend=dict(orientation="v",
                                               yanchor="top",
                                               y=0.99,
                                               xanchor="left",
                                               x=0.05))
                fig2.update_xaxes(
                    title_text='Dias da Aplicação da Vacina',
                    title_font=dict(family='Sans-serif', size=12),
                    tickfont=dict(family='Sans-serif', size=9),
                    rangeslider_visible=True)
                fig2.update_yaxes(
                    title_text="Número de Vacinados",
                    title_font=dict(family='Sans-serif', size=12),
                    tickfont=dict(family='Sans-serif', size=9),
                    nticks=7, showgrid=True, gridwidth=0.5, gridcolor='#D3D3D3')

                st.markdown(html_card_header_1C11, unsafe_allow_html=True)
                st.plotly_chart(fig2)

                # PREPARAÇÂO DOS DADOS - 1.4A - Variação Mensal da Aplicação da Vacinas: --------------------------
                df_area = df_selection.groupby(['vacina_dataaplicacao']).sum().reset_index()

                # PLOTAGEM GRÀFICO DE BARRA - 1.4A - Variação Mensal da Aplicação da Vacinas: ----------------------
                fig2 = go.Figure()
                fig2.add_trace(go.Scatter(
                    x=df_area['vacina_dataaplicacao'],
                    y=df_area['AstraZeneca'],
                    name='AstraZeneca',
                    mode='lines',
                    line=dict(width=1, color='#D70270'),
                    stackgroup='one'))
                fig2.add_trace(go.Scatter(
                    x=df_area['vacina_dataaplicacao'],
                    y=df_area['Pfizer'],
                    name='Pfizer',
                    mode='lines',
                    line=dict(width=1, color='#4169E1'),
                    stackgroup='two'))
                fig2.add_trace(go.Scatter(
                    x=df_area['vacina_dataaplicacao'],
                    y=df_area['Coronavac'],
                    name='Coronavac',
                    mode='lines',
                    line=dict(width=1, color='#8A2BE2'),
                    stackgroup='four'))
                fig2.add_trace(go.Scatter(
                    x=df_area['vacina_dataaplicacao'],
                    y=df_area['Janssen'],
                    name='Janssen',
                    mode='lines',
                    line=dict(width=1, color='#00FFFF'),
                    stackgroup='five'))
                fig2.update_layout(legend_font_size=10,
                                   paper_bgcolor="#F8F8FF", plot_bgcolor="#F8F8FF",
                                   font={'color': "#4169E1", 'family': "sans-serif"}, height=250, width=550,
                                   margin=dict(l=2, r=2, b=4, t=4),
                                   legend=dict(orientation="v",
                                               yanchor="top",
                                               y=0.99,
                                               xanchor="left",
                                               x=0.05))
                fig2.update_xaxes(
                    title_text='Dia da Aplicação da Vacina',
                    title_font=dict(family='Sans-serif', size=12),
                    tickfont=dict(family='Sans-serif', size=9),
                    rangeslider_visible=True)
                fig2.update_yaxes(
                    title_text="Número de Vacinados",
                    title_font=dict(family='Sans-serif', size=12),
                    tickfont=dict(family='Sans-serif', size=9),
                    nticks=7, showgrid=True, gridwidth=0.5, gridcolor='#D3D3D3')

                st.markdown(html_card_header_1C12, unsafe_allow_html=True)
                st.plotly_chart(fig2)

            else:
                df_line = df_selection.groupby(['meses_aplicacao']).sum().reset_index()

                # ------------------- PLOTAGEM GRÀFICO DE LINHA - 1.2A:
                fig1 = go.Figure()
                fig1.add_trace(go.Scatter(
                    x=df_line['meses_aplicacao'],
                    y=df_line['1° Dose'],
                    name='1° Dose',
                    mode='lines',
                    line=dict(width=2, color='#D70270'),
                    stackgroup='one'))
                fig1.add_trace(go.Scatter(
                    x=df_line['meses_aplicacao'],
                    y=df_line['2° Dose'],
                    name='2° Dose',
                    mode='lines',
                    line=dict(width=2, color='#4169E1'),
                    stackgroup='two'))
                fig1.add_trace(go.Scatter(
                    x=df_line['meses_aplicacao'],
                    y=df_line['Dose Única'],
                    name='Dose Única',
                    mode='lines',
                    line=dict(width=2, color='#00FFFF'),
                    stackgroup='five'))
                fig1.add_trace(go.Scatter(
                    x=df_line['meses_aplicacao'],
                    y=df_line['Dose Adicional'],
                    name='Dose Adicional',
                    mode='lines',
                    line=dict(width=2, color='#8A2BE2'),
                    stackgroup='four'))
                fig1.update_layout(legend_font_size=10,
                                   paper_bgcolor="#F8F8FF", plot_bgcolor="#F8F8FF",
                                   font={'color': "#4169E1", 'family': "sans-serif"}, height=250, width=550,
                                   margin=dict(l=2, r=2, b=4, t=4),
                                   legend=dict(orientation="h",
                                               yanchor="top",
                                               y=0.99,
                                               xanchor="left",
                                               x=0.05))
                fig1.update_xaxes(
                    title_text='Mês da Aplicação da Vacina',
                    title_font=dict(size=12, family='Sans-serif'),
                    tickfont=dict(size=9, family='Sans-serif'),
                    rangeslider_visible=True)
                fig1.update_yaxes(
                    title_text="Número de Vacinados",
                    title_font=dict(size=12, family='Sans-serif'),
                    tickfont=dict(size=9, family='Sans-serif'),
                    nticks=7, showgrid=True, gridwidth=0.5, gridcolor='#D3D3D3')

                st.markdown(html_card_header_1C11, unsafe_allow_html=True)
                st.plotly_chart(fig1)

                df_area = df_selection.groupby(['meses_aplicacao']).sum().reset_index()

                # PLOTAGEM GRÀFICO DE BARRA - 1.4A - Variação Mensal da Aplicação da Vacinas: ------------------------
                fig1 = go.Figure()
                fig1.add_trace(go.Scatter(
                    x=df_area['meses_aplicacao'],
                    y=df_area['AstraZeneca'],
                    name='AstraZeneca',
                    mode='lines',
                    line=dict(width=2, color='#D70270'),
                    stackgroup='one'))
                fig1.add_trace(go.Scatter(
                    x=df_area['meses_aplicacao'],
                    y=df_area['Pfizer'],
                    name='Pfizer',
                    mode='lines',
                    line=dict(width=2, color="#4169E1"),
                    stackgroup='two'))
                fig1.add_trace(go.Scatter(
                    x=df_area['meses_aplicacao'],
                    y=df_area['Coronavac'],
                    name='Coronavac',
                    mode='lines',
                    line=dict(width=2, color='#8A2BE2'),
                    stackgroup='three'))
                fig1.add_trace(go.Scatter(
                    x=df_area['meses_aplicacao'],
                    y=df_area['Janssen'],
                    name='Janssen',
                    mode='lines',
                    line=dict(width=4, color='#00FFFF'),
                    stackgroup='four'))
                fig1.update_layout(legend_font_size=10,
                                   paper_bgcolor="#F8F8FF", plot_bgcolor="#F8F8FF",
                                   font={'color': "#4169E1", 'family': "sans-serif"}, height=250, width=550,
                                   margin=dict(l=2, r=2, b=4, t=4),
                                   legend=dict(orientation="h",
                                               yanchor="top",
                                               y=0.99,
                                               xanchor="left",
                                               x=0.05))
                fig1.update_xaxes(
                    title_text='Mês da Aplicação da Vacina',
                    title_font=dict(family='Sans-serif', size=12),
                    tickfont=dict(family='Sans-serif', size=9),
                    rangeslider_visible=True)
                fig1.update_yaxes(
                    title_text="Número de Vacinados",
                    title_font=dict(family='Sans-serif', size=12),
                    tickfont=dict(family='Sans-serif', size=9),
                    nticks=7, showgrid=True, gridwidth=0.5, gridcolor='#D3D3D3')

                st.markdown(html_card_header_1C12, unsafe_allow_html=True)
                st.plotly_chart(fig1)
        with col3B:
            st.write("")
        with col4B:
            if intervalo == 'Dia':
                st.markdown(html_card_header_1C20, unsafe_allow_html=True)
                df_filter1 = df_selection[["vacina_dataaplicacao", "Total Doses",
                                           "1° Dose", "2° Dose", "Dose Única", "Dose Adicional",
                                           "AstraZeneca", "Pfizer", "Coronavac", "Janssen"]]
                df_new1 = df_filter1.groupby('vacina_dataaplicacao').sum().reset_index()
                st.dataframe(data=df_new1, width=550, height=520)

            else:
                st.markdown(html_card_header_1C20, unsafe_allow_html=True)
                df_filter2 = df_selection[["meses_aplicacao", "Total Doses",
                                           "1° Dose", "2° Dose", "Dose Única", "Dose Adicional",
                                           "AstraZeneca", "Pfizer", "Coronavac", "Janssen"]]
                df_new2 = df_filter2.groupby('meses_aplicacao').sum().reset_index()
                st.dataframe(data=df_new2, width=550, height=520)
        with col5B:
            st.write("")

    return None

def caracteristicas2_blocoA( df_selection ):
    st.markdown("""---""")
    st.markdown(html_header_20, unsafe_allow_html=True)
    st.markdown("""---""")
    st.markdown(html_subheader_2A_10, unsafe_allow_html=True)
    st.markdown("""###""")

    with st.container():
        col1A, col2A, col3A, col4A, col5A, col6A, col7A = st.columns([1, 15, 1, 15, 1, 15, 1])
        with col1A:
            st.write("")
        with col2A:
            st.markdown(html_card_header_2A_1_11, unsafe_allow_html=True)
            df_selection1 = df_selection.drop_duplicates(subset=['paciente_id'], keep="last")

            popul_femi = int(268592)
            rebanho_femi = int(201444)
            popul_masc = int(247931)
            rebanho_masc = int(185948)
            vacinados_femi = int(df_selection1['Feminino'].sum())
            vacinados_masc = int(df_selection1['Masculino'].sum())

            # --------------------------------------------------------------------------------------
            fig3 = go.Figure()
            fig3.add_trace(go.Indicator(
                mode="gauge+number+delta",
                value=vacinados_masc,
                domain={'x': [0, 1], 'y': [0, 1]},
                delta={'reference': rebanho_masc, 'increasing': {'color': "Purple"}},
                gauge={
                    'axis': {'range': [0, popul_masc], 'tickwidth': 2, 'tickcolor': "#4169E1"},
                    'bordercolor': "#4169E1",
                    'bar': {'color': "#4169E1"},
                    'bgcolor': "lightgray",
                    'borderwidth': 2,
                    'steps': [
                        {'range': [0, rebanho_masc], 'color': "#ADD8E6"}],
                    'threshold': {
                        'line': {'color': "red", 'width': 4},
                        'thickness': 0.7,
                        'value': rebanho_masc}}))
            fig3.update_layout(autosize=False,
                               width=350, height=150, margin=dict(l=20, r=20, b=20, t=30),
                               paper_bgcolor="#F8F8FF", font={'size': 20})
            st.plotly_chart(fig3, use_container_width=True)

        with col3A:
            st.write("")

        with col4A:
            st.markdown(html_card_header_2A_1_12, unsafe_allow_html=True)
            labels1 = ['Sexo Feminino', 'Sexo Masculino']
            colors1 = ['#D70270', '#4169E1']  # magenta | royalblue

            # PLOTAGEM GRÀFICO DE PIZZA - 2.1A - Proporção entre os Sexos: --------------------------------------------------------------
            fig2 = go.Figure(data=[go.Pie(labels=labels1,
                                          values=[vacinados_femi, vacinados_masc],
                                          textinfo='percent', textfont_size=20,
                                          showlegend=False,
                                          marker=dict(colors=colors1,
                                                      line=dict(color='black', width=3)))])
            fig2.update_traces(hole=.4, hoverinfo="label+percent+value")
            fig2.update_layout(autosize=False,
                               width=350, height=150, margin=dict(l=20, r=20, b=20, t=30),
                               paper_bgcolor="#F8F8FF", font={'size': 20})
            st.plotly_chart(fig2, use_container_width=True)

        with col5A:
            st.write("")
        with col6A:
            st.markdown(html_card_header_2A_1_13, unsafe_allow_html=True)
            fig1 = go.Figure()
            fig1.add_trace(go.Indicator(
                mode="gauge+number+delta",
                value=vacinados_femi,
                domain={'x': [0, 1], 'y': [0, 1]},
                delta={'reference': rebanho_femi, 'increasing': {'color': "Purple"}},
                gauge={
                    'axis': {'range': [0, popul_femi], 'tickwidth': 2, 'tickcolor': "#D70270"},
                    'bordercolor': "#D70270",
                    'bar': {'color': "#D70270"},
                    'bgcolor': "lightgray",
                    'borderwidth': 2,
                    'steps': [
                        {'range': [0, rebanho_femi], 'color': "#FFC0CB"}],
                    'threshold': {
                        'line': {'color': "red", 'width': 4},
                        'thickness': 0.7,
                        'value': rebanho_femi}}))
            fig1.update_layout(autosize=False,
                               width=350, height=150, margin=dict(l=20, r=20, b=20, t=30),
                               paper_bgcolor="#F8F8FF", font={'size': 20})
            st.plotly_chart(fig1, use_container_width=True)

        with col7A:
            st.write("")

#--------------------------- BLOCO 2A-2 --------------------------------------------------------------
    with st.container():
        col1B, col2B, col3B = st.columns([1, 25, 1])
        with col1B:
            st.write("")
        with col2B:
            st.markdown(html_card_header_2A_1_20, unsafe_allow_html=True)
            df_new = df_selection.groupby(['paciente_enumsexobiologico']).sum().reset_index()
            df_new = df_new[["paciente_enumsexobiologico", "Total Doses",
                             "1° Dose", "2° Dose", "Dose Única", "Dose Adicional",
                             "AstraZeneca", "Pfizer", "Coronavac", "Janssen",
                             ]]
            st.dataframe(data=df_new, width=1100, height=400)

        with col3B:
            st.write("")

    with st.container():
        col1B, col2B, col3B = st.columns([1, 25, 1])
        with col1B:
            st.write("")
        with col2B:
            df_area = df_selection.groupby(['vacina_dataaplicacao']).sum().reset_index()

            # 1.2B - Variação Diária da Aplicação das Doses - PLOTAGEM GRÀFICO DE AREA --------------------------------
            fig2 = go.Figure()
            fig2.add_trace(go.Scatter(
                x=df_area['vacina_dataaplicacao'],
                y=df_area['Masculino'],
                name='Masculino',
                mode='lines',
                line=dict(width=1, color='#4169E1')))
            fig2.add_trace(go.Scatter(
                x=df_area['vacina_dataaplicacao'],
                y=df_area['Feminino'],
                name='Feminino',
                mode='lines',
                line=dict(width=1, color='#D70270')))
            fig2.update_layout(legend_font_size=12, autosize=False,
                               paper_bgcolor="#F8F8FF", plot_bgcolor="#F8F8FF",
                               font={'color': "#4169E1", 'family': "sans-serif"}, height=220, width=1100,
                               margin=dict(l=2, r=2, b=4, t=4),
                               legend=dict(orientation="h",
                                           yanchor="top",
                                           y=0.99,
                                           xanchor="left",
                                           x=0.05))
            fig2.update_xaxes(
                title_text='Dias da Aplicação da Vacina',
                title_font=dict(family='Sans-serif', size=12),
                tickfont=dict(family='Sans-serif', size=9),
                rangeslider_visible=True)
            fig2.update_yaxes(
                title_text="Número de Vacinados",
                title_font=dict(family='Sans-serif', size=12),
                tickfont=dict(family='Sans-serif', size=9),
                nticks=7, showgrid=True, gridwidth=0.5, gridcolor='#D3D3D3')

            st.markdown(html_card_header_2A_1_30, unsafe_allow_html=True)
            st.plotly_chart(fig2)
        with col2B:
            st.write("")

    st.markdown("""---""")
    return None

def caracteristicas2_blocoB( df_selection ):
    st.markdown(html_subheader_2B_10, unsafe_allow_html=True)
    st.markdown("""###""")

    with st.container():
        col1A, col2A, col3A, col4A, col5A = st.columns([1, 20, 1, 20, 1])
        with col1A:
            st.write("")
        with col2A:
            dados = df_selection.drop_duplicates(subset=['paciente_id'], keep="last")

            popul_branca = int(436722)
            popul_parda = int(50258)
            popul_preta = int(25568)
            popul_amarela = int(2686)
            popul_indigena = int(1239)
            vacinados_branca = int(dados['BRANCA'].sum())
            vacinados_parda = int(dados['PARDA'].sum())
            vacinados_preta = int(dados['PRETA'].sum())
            vacinados_amarela = int(dados['AMARELA'].sum())
            vacinados_indigena = int(dados['INDIGENA'].sum())
            vacinados_seminfo = int(dados['SEM INFORMACAO'].sum())

            # 2.2A - Raça/Cor da População Residente e População Vacinada Completamente - DECLARAÇÂO DE VARIAVEIS ------------------------------------
            raca_vacina = ['Branca', 'Parda', 'Preta', 'Amarela', 'Indigena', 'Sem Informação']

            y_popul = [popul_branca, popul_preta, popul_parda, popul_amarela, popul_indigena, 0]
            y_vacina = [vacinados_branca, vacinados_preta, vacinados_parda, vacinados_amarela, vacinados_indigena,
                        vacinados_seminfo]

            # 2.2A - Raça/Cor da População Residente e População Vacinada Completamente - PLOTAGEM GRÀFICO DE BARRA - --------------------------------------------------------------
            fig1 = go.Figure()
            fig1.add_trace(go.Bar(name='População Residente (2010)', x=raca_vacina, y=y_popul,
                                  text=y_popul, textposition='outside',
                                  marker_color=['#4169E1', '#4169E1', '#4169E1', '#4169E1', '#4169E1', '#4169E1']))
            fig1.add_trace(go.Bar(name='População Vacinada', x=raca_vacina, y=y_vacina,
                                  text=y_vacina, textposition='outside',
                                  marker_color=['#D70270', '#D70270', '#D70270', '#D70270', '#D70270', '#D70270']))
            fig1.update_layout(legend_font_size=12, autosize=False,
                               paper_bgcolor="#F8F8FF", plot_bgcolor="#F8F8FF",
                               font={'color': "#4169E1", 'family': "sans-serif"}, height=200, width=550,
                               margin=dict(l=2, r=2, b=4, t=4),
                               legend=dict(orientation="v",
                                           yanchor="top",
                                           y=0.95,
                                           xanchor="right",
                                           x=0.98),
                               barmode='group')
            fig1.update_xaxes(
                title_text='Raça/Cor',
                title_font=dict(family='Sans-serif', size=12),
                tickfont=dict(family='Sans-serif', size=9))
            fig1.update_yaxes(
                title_text="Número de Residentes/Vacinados",
                title_font=dict(family='Sans-serif', size=9),
                tickfont=dict(family='Sans-serif', size=9),
                nticks=7, showgrid=True, gridwidth=0.5, gridcolor='#D3D3D3')

            st.markdown(html_card_header_2B_2_11, unsafe_allow_html=True)
            st.plotly_chart(fig1, use_container_width=True)

        with col3A:
            st.write("")
        with col4A:
            st.markdown(html_card_header_2B_2_12, unsafe_allow_html=True)
            df_new = df_selection.groupby(['paciente_racacor_valor']).sum().reset_index()
            df_new = df_new[["paciente_racacor_valor", "Total Doses",
                             "1° Dose", "2° Dose", "Dose Única", "Dose Adicional",
                             "AstraZeneca", "Pfizer", "Coronavac", "Janssen",
                             ]]
            st.dataframe(data=df_new, width=550, height=250)
        with col5A:
            st.write("")

    with st.container():
        col1B, col2B, col3B, col4B, col5B = st.columns([1, 20, 1, 20, 1])
        with col1B:
            st.write("")
        with col2B:
            fig2 = go.Figure()
            fig2.add_trace(go.Violin(
                x=df_selection['paciente_racacor_valor'][df_selection['paciente_enumsexobiologico'] == 'Masculino'],
                y=df_selection["paciente_idade"][df_selection['paciente_enumsexobiologico'] == 'Masculino'],
                legendgroup='Masculino', scalegroup='Masculino', name='Masculino',
                side='negative',
                meanline_visible=True,
                line_color='#4169E1',
                fillcolor='#4169E1'))
            fig2.add_trace(go.Violin(
                x=df_selection['paciente_racacor_valor'][df_selection['paciente_enumsexobiologico'] == 'Feminino'],
                y=df_selection["paciente_idade"][df_selection['paciente_enumsexobiologico'] == 'Feminino'],
                legendgroup='Feminino', scalegroup='Feminino', name='Feminino',
                side='positive',
                meanline_visible=True,
                line_color='#D70270',
                fillcolor='#D70270'))
            fig2.update_layout(violingap=0, violinmode='overlay')
            fig2.update_layout(legend_font_size=12, autosize=False,
                               paper_bgcolor="#F8F8FF", plot_bgcolor="#F8F8FF",
                               font={'color': "#4169E1", 'family': "sans-serif"}, height=250, width=550,
                               margin=dict(l=2, r=2, b=4, t=4),
                               legend=dict(orientation="h",
                                           yanchor="top",
                                           y=0.95,
                                           xanchor="right",
                                           x=0.99))
            fig2.update_xaxes(
                title_text='Raça/Cor',
                title_font=dict(family='Sans-serif', size=12),
                tickfont=dict(family='Sans-serif', size=9))
            fig2.update_yaxes(
                title_text="Idade dos Vacinados",
                title_font=dict(family='Sans-serif', size=12),
                tickfont=dict(family='Sans-serif', size=9),
                nticks=10, showgrid=True, gridwidth=0.5, gridcolor='#D3D3D3')

            st.markdown(html_card_header_2B_2_21, unsafe_allow_html=True)
            st.plotly_chart(fig2, use_container_width=True)

        with col3B:
            st.write("")

        with col4B:
            df_area = df_selection.groupby(['vacina_dataaplicacao']).sum().reset_index()

            # 1.2B - Variação Diária da Aplicação das Doses - PLOTAGEM GRÀFICO DE AREA --------------------------------
            fig2 = go.Figure()
            fig2.add_trace(go.Scatter(
                x=df_area['vacina_dataaplicacao'],
                y=df_area['BRANCA'],
                name='BRANCA',
                mode='lines',
                line=dict(width=1, color='#4169E1'),
                stackgroup='one'))
            fig2.add_trace(go.Scatter(
                x=df_area['vacina_dataaplicacao'],
                y=df_area['SEM INFORMACAO'],
                name='SEM INFORMACAO',
                mode='lines',
                line=dict(width=1, color='#D70270'),
                stackgroup='two'))
            fig2.add_trace(go.Scatter(
                x=df_area['vacina_dataaplicacao'],
                y=df_area['INDIGENA'],
                name='INDIGENAS',
                mode='lines',
                line=dict(width=1, color='#00FFFF'),
                stackgroup='three'))
            fig2.add_trace(go.Scatter(
                x=df_area['vacina_dataaplicacao'],
                y=df_area['PARDA'],
                name='PARDA',
                mode='lines',
                line=dict(width=1, color='#8A2BE2'),
                stackgroup='four'))
            fig2.update_layout(legend_font_size=10,
                               paper_bgcolor="#F8F8FF", plot_bgcolor="#F8F8FF",
                               font={'color': "#4169E1", 'family': "sans-serif"}, height=250, width=550,
                               margin=dict(l=2, r=2, b=4, t=4),
                               legend=dict(orientation="v",
                                           yanchor="top",
                                           y=0.99,
                                           xanchor="left",
                                           x=0.05))
            fig2.update_xaxes(
                title_text='Dias da Aplicação da Vacina',
                title_font=dict(family='Sans-serif', size=12),
                tickfont=dict(family='Sans-serif', size=9),
                rangeslider_visible=True)
            fig2.update_yaxes(
                title_text="Número de Vacinados",
                title_font=dict(family='Sans-serif', size=12),
                tickfont=dict(family='Sans-serif', size=9),
                nticks=7, showgrid=True, gridwidth=0.5, gridcolor='#D3D3D3')

            st.markdown(html_card_header_2B_2_22, unsafe_allow_html=True)
            st.plotly_chart(fig2)

        with col5B:
            st.write("")

    return None

def mapas3( df_selection ):
    return None