import streamlit as st
import requests
from PIL import Image

st.title('Casting Product Image for Quality Inspection Services')
st.markdown("Using our model to check your product!")
if st.session_state["authentication_status"]:
    st.write("The purpose of this app is to predict and check if the uploaded image is a defective product or an ok product.")
    st.write("You can upload an product image and you will get the probability of the product is a defective product or an ok product.")

    uploaded_file = st.file_uploader("Please Choose a Casting Product Image File to Upload", type = ["jpg", "jpeg"])
    if uploaded_file is not None:
        width, height = 300, 300
        image = Image.open(uploaded_file).convert('L')
        img = image.resize((width, height), Image.ANTIALIAS)
        st.image(image, caption = 'Uploaded Image to Greyscale', use_column_width = True)
        submit = st.button("Check the Image")
        if submit:
            res = requests.get(f"https://metal-defect-classifier-team-1.herokuapp.com/docs#/default/def_or_ok_def_or_ok__img__get/{img}")
            st.write(res.json())
else:
    st.subheader("Please login first!")
