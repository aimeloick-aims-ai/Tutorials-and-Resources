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
   st.sidebar.page_link("pages/Risque2.py", label=f"      Gestion des Risque")
#Body
st.markdown('<div  class="section2"> </div>  ', unsafe_allow_html=True)
st.title("Gestion de Pret  ")
#Modele
import sklearn  as sk 
#from sklearn_model_selection import train_test_split
#X=data.drop("Loan_Status",axis= 1)
#Y=data.Loan_Status


st.write(data)
st.markdown('<div  class="section2"> </div>  ', unsafe_allow_html=True)
year_list = list(data.Loan_ID.unique())[::-1]

selected_year = st.selectbox('Selectionner une demande', year_list)
df = data[data.Loan_ID == selected_year]
df.Gender=df.Gender.map({'Male':1,'Female':0})
df.Married=df.Married.map({'Yes':1,'No':0})
df.Dependents=df.Dependents.map({'0':0,'1':1,'2':2,'3+':3})
df.Education=df.Education.map({'Graduate':1,'Not Graduate':0})
df.Self_Employed=df.Self_Employed.map({'Yes':1,'No':0})
df.Property_Area=df.Property_Area.map({'Urban':2,'Rural':0,'Semiurban':1})



model = pickle.load(open('./Model/ML_Model.pkl', 'rb'))
if st.button(f"Analyser la demande {df.Loan_ID.iloc[0]}"):
        
       


        feature = [[df.Gender.iloc[0], df.Married.iloc[0], int(df.Dependents.iloc[0]), df.Education.iloc[0],df.Self_Employed.iloc[0], int(df.ApplicantIncome.iloc[0]), int(df.CoapplicantIncome.iloc[0]), df.LoanAmount.iloc[0], df.Loan_Amount_Term.iloc[0], df.Credit_History.iloc[0],df.Property_Area.iloc[0]]]
        #st.write(feature)
        predictions = model.predict(feature)
        lc = [str(i) for i in predictions]
        ans = int("".join(lc))
        if ans == 0:
            st.error(
                "Bonjour: Le client " + df.Loan_ID.iloc[0]+" || "
                "De numero de Compte: "+df.Loan_ID.iloc[0] +' || '
                'Apres analyses, Ne peut pas obtenir  ce pret '
            )
        else:
            st.success(
            "Bonjour: Le client " + df.Loan_ID.iloc[0] +" || "
                    "De numero de Compte: "+ df.Loan_ID.iloc[0] +' || '
                    'Apres Nos analyses, Ne peut obtenir  ce pret '
                )
     
#st.markdown('<div  class="section1"> ..... </div>   <div class="section1"> ....</div> ', unsafe_allow_html=True)
st.markdown('<div  class="section1"> Interpretation et explicabilité (Travail en cours) </div>   <div class="section1"> Graphique score emprunt....</div> ', unsafe_allow_html=True)  
col =st.columns((4,4),gap='medium')
#

