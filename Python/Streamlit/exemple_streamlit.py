import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("diamonds.csv")

# Créer le titre de la "page web"
st.title("Bienvenue")

# Ajouter des radio boutons
choice = st.radio("Assigner la couleur des points selon...", ["Transparence","Coupe"])
choiceDepth = st.checkbox('Assigner la taille des points selon la profondeur')

# utiliser le résultat de la variable pour générer le graphique
if (choiceDepth == True):
    if (choice == 'Transparence'):
        fig = px.scatter(df, x='carat', y='price', color='clarity', size='depth')
    else:
        fig = px.scatter(df, x='carat', y='price', color='cut', size='depth')
else:
    if (choice == 'Transparence'):
        fig = px.scatter(df, x='carat', y='price', color='clarity')
    else:
        fig = px.scatter(df, x='carat', y='price', color='cut')

# Intégré le graph dans la page streamlit
st.plotly_chart(fig)

### https://cheat-sheet.streamlit.app/