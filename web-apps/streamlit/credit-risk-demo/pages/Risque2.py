import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import altair as alt 
import pandas as pd 
import plotly.express as px
from PIL import Image
import streamlit.components.v1 as components
import streamlit as st
from PIL import Image
import pickle
##Data
data= pd.read_csv('../Mémoire/Loan_Data/test.csv')

 #######################
# Page configuration
st.set_page_config(
    page_title="BFT Dashboard",
    page_icon=" 📊 ",
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

# Style CSS pour ajouter une bordure et une ombre à chaque section
st.markdown(
    """
   <style>
         .section1 {
            width: 450px; /* Largeur de la section */
            height: 150px; /* Hauteur de la section */
            border: 5px solid  #888; /* Bordure */
            box-shadow: 5px 5px 10px #888; /* Ombre */
            padding: 10px; /* Espacement interne */
            margin: 5px; /* Marge externe */
            display: inline-block;
            margin-right: 100px;
            margin-top: 50px;
            border-radius: 0px;
        }
        .section2 {
            width: 1130px; /* Largeur de la section */
            height: 10px; /* Hauteur de la section */
            border: 5px solid #ccc; /* Bordure */
            box-shadow: 5px 5px 10px #888; /* Ombre */
            padding: 10px; /* Espacement interne */
            margin: 5px; /* Marge externe */
            margin-right: 100px;
            margin-top: 50px;
            margin-bottom: 50px;
            border-radius: 0px;
        }
         h1{color:#069840;
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
   st.sidebar.page_link("app.py", label=f"         Activité de pret ({no})   ")
   st.sidebar.page_link("pages/Risque.py", label=f"      Gestion des Risque")
#Body
st.markdown('<div  class="section2"> </div>  ', unsafe_allow_html=True)

#from sklearn_model_selection import train_test_split
#X=data.drop("Loan_Status",axis= 1)
#Y=data.Loan_Status


          
     


st.title("Demo prévision Solvabilité clients")
col =st.columns((4,4),gap='medium')
#


model = pickle.load(open('./Model/ML_Model.pkl', 'rb'))
def run():
    with col[0]:
    

            

            ## Account No
            account_no = st.text_input('Numero de compte')

            ## Full Name
            fn = st.text_input('Nom complet')

            ## For PME
            gen_display = ('PADME','CLCAM','FECECAM','Poste')
            gen_options = list(range(len(gen_display)))
            gen = st.selectbox("Institution",gen_options, format_func=lambda x: gen_display[x])

            ## For gender
            gen_display = ('Femme','Homme')
            gen_options = list(range(len(gen_display)))
            gen = st.selectbox("Genre",gen_options, format_func=lambda x: gen_display[x])

            ## For Marital Status
            mar_display = ('Non','Oui')
            mar_options = list(range(len(mar_display)))
            mar = st.selectbox("Marié(e)", mar_options, format_func=lambda x: mar_display[x])

            ## No of dependets
            dep_display = ('Non','Un','Deux','Plus de deux')
            dep_options = list(range(len(dep_display)))
            dep = st.selectbox("Dependents",  dep_options, format_func=lambda x: dep_display[x])
            ## For edu
            edu_display = ('Non Diplomé','Diplomé')
            edu_options = list(range(len(edu_display)))
            edu = st.selectbox("Education",edu_options, format_func=lambda x: edu_display[x])
             
    with col[1]:
            

           ## For emp status
            emp_display = ('Employé','Business')
            emp_options = list(range(len(emp_display)))
            emp = st.selectbox("Emploi",emp_options, format_func=lambda x: emp_display[x])

            ## For Property status
            prop_display = ('Rural','Semi-Urban','Urbain')
            prop_options = list(range(len(prop_display)))
            prop = st.selectbox("territoire",prop_options, format_func=lambda x: prop_display[x])

            ## For Credit Score
            cred_display = ('Entre 3 et 5','Plus de 5')
            cred_options = list(range(len(cred_display)))
            cred = st.selectbox("Status client",cred_options, format_func=lambda x: cred_display[x])

            ## Applicant Monthly Income
            mon_income = st.number_input("Revenu mensuel du demandeur($)",value=0)

            ## Co-Applicant Monthly Income
            co_mon_income = st.number_input("Revenu mensuel du codemandeur($)",value=0)

            ## Loan AMount
            loan_amt = st.number_input("Montant souhaité",value=0)

            ## loan duration
            dur_display = ['2 Mois','6 Mois','8 Mois','1 An','16 Mois']
            dur_options = range(len(dur_display))
            dur = st.selectbox("Durée de Pret ",dur_options, format_func=lambda x: dur_display[x])

    if st.button("Analyser"):
        duration = 0
        if dur == 0:
            duration = 60
        if dur == 1:
            duration = 180
        if dur == 2:
            duration = 240
        if dur == 3:
            duration = 360
        if dur == 4:
            duration = 480
        features = [[gen, mar, dep, edu, emp, mon_income, co_mon_income, loan_amt, duration, cred, prop]]
        print(features)
        prediction = model.predict(features)
        lc = [str(i) for i in prediction]
        ans = int("".join(lc))
        if ans == 0:
            st.error(
                "Bonjour: Le client " + fn +" || "
                "De numero de Compte: "+account_no +' || '
                'Apres analyses, Ne peut pas obtenir  ce pret '
            )
        else:
            st.success(
            "Bonjour: Le client " + fn +" || "
                    "De numero de Compte: "+account_no +' || '
                    'Apres nos analyses, Ne peut obtenir  ce pret '
                )

run()








#Affichage
col =st.columns((4,4),gap='medium')
#with col[0]:
   #st.markdown('#### Nombre de Client')
   #st.markdown('<div class="section"><h1> 12333</h1> </div>', unsafe_allow_html=True)
st.markdown('<div  class="section1"> Interpretation et explicabilité (Travail en cours) </div>   <div class="section1"> Graphique score emprunt....</div> ', unsafe_allow_html=True)   
   