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

# Définition des couleurs
couleur_vert = "#00FF00"  # Vert
couleur_blanc = "#FFFFFF"  # Blanc

# Définition de la largeur pour chaque rectangle
largeur_vert = "25px"  # Largeur des rectangles verts
largeur_blanc = "75px"  # Largeur des rectangles blancs

# Définition de l'espace entre chaque rectangle
espace_entre_rectangles = "10px"

# Définition du style CSS pour les rectangles
style_rectangle = f"""
    display: inline-block;
    width: {largeur_vert};
    height: 100px; /* Hauteur des rectangles */
    margin-right: {espace_entre_rectangles};
    box-shadow: 5px 5px 15px #888888;
    border-radius: 10px;
"""

# Création des cinq rectangles
for i in range(5):
    st.markdown(
        f"""
        <div style="{style_rectangle}">
            <div style="width: 100%; height: 50%; background-color: {couleur_vert}; border-top-left-radius: 10px; border-top-right-radius: 10px;"></div>
            <div style="width: 100%; height: 50%; background-color: {couleur_blanc};"></div>
        </div>
        """,
        unsafe_allow_html=True
    )
import streamlit as st

# Définition des couleurs
couleur_vert = "#00FF00"  # Vert
couleur_blanc = "#FFFFFF"  # Blanc

# Définition de la largeur pour chaque rectangle
largeur_vert = "25px"  # Largeur des rectangles verts
largeur_blanc = "75px"  # Largeur des rectangles blancs

# Définition de l'espace entre chaque rectangle
espace_entre_rectangles = "10px"

# Style CSS pour les rectangles
style_rectangle = f"""
    width: {largeur_vert};
    height: 100px; /* Hauteur des rectangles */
    margin-right: {espace_entre_rectangles};
    box-shadow: 5px 5px 15px #888888;
    border-radius: 10px;
"""

# Affichage des cinq rectangles sur une ligne
st.markdown(
    f"""
    <div style="display: flex; align-items: center;">
        <div style="{style_rectangle}; background-color: {couleur_vert};">
            <div style="width: 100%; height: 50%; background-color: {couleur_vert}; border-top-left-radius: 10px; border-top-right-radius: 10px;"></div>
            <div style="width: 100%; height: 50%; background-color: {couleur_blanc};"></div>
        </div>
        <div style="{style_rectangle}; background-color: {couleur_vert};">
            <div style="width: 100%; height: 50%; background-color: {couleur_vert}; border-top-left-radius: 10px; border-top-right-radius: 10px;"></div>
            <div style="width: 100%; height: 50%; background-color: {couleur_blanc};"></div>
        </div>
        <div style="{style_rectangle}; background-color: {couleur_vert};">
            <div style="width: 100%; height: 50%; background-color: {couleur_vert}; border-top-left-radius: 10px; border-top-right-radius: 10px;"></div>
            <div style="width: 100%; height: 50%; background-color: {couleur_blanc};"></div>
        </div>
        <div style="{style_rectangle}; background-color: {couleur_vert};">
            <div style="width: 100%; height: 50%; background-color: {couleur_vert}; border-top-left-radius: 10px; border-top-right-radius: 10px;"></div>
            <div style="width: 100%; height: 50%; background-color: {couleur_blanc};"></div>
        </div>
        <div style="{style_rectangle}; background-color: {couleur_vert};">
            <div style="width: 100%; height: 50%; background-color: {couleur_vert}; border-top-left-radius: 10px; border-top-right-radius: 10px;"></div>
            <div style="width: 100%; height: 50%; background-color: {couleur_blanc};"></div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)
  
# Initialize connection.
conn = st.connection('mysql', type='sql')

# Perform query.
df = conn.query('SELECT * from client;', ttl=600)
dc =conn.query('SELECT * from credit ;' ,ttl=600 )
# Print results.
#for row in df.itertuples():
    #st.write(f"{row.ID_Client} has a :{row.Sexe}:")
    # Plot histogram
    
#######################
import streamlit as st

# Définition des couleurs
couleur1 = "#ff6347"  # Rouge
couleur2 = "#4682b4"  # Bleu

# Définition du texte pour chaque section
texte_section1 = "Contenu de la première section..."
texte_section2 = "Contenu de la deuxième section..."

# Création de la section à deux couleurs
st.markdown(
    f"""
    <div style="background-color:{couleur1};padding:10px;border-radius:10px;">
    <h2 style="color:white;text-align:center;">Section 1</h2>
    <p style="color:white;text-align:center;">{texte_section1}</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    f"""
    <div style="background-color:{couleur2};padding:10px;border-radius:10px;">
    <h2 style="color:white;text-align:center;">Section 2</h2>
    <p style="color:white;text-align:center;">{texte_section2}</p>
    </div>
    """,
    unsafe_allow_html=True
)
import streamlit as st

# Définition des couleurs
couleur1 = "#ff6347"  # Rouge
couleur2 = "#4682b4"  # Bleu

# Définition du contenu pour chaque section
texte_section1 = "Contenu de la première section..."
texte_section2 = "Contenu de la deuxième section..."

# Création des deux colonnes avec des couleurs différentes
colonne1, colonne2 = st.columns(2)

with colonne1:
    st.markdown(
        f"""
        <div style="background-color:{couleur1};padding:20px;border-radius:10px;">
        <h2 style="color:white;text-align:center;">Section 1</h2>
        <p style="color:white;text-align:center;">{texte_section1}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with colonne2:
    st.markdown(
        f"""
        <div style="background-color:{couleur2};padding:20px;border-radius:10px;">
        <h2 style="color:white;text-align:center;">Section 2</h2>
        <p style="color:white;text-align:center;">{texte_section2}</p>
        </div>
        """,
        unsafe_allow_html=True
    )
import streamlit as st

# Création d'une colonne
colonne = st.columns(3)  # Vous pouvez ajuster le nombre de colonnes selon le nombre d'éléments à aligner

# Ajout des éléments dans la colonne
with colonne[0]:
    st.write("Élément 1")

with colonne[1]:
    st.write("Élément 2")

with colonne[2]:
    st.write("Élément 3")
import streamlit as st

# Définition des couleurs
couleur_vert = "#00FF00"  # Vert
couleur_blanc = "#FFFFFF"  # Blanc

# Fonction pour créer une section avec la couleur spécifiée
def creer_section(couleur):
    return f"""
        <div style="
            width: 100%;
            height: 100px; /* Ajustez la hauteur selon vos besoins */
            background-color: {couleur};
            box-shadow: 5px 5px 5px grey; /* Ajout d'ombre */
            border-radius: 10px; /* Bords arrondis */
            margin-bottom: 10px; /* Marge en bas */
            ">
        </div>
    """

# Création des sections
st.markdown(creer_section(couleur_vert), unsafe_allow_html=True)
st.markdown(creer_section(couleur_blanc), unsafe_allow_html=True)
st.markdown(creer_section(couleur_vert), unsafe_allow_html=True)
st.markdown(creer_section(couleur_blanc), unsafe_allow_html=True)
st.markdown(creer_section(couleur_vert), unsafe_allow_html=True)
import streamlit as st

# Définition des couleurs
couleur_vert = "#00FF00"  # Vert
couleur_blanc = "#FFFFFF"  # Blanc

# Fonction pour créer une section avec la couleur spécifiée
def creer_section(couleur):
    return f"""
        <div style="
            width: 100%;
            height: 100px; /* Ajustez la hauteur selon vos besoins */
            background-color: {couleur};
            border-radius: 10px; /* Bords arrondis */
            margin-bottom: 10px; /* Marge en bas */
            box-shadow: 5px 5px 5px grey; /* Ajout d'ombre */
            ">
        </div>
    """

# Création des sections
st.write(creer_section(couleur_vert), unsafe_allow_html=True)
st.write(creer_section(couleur_blanc), unsafe_allow_html=True)
st.write(creer_section(couleur_vert), unsafe_allow_html=True)
st.write(creer_section(couleur_blanc), unsafe_allow_html=True)
st.write(creer_section(couleur_vert), unsafe_allow_html=True)
import streamlit as st

# Définition des couleurs
couleur_vert = "#00FF00"  # Vert
couleur_blanc = "#FFFFFF"  # Blanc

# Définition des hauteurs pour chaque section
hauteur_vert = "25vh"  # 25% de la hauteur de la fenêtre
hauteur_blanc = "75vh"  # 75% de la hauteur de la fenêtre

# Définition du style CSS pour les rectangles
style_rectangle = f"""
    width: 100%;
    height: 100%;
    box-shadow: 5px 5px 15px #888888;
    border-radius: 10px;
"""

# Création des cinq rectangles
for i in range(5):
    st.markdown(
        f"""
        <div style="{style_rectangle}">
            <div style="height: {hauteur_vert}; background-color: {couleur_vert}; border-top-left-radius: 10px; border-top-right-radius: 10px;"></div>
            <div style="height: {hauteur_blanc}; background-color: {couleur_blanc};"></div>
        </div>
        """,
        unsafe_allow_html=True
    )
import streamlit as st

# Définition des couleurs
couleur_vert = "#00FF00"  # Vert
couleur_blanc = "#FFFFFF"  # Blanc

# Définition de la largeur pour chaque section
largeur_vert = "25vw"  # 25% de la largeur de la fenêtre
largeur_blanc = "75vw"  # 75% de la largeur de la fenêtre

# Définition de l'espace entre chaque section
espace_entre_sections = "10px"

# Définition du style CSS pour les rectangles
style_rectangle = f"""
    display: inline-block;
    width: {largeur_vert};
    height: 100vh;
    margin-right: {espace_entre_sections};
    box-shadow: 5px 5px 15px #888888;
    border-radius: 10px;
"""

# Création des cinq rectangles
for i in range(5):
    st.markdown(
        f"""
        <div style="{style_rectangle}">
            <div style="width: 100%; height: 50%; background-color: {couleur_vert}; border-top-left-radius: 10px; border-top-right-radius: 10px;"></div>
            <div style="width: 100%; height: 50%; background-color: {couleur_blanc};"></div>
        </div>
        """,
        unsafe_allow_html=True
    )

# Style CSS pour ajouter une bordure et une ombre à chaque section
st.markdown(
    """
   <style>
        .section {
            
            width: 220px; /* Largeur de la section */
            height: 120px; /* Hauteur de la section */
            border: 5px solid #ccc; /* Bordure */
            box-shadow: 5px 5px 10px #888; /* Ombre */
            padding: 3px; /* Espacement interne */
            margin: 5px; /* Marge externe */
            display: inline-block;
            margin-right: 100px;
             margin-bottom: 50px;
             border-radius: 10px;
        }
        .section1 {
            width: 220px; /* Largeur de la section */
            height: 60px; /* Hauteur de la section */
            border: 5px solid #ccc; /* Bordure */
            box-shadow: 5px 5px 10px #888; /* Ombre */
            padding: 10px; /* Espacement interne */
            margin: 5px; /* Marge externe */
            display: inline-block;
            margin-right: 100px;
            margin-top: 50px;
            border-radius: 0px;
        }
        .section2 {
            width: 1200px; /* Largeur de la section */
            height: 60px; /* Hauteur de la section */
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
   st.sidebar.page_link("app.py", label=f"      Vue d'Ensemble")
   st.sidebar.page_link("pages/Activite_de_pret.py", label=f"      Activité de pret ({no})")
   st.sidebar.page_link("pages/Risque.py", label=f"      Gestion des Risque")
#Body
st.markdown('<div  class="section2"> </div>  ', unsafe_allow_html=True)
st.title("  Tableau de Bord ")
st.markdown('<div  class="section1"> Nombre de client </div>   <div class="section1"> Pret</div><div class="section1"> Pret</div><div class="section1"> Pret</div> ', unsafe_allow_html=True)
st.markdown('<div  class="section"><h1> {no} </h1></div>   <div class="section"><h1> 1233  CFA</h1></div>   <div class="section"><h1> 12333</h1></div>   <div class="section"><h1> 12333</h1></div> ', unsafe_allow_html=True)
col =st.columns((4,4),gap='medium')
with col[0]:
   #st.markdown('#### Nombre de Client')
   #st.markdown('<div class="section"><h1> 12333</h1> </div>', unsafe_allow_html=True)
   fig, ax = plt.subplots()
   plt.hist(df['Situation_matrimoniale'], bins=20)  # Adjust bins as needed
   plt.xlabel('id')
   plt.ylabel('Fréquence')
   plt.title('Histogramme de la colonne "nombre"')
   st.pyplot(fig)
   
   dcs= dc.sort_values(by="Montant_credit_accorde", ascending=False)
   st.dataframe(dcs,
                 column_order=("Secteur_activite_economique", "Montant_credit_accorde"),
                 hide_index=True,
                 width=None,
                 column_config={
                    "statesr": st.column_config.TextColumn(
                        "Stat",
                    ),
                    "populationr": st.column_config.ProgressColumn(
                        "Populati",
                        format="%f",
                        min_value=0,
                        max_value=max(dcs.Secteur_activite_economique),
                     )}
                 )
   st.write(dcs)
   # Début de la section 2
with col[1]:
   #st.markdown('#### Nombre de Client')
   #st.markdown('<div class="section"><h1> 12333</h1> </div>', unsafe_allow_html=True)
   fig, ax = plt.subplots()
   plt.hist(dc['Secteur_activite_economique'], bins=20)  # Adjust bins as needed
   plt.xlabel('id')
   plt.ylabel('Fréquence')
   plt.title('Histogramme de la colonne "nombre"')
   st.pyplot(fig)
   fig, ax = plt.subplots()
   plt.hist(dc['Sous_secteur_activite_economique'], bins=20)  # Adjust bins as needed
   plt.xlabel('id')
   plt.ylabel('Fréquence')
   plt.title('Histogramme de la colonne "nombre"')
   st.pyplot(fig)  


