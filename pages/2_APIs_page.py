import numpy as np
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
        image = Image.open(uploaded_file)
        try:
            new_img = image.resize((width, height), Image.BILINEAR)
            if new_img.mode != 'L':
                img = new_img.convert("L")
        except Exception as e:
            print(e)
        img_array = np.array(img)
        st.image(img, caption = 'Uploaded Image', use_column_width = True)
        submit = st.button("Check the Image")
        if submit:
            res = requests.get(f"https://airbus-detection-data-services.herokuapp.com/image_number_of_ships/{img_array}")
            st.write(res.json())
else:
    st.subheader("Please login first!")