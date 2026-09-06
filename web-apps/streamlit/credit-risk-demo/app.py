import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import altair as alt 
import pandas as pd 
import plotly.express as px
from PIL import Image
import streamlit.components.v1 as components

 #######################
# Page configuration
st.set_page_config(
    page_title="BFT Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded")

alt.themes.enable("dark")
   
# Initialize connection.
#conn = st.connection('mysql', type='sql')

# Perform query.
#df = conn.query('SELECT * from client;', ttl=600)
#dc =conn.query('SELECT * from credit ;' ,ttl=600 )
# Print results.
#for row in df.itertuples():
    #st.write(f"{row.ID_Client} has a :{row.Sexe}:")
    # Plot histogram
    
#######################
test=pd.read_csv('../Mémoire/Loan_Data/test.csv')
train=pd.read_csv('../Mémoire/Loan_Data/train.csv')
# Style CSS pour ajouter une bordure et une ombre à chaque section
st.markdown(
    """
   <style>
        .section {
            
            width: 180px; /* Largeur de la section */
            height: 120px; /* Hauteur de la section */
            border: 5px solid #ccc; /* Bordure */
            box-shadow: 5px 5px 10px #888; /* Ombre */
            padding: 3px; /* Espacement interne */
           
            display: inline-block;
            margin-left: 50px;
            
            margin-right: 50px;
             margin-bottom: 50px;
             border-radius: 10px;
        }
        .section1 {
            width: 180px; /* Largeur de la section */
            height: 60px; /* Hauteur de la section */
            border: 5px solid #ccc; /* Bordure */
            box-shadow: 5px 5px 10px #888; /* Ombre */
            padding: 10px; /* Espacement interne */
            
            display: inline-block;
            margin-right: 50px;
            margin-left: 50px;
            margin-top: 50px;
            border-radius: 0px;
        }
        .section2 {
            width: 1200px; /* Largeur de la section */
            height: 30px; /* Hauteur de la section */
            border: 5px solid #ccc; /* Bordure */
            box-shadow: 5px 5px 10px #888; /* Ombre */
            padding: 10px; /* Espacement interne */
            margin: 5px; /* Marge externe */
            margin-right: 100px;
            margin-top: 50px;
            border-radius: 0px;
        }
         h1{color:green ;
        text-align:center };
        h2{color:red ;
        text-align:center };

       
        </style>
        """,
        unsafe_allow_html=True
)

#alt.themes.enable("dark")

# sidebar
with st.sidebar :
   st.image("image/logo-BFT.png")
   
   annee=  ["      De 2022","     De 2023","    De 2024"]
   select_period =st.selectbox('',annee)

   no = 2
   st.sidebar.page_link("app.py", label=f"         Activité de pret  ({no})")
   st.sidebar.page_link("pages/Risque.py", label=f"      Gestion des Risque")
#Body
st.markdown('<div  class="section2"> </div>  ', unsafe_allow_html=True)
st.title("  Tableau de Bord ")
st.markdown('<div  class="section1">  </div>   <div class="section1"> </div><div class="section1"> </div><div class="section1"> </div> ', unsafe_allow_html=True)
st.markdown('<div  class="section"><h1> </h1></div> <div  class="section"><h1> </h1></div>   <div class="section"><h1> </h1></div>   <div class="section"><h1> </h1></div>    ', unsafe_allow_html=True)
col =st.columns((4,4),gap='medium')


  