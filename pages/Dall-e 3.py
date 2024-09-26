import streamlit as st

st.title("Dall-e 3")

# 1. Champ de saisie
user_input = st.text_input("Tapez votre texte")

# 2. Champ de saisie dans la sidebar (pour la clé OpenAI)
openai_key = st.sidebar.text_input("Renseignez la clé OpenAI")

# 3. Intéraction avec OpenAI
from openai import OpenAI

client = OpenAI(api_key=openai_key)
image = client.images.generate(
    model="dall-e-2",
    prompt=user_input,
    size="512x512",
    quality="standard",
    n=1,
)

image_url = image.data[0].url

# 4. Affichage de l'image
st.image(image_url)

