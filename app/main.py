import streamlit as st
from model import train_model, predict_category

# Train model
train_model()

# Title
st.title("AI Customer Support Ticket Classifier (BERT Powered)")

# Input
user_input = st.text_area("Enter customer support ticket")

# Button
if st.button("Analyze Ticket"):

    if user_input.strip() == "":
        st.warning("Please enter ticket text.")

    else:

        category = predict_category(user_input)

        st.success(f"Predicted Category: {category}")