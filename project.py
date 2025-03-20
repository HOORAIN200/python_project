import streamlit as st
from datetime import datetime

# Streamlit UI
st.title("🎂 Birthday Countdown ⏳")
st.write("Enter your birthday to see how many days are left!")

# User input for birthday
date_input = st.date_input("Select your birthday:")

if date_input:
    # Get today's date
    today = datetime.today().date()
    birthday = date_input.replace(year=today.year)
    
    # If birthday has already passed this year, set it for next year
    if birthday < today:
        birthday = birthday.replace(year=today.year + 1)
    
    # Calculate the days left
days_left = (birthday - today).days
    
    # Display the countdown
if days_left == 0:
        st.success("🎉 Happy Birthday! 🥳🎂")
else:
        st.info(f"🎈 Your birthday is in {days_left} days! 🎁")
