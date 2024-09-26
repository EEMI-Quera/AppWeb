import streamlit as st

# Titre
st.title("Mon formulaire")

# Texte
st.write("Ceci est un formulaire de contact")

# Champ de saisie
user_input = st.text_input("Tapez votre texte : ")

st.write(user_input)


# Image
st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSbMZFucLMvnC70v26VRtwnsv73EX8FpKxCqA&s")


