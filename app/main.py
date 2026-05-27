import streamlit as st
from model import train_model, predict_category

train_model()

st.title("AI Customer Support Ticket Classifier")

user_input = st.text_area("Enter support ticket")

if st.button("Analyze"):
    category = predict_category(user_input)
    st.success(f"Predicted Category: {category}")


from utils import get_priority

if st.button("Analyze"):
    category = predict_category(user_input)
    priority = get_priority(user_input)

    st.success(f"Category: {category}")
    st.warning(f"Priority: {priority}")