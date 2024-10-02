import streamlit as st
from streamlit_option_menu import option_menu
from dotenv import load_dotenv
import os


from Models.Anime_DF import display_Anime_df



load_dotenv()
HUGGINGFACE_API_KEY = st.secrets['PrashantGenAIHuggingFaceToken']

st.set_page_config(
        page_title="Generative Image",
)

# Define the sidebar
with st.sidebar:
    # Create the options menu
    selected = option_menu(menu_title="Image-Gen Models",
                           options=["Stable Diffusion XL"],
                           icons=["box"],
                           menu_icon="boxes",
                           default_index=0
                           )
    

if selected == "Anime Diffusion":
    display_Anime_df(HUGGINGFACE_API_KEY1)
