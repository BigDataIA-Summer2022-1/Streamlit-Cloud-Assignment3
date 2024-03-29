import boto3
import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml import SafeLoader
from PIL import Image

st.title('Casting Product Image for Quality Inspection Services')
col1, col2 = st.columns(2)
with col1:
    data_load_state = st.text('Loading data...')
# AWS Credentials
aws_key_id = 'AKIA2ZQ35MMOGV7ZZ7PA'
aws_key = 'BrLIKkkVD+kdOQRz4TLp70K0YXZNaBHt6NVcfF2k'
bucket_name = 'casting-product-data-team-1-re'
object_key_img = 'casting-data/train/def_front/cast_def_0_19.jpeg'


client = boto3.client('s3', aws_access_key_id = aws_key_id,
        aws_secret_access_key = aws_key)
img_obj = client.get_object(Bucket = bucket_name, Key = object_key_img)
body = img_obj['Body']
img = Image.open(body)


with col1:
    st.image(img, caption = 'Defective Image in Dataset', use_column_width = 'always')
    data_load_state.text('Loading data...done!')
with col2:
    with open('config.yaml') as file:
        config = yaml.load(file, Loader = SafeLoader)
    authenticator = stauth.Authenticate(
        config['credentials'],
        config['cookie']['name'],
        config['cookie']['key'],
        config['cookie']['expiry_days'],
        config['preauthorized']
    )
    name, authentication_status, username = authenticator.login('Login', 'main')

    if authentication_status:
        authenticator.logout('Logout', 'main')
        st.write(f'Welcome *{name}*')
        st.write('Please use the APIs in the APIs page')
    elif authentication_status == False:
        st.error('Username/password is incorrect!')
    elif authentication_status == None:
        st.warning('Please enter your username and password')
