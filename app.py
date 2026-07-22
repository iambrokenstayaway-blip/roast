import streamlit as st

# Set up the title of your webpage
st.title("I am Loid Forger. I like Yor Forger and basketball and I'm failing hsc")

# Create a text input box on the website (replaces input())
name = st.text_input("Enter your name:")

# Check if the user has typed anything
if name:
    # A simple dictionary of funny responses based on names
    # You can customize these or use logic to generate jokes
    jokes = {
        "nabil": "Bakayarrooo. Thats a stupid name. Baka, maybe you should type your master's name that starts with T. Try again",
        "tasin": "Good boy. Your master is happy",
        "antony": "Bakayarrooo. Thats a stupid name. Baka, maybe you should type your master's name that starts with T",
        "toppo": "Bakayarrooo. Thats a stupid name. Baka, maybe you should type your idol's name that starts with T and ends with an in. he likes boxin. dhcbhbcdjbsjbi"
    }

    # Process the name (lowercase to catch variations)
    name_lower = name.lower().strip()

    if name_lower in jokes:
        response = jokes[name_lower]
    else:
        response = " Nabil is an absolute Baka.Incorrect Answer."

    # Output the result to the webpage (replaces print())
    st.success(response)
