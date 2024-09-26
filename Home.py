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

# Sidebar
st.sidebar.title("Kevin Duranty")

# Vidéo dans la sidebar
st.sidebar.video("https://www.youtube.com/watch?v=05yfPEf4r_8")

# Select Bare
st.selectbox("Selectionnez votre niveau d'étude", ["Bac", "Bac +2", "BAC+5"])



