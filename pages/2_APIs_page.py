import requests
import streamlit as st
from requests_toolbelt.multipart.encoder import MultipartEncoder
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
        st.image(image, caption = 'Uploaded Image to Greyscale', use_column_width = True)

        submit = st.button("Check the Image")

        if submit:
            def process(image, server_url: str):
                m = MultipartEncoder(fields = {'file': ('filename', image, 'image/jpeg')})
                r = requests.post(server_url,
                                data = m,
                                headers = {'Content-Type': m.content_type},
                                timeout = 8000)
                m = None
                return r
            url = "https://metal-defect-classifier-team-1.herokuapp.com/def_or_ok/"
            st.write(process(uploaded_file, url).json())

else:
    st.subheader("Please login first!")
