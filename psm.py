# password strength meter

import streamlit as st
import random
import string
import re

# Set up the app
st.set_page_config(page_title="Password Tools", page_icon="🔒")

st.title("🔒 Password Tools")

# Function to check password strength
def check_password(password):
    if len(password) < 8:
        return "❌ Password is too short (min 8 characters)"
    if not re.search(r'[A-Z]', password):
        return "❌ Add at least one uppercase letter"
    if not re.search(r'[a-z]', password):
        return "❌ Add at least one lowercase letter"
    if not re.search(r'[0-9]', password):
        return "❌ Add at least one number"
    if not re.search(r'[!@#$%^&*()_+]', password):
        return "❌ Add at least one special character"
    return "✅ Password is strong!"

# Function to generate a password
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

# Create tabs
tab1, tab2 = st.tabs(["🔍 Password Strength Checker", "🔑 Password Generator"])

# Password Strength Checker
with tab1:
    st.subheader("Check Your Password Strength")
    password = st.text_input("Enter your password", type="password")
    if st.button("Check Strength"):
        st.write(check_password(password))

# Password Generator
with tab2:
    st.subheader("Generate a Secure Password")
    length = st.slider("Password Length", min_value=8, max_value=32, value=12)
    if st.button("Generate Password"):
        st.code(generate_password(length))
