import streamlit as st

# Set up the title of your webpage
st.title("I am Loid Forger. I like Yor Forger and basketball and I'm failing hsc")

# Create a text input box on the website
name = st.text_input("Enter your name:")

# Check if the user has typed anything
if name:
    # A dictionary of funny responses based on names
    jokes = {
        "nabil": "Bakayarrooo. Thats a stupid name. Baka, maybe you should type your master's name that starts with T. Try again",
        "tasin": "Good boy. Your master is happy",
        "antony": "Bakayarrooo. Thats a stupid name. Baka, maybe you should type your master's name that starts with T",
        "toppo": "Snot nosed toppi toppi femboy Baka, maybe you should type the coolest persons name that starts with T, you eat his dih.It ends with an in. he likes boxin. dhcbhbcdjbsjbi",
        "labib": "Saala pu*ki me daala masala.Labib ne chaat daala. Ho gaya kala. shut the fuck up. Type the name of the strongest person you have ever seen. Baka. His majesty has a name that starts with T. You eat his dih.",
        "sonet":"Long ass goofy ass NiGGGA.Saala pu*ki me daala masala. Sonet ne chaat daala. Ho gaya kala. shut the fuck up, Baka. His majesty has a name that starts with T. You eat his dih.",
        "muin":"Fat ass white ass white nigga. You don't have any beard and you are really very gay. You are in a romantic relationship with Fahim. Shut the fuck up and lose some weight.",
        "labib2":"Gay nigga. Shut the fuck up",
        "fahim":"gay"
        
    }
    
    # Process the name (lowercase to catch variations)
    name_lower = name.lower().strip()
    
    # --- AUDIO AUDIO LOGIC ---
    if name_lower == "tasin":
        # Play both celebration sounds at the exact same time
        st.audio("https://www.myinstants.com/media/sounds/kids-saying-yay-sound-effect_3.mp3", format="audio/mp3", autoplay=True)
        st.audio("https://www.myinstants.com/media/sounds/gugugugu.mp3", format="audio/mp3", autoplay=True)
    else:
        # Every other name (Nabil, Antony, Toppo, or anything wrong) triggers the brain fart sound
        st.audio("https://www.myinstants.com/media/sounds/long-brain-fart.mp3", format="audio/mp3", autoplay=True)
        
    # --- TEXT OUTPUT LOGIC ---
    if name_lower in jokes:
        response = jokes[name_lower]
        st.success(response)
    else:
        response = " You are an absolute Baka. Incorrect Answer. Type your master's name."
        st.error(response)

