import streamlit as st
st.title("Welcome! Ai Chatbot.")
you=st.text_input("Enter a prompt:")
if st.button("send"):
    if you:
        st.write(you)
        st.success("success")
    else:
        st.warning("please enter correct prompt.")