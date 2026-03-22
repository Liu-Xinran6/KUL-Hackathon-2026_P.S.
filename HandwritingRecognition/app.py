import streamlit as st
import pandas as pd
from PIL import Image
import os

# 1. Web basic configuration
st.set_page_config(page_title="Time Capsule Decoder", page_icon="📜", layout="wide")

# 2. Load the data
CSV_PATH = "challenge_backs_for_users.csv"
IMG_DIR = "Final_Challenge_Images"

df = pd.read_csv("challenge_backs_for_users.csv", nrows=10)

# 3. Initialize the game
if 'card_index' not in st.session_state:
    st.session_state.card_index = 0

st.title(" Are You Smarter Than AI?")
st.markdown(f"### Help us decode the **Belgian Digital Heritage**")
st.progress((st.session_state.card_index + 1) / len(df))

current_card = df.iloc[st.session_state.card_index]
mms_id = str(current_card['MMS_ID'])

col1, col2 = st.columns([1.5, 1])

with col1:
    st.subheader(" Historical Postcard (Verso)")
    img_path = os.path.join(IMG_DIR, f"{mms_id}_back.jpg")
    if os.path.exists(img_path):
        image = Image.open(img_path)
        st.image(image, use_container_width=True)
    else:
        st.error(f"Image not found: {img_path}")

with col2:
    st.subheader(" AI's Failed Attempt")
    st.info(f"**AI Confidence:** {current_card['AI_Confidence'] * 100:.1f}%")
    st.code(current_card['AI_Detected_Text'], language="text")
    
    st.divider()
    
    st.subheader(" Your Transcription")
    user_input = st.text_area("Can you read what's actually written?", placeholder="Type your transcription here...")
    

    if st.button("Submit & Contribute "):
        if user_input:
            st.balloons()
            st.success(" Incredible! You've just saved a piece of history.")
            st.session_state.submitted = True
        else:
            st.warning("Please try to type at least one word!")

    if st.session_state.get('submitted'):
        if st.button("Next Challenge "):
            st.session_state.card_index += 1
            st.session_state.submitted = False 
            st.rerun()  