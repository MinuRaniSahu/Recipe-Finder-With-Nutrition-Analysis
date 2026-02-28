import streamlit as st
from main1 import DevSearch_expedition

st.title("Recipe Finder")

dish = st.text_input("Enter recipe name")

if dish:
    result = DevSearch_expedition(dish)
    st.write(result)
    if dish:
    result = DevSearch_expedition(dish)

if isinstance(result, dict):
    st.subheader("Ingredients")
     for item in result["ingredients"]:
         st.write("- " + item)

        st.subheader("Instructions")
        st.write(result["instructions"])
 else:
        st.write(result)
