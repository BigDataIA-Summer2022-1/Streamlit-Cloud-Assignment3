import streamlit as st
from PIL import Image

st.title('Casting Product Image for Quality Inspection Services')
st.markdown("Using our model to check the entire test set!")
if st.session_state["authentication_status"]:
    st.write("This page shows the Airflow details of all the test data!")
    # confusion matrix
    st.write("The confusion matrix is as follows:")
    col1, col2 = st.columns(2)
    col1.metric("True Negative", "262")
    col2.metric("False Negative", "0")
    col1.metric("False Positive", "1")
    col2.metric("True Positive", "452")
    cm_img = Image.open('cm.png')
    st.image('cm.png', use_column_width = True)
    # airflow analysis
    

else:
    st.subheader("Please login first!")