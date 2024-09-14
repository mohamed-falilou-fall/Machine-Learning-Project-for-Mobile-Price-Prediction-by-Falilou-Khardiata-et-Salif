import streamlit as st
import pickle
import numpy as np

# Chargement du modèle
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

# Titre de l'APP
st.title('FKS (Falilou, Khardiata et Salif) APP de Prédiction de Prix en $ de Smartphone aux Etats-Unis')

# User Interface
st.sidebar.header('Veuillez saisir les caractéristiques du smartphone désiré')

# Paramètres pour le smartphone avec les caractéristiques fournies
screen_size = st.sidebar.slider(
    'Taille de l\'écran (en pouces)', 
    min_value=5.7, 
    max_value=6.9, 
    step=0.1
)
ram = st.sidebar.slider(
    'RAM (en Go)', 
    min_value=3, 
    max_value=8, 
    step=1
)
storage = st.sidebar.slider(
    'Stockage (en Go)', 
    min_value=32, 
    max_value=256,  
    step=32
)
battery_capacity = st.sidebar.slider(
    'Capacité de la batterie (en mAh)', 
    min_value=1000, 
    max_value=5000,  
    step=10
)
camera_quality = st.sidebar.slider(
    'Qualité de la caméra (en MP)', 
    min_value=12, 
    max_value=64, 
    step=4
)

# Collecte des données sous forme de tableau
input_data = np.array([[screen_size, ram, storage, battery_capacity, camera_quality]])

# Affichage des données d'entrée pour débogage
st.write("Caractéristiques saisies :", input_data)

# Vérification des dimensions de l'entrée
st.write("Dimensions des données d'entrée :", input_data.shape)

# Bouton pour valider les entrées
if st.button('Prédire le prix'):

    # Prédictions
    if hasattr(model, 'predict'):
        try:
            # Vérifier si la forme des données d'entrée est correcte
            if input_data.shape[1] == 5:  # Assurez-vous que le modèle attend 5 caractéristiques
                # Prédiction brute
                prediction = model.predict(input_data)[0]

                # Ajustement de la prédiction au pas de 50 $
                rounded_prediction = 50 * round(prediction / 50)
                
                # Affichage de la prédiction
                st.write(f'**Prix estimé du smartphone** : ${rounded_prediction:,.2f}')
            else:
                st.write("Erreur : Les données d'entrée n'ont pas le bon nombre de caractéristiques.")

        except Exception as e:
            st.write("Erreur lors de la prédiction :", e)
    else:
        st.write("Erreur : Le modèle chargé n'a pas la méthode 'predict'.")

# Bas de page
st.markdown("---")
st.markdown("#### © 2024 Mohamed Falilou Fall, Khardiata Ke Faye, Mamadou Salif Diallo - Application de Prédiction de Prix en $ de Smartphone")
st.markdown("##### Contacts : mff.faliou.fall@gmail.com | khardiatakefaye@gmail.com | mamadousalif.diallo@uadb.edu.sn ")
