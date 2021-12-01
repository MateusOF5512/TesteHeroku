





path_vac = "dados_gerais.csv"







#------------------------------------------------------------------------------------ HTML VARIABLES:

# --------------------------- INTRODUÇÂO --------------------------------------------------------------
html_title="""
<head>
<title>PControlDB</title>
<meta charset="utf-8">
<meta name="keywords" content="project control, dashboard, management">
<meta name="description" content="project control dashboard">
<meta name="author" content="Mateus Ortiz Ferreira">
<meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<h1 style="font-size:300%; color:#4169e1; font-family:sans-serif"> Observatório de Dados Abertos <br>
 <hr style= "display: block;
  margin-top: 0.5em;
  margin-bottom: 0.5em;
  margin-left: auto;
  margin-right: auto;
  border-style: inset;
  border-width: 1.5px;"></h1>
"""
html_card_header_0A1="""
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #4169E1; padding-top: 5px; width: 550px; height: 50px;">
    <h5 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif; text-align: center; padding: 10px 0;"
    >Descrição dos Dados</h5>
  </div>
</div>
"""
html_card_body_0A1="""
<div class="card" style="border-radius: 0px 0px 0px 0px; background: #F5F5F5; padding-top: 5px; width: 550px; height: 50px;">
    <h10 class="card-title" style="background-color:#F5F5F5; color:#4169E1; 
        font-family:sans-serif; text-align: left; padding: 5px 0;"
        >Os dashboards a seguir apresentam os Dados referentes à Campanha de Vacinação contra Covid-19, 
        da população residente em Florianópolis/SC, sendo disponibilizados neste formato para visualização, 
        análise e aprofundamento da sociedade.</h10>
</div>
"""

html_card_header_0A2="""
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #4169E1; padding-top: 5px; width: 550px; height: 50px;">
    <h5 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif; text-align: center; padding: 10px 0;"
    >Links Importantes</h5>
  </div>
</div>
"""
html_card_body_0A2="""
<div class="card">
    <h6 class="card-title" style="background-color:#F5F5F5; color:#4169E1; 
        font-family:sans-serif; text-align: left; padding: 7px 0;</h6>
</div>
"""
#------------------- 1.1 - Número de Doses & Vacinas Aplicadas -------------------------------------------

html_header_01="""
<div class="card">
  <div class="card-body">
    <h2 class="card-title" style="color:#4169E1; font-family:sans-serif; text-align: center; padding: 10px 0;"
    >1 - Campanha de Vacinação contra COVID-19 em Florianópolis-SC</h2>
  </div>
</div>
"""
html_subheader_11="""
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 10px 10px; background: #4169E1; padding-top: 5px; width: 1200px; height: 60px;">
    <h3 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif; text-align: center; padding: 10px 10px;"
    >1.1 - Número de Doses & Vacinas Aplicadas</h3>
  </div>
</div>
"""
html_card_header_1A1="""
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #4169E1; padding-top: 5px; width: 275px; height: 60px;">
    <h5 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif; text-align: center; padding: 0px 0;"
    >Vacinados com 1° Dose: Proporção</h5>
  </div>
</div>
"""
html_card_header_1A2="""
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #4169E1; padding-top: 5px; width: 275px; height: 60px;">
    <h5 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif; text-align: center; padding: 0px 0;"
    >Vacinados com 1° Dose: Quantidade</h5>
  </div>
</div>
"""
html_card_header_1A3="""
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #4169E1; padding-top: 5px; width: 275px; height: 60px;">
    <h5 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif; text-align: center; padding: 0px 0;"
    >Vacinados Completamente: Quantidade</h5>
  </div>
</div>
"""
html_card_header_1A4="""
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #4169E1; padding-top: 5px; width: 275px; height: 60px;">
    <h5 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif; text-align: center; padding: 0px 0;"
    >Vacinados Completamente: Proporção</h5>
  </div>
</div>
"""

html_card_header_1B11="""
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #4169E1; padding-top: 5px; width: 550px; height: 40px;">
    <h5 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif; text-align: center; padding: 5px 5;"
    >Quantidade de Vacinas Aplicadas por Dose</h5>
  </div>
</div>
"""
html_card_header_1B12="""
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #4169E1; padding-top: 5px; width: 550px; height: 40px;">
    <h5 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif; text-align: center; padding: 5px 5;"
    >Proporção entre as Vacinas Aplicadas</h5>
  </div>
</div>
"""
html_card_header_1B2="""
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #4169E1; padding-top: 5px; width: 550px; height: 40px;">
    <h5 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif; text-align: center; padding: 5px 0;"
    >Dados dos Pacientes Vacinados</h5>
  </div>
</div>
"""
#--------------------------------------- 1.2 - Variação das Doses & Vacinas Aplicadas ----------------------
html_subheader_12="""
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 10px 10px; background: #4169E1; padding-top: 5px; width: 1200px; height: 60px;">
    <h3 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif; text-align: center; padding: 10px 10px;"
    >1.2 - Variação das Doses & Vacinas Aplicadas</h3>
  </div>
</div>
"""
html_card_header_1C11="""
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #4169E1; padding-top: 5px; width: 550px; height: 40px;">
    <h5 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif; text-align: center; padding: 5px 5;"
    >Variação das Doses Aplicadas</h5>
  </div>
</div>
"""
html_card_header_1C12="""
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #4169E1; padding-top: 5px; width: 550px; height: 40px;">
    <h5 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif; text-align: center; padding: 5px 5;"
    >Variação das Vacinas Aplicadas</h5>
  </div>
</div>
"""
html_card_header_1C20="""
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #4169E1; padding-top: 5px; width: 550px; height: 40px;">
    <h5 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif; text-align: center; padding: 5px 5;"
    >Dados</h5>
  </div>
</div>
"""


#------------------------------------------------2 -
html_header_20="""
<div class="card">
  <div class="card-body">
    <h2 class="card-title" style="color:#4169E1; font-family:sans-serif; text-align: center; padding: 10px 0;"
    >2 - Características da População Vacinada em Florianópolis-SC/BR</h2>
  </div>
</div>
"""
html_subheader_2A_10="""
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 10px 10px; background: #4169E1; padding-top: 5px; width: 1200px; height: 60px;">
    <h3 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif; text-align: center; padding: 10px 10px;"
    >2.1 - Análise do Sexo Biológico</h3>
  </div>
</div>
"""
html_card_header_2A_1_11="""
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #4169E1; padding-top: 5px; width: 355px; height: 40px;">
    <h5 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif; text-align: center;  padding: 5px 5;"
    >Vacinados do Sexo Masculino</h5>
  </div>
</div>
"""
html_card_header_2A_1_12="""
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #4169E1; padding-top: 5px; width: 355px; height: 40px;">
    <h5 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif; text-align: center;  padding: 5px 5;"
    >Proporção entre os Sexos</h5>
  </div>
</div>
"""
html_card_header_2A_1_13="""
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #4169E1; padding-top: 5px; width: 355px; height: 40px;">
    <h5 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif; text-align: center;  padding: 5px 5;"
    >Vacinados do Sexo Feminino</h5>
  </div>
</div>
"""
html_card_header_2A_1_20="""
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #4169E1; padding-top: 5px; width: 1100px; height: 40px;">
    <h5 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif; text-align: center; padding: 0px 0px;"
    >Sexo Biológico - Dados Agrupados</h5>
  </div>
</div>
"""
html_card_header_2A_1_30="""
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #4169E1; padding-top: 5px; width: 1100px; height: 40px;">
    <h5 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif; text-align: center; padding: 5px 5;"
    >Variação de Vacinados</h5>
  </div>
</div>
"""


html_subheader_22="""
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 10px 10px; background: #4169E1; padding-top: 5px; width: 1200px; height: 60px;">
    <h3 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif; text-align: center; padding: 10px 10px;"
    >2.1 - Análise do Sexo Biológico</h3>
  </div>
</div>
"""
html_card_header_2B="""
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #4169E1; padding-top: 5px; width: 355px; height: 40px;">
    <h5 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif; text-align: center;  padding: 5px 5;"
    >Vacinados do Sexo Masculino</h5>
  </div>
</div>
"""
html_subheader_2B_10="""
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 10px 10px; background: #4169E1; padding-top: 5px; width: 1200px; height: 60px;">
    <h3 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif; text-align: center; padding: 10px 10px;"
    >2.1 - Análise da Raça/Cor</h3>
  </div>
</div>
"""
html_card_header_2B_2_11="""
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #4169E1; padding-top: 5px; width: 550px; height: 40px;">
    <h5 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif; text-align: center; padding: 0px 0;"
    >População Residente x População Vacinada</h5>
  </div>
</div>
"""
html_card_header_2B_2_12="""
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #4169E1; padding-top: 5px; width: 550px; height: 40px;">
    <h5 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif; text-align: center; padding: 0px 0;"
    >Raça/Cor - Dados Agrupados</h5>
  </div>
</div>
"""
html_card_header_2B_2_21="""
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #4169E1; padding-top: 5px; width: 550px; height: 40px;">
    <h5 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif; text-align: center; padding: 0px 0;"
    >Raça/Cor - Dados Agrupados</h5>
  </div>
</div>
"""
html_card_header_2B_2_22="""
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #4169E1; padding-top: 5px; width: 550px; height: 40px;">
    <h5 class="card-title" style="background-color:#4169E1; color:#F5F5F5; font-family:sans-serif; text-align: center; padding: 0px 0;"
    >Raça/Cor - Dados Agrupados</h5>
  </div>
</div>
"""

