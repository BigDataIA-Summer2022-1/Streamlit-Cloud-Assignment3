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
    st.image('cm.png', use_column_width = True)
    st.write('Classification Report:')
    st.image('classification.png', use_column_width = True)
    # airflow analysis 
    tab1, tab2, tab3, tab4 = st.tabs(["Success Rate", "Task Duration", "DAGs Info", "Log"])

    with tab1:
        st.header("Success? Fail? Still Running?")
        st.image('airflow1.png', width = 750)

    with tab2:
        st.header("The task duration is as follows:")
        st.image('airflow2.png', width = 750)

    with tab3:
        st.header('DAGs Info:')
        st.image('daginfo.png', width = 750)
        
    with tab4:
        st.header('Batch Process Log:')
        st.image("batch.png", width = 750)

else:
    st.subheader("Please login first!")
