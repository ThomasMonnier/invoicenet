import streamlit as st
import shutil
from src import st_stdout

from src.prepare_data import prepare
from src.train import train
from src.predict import predict

# Set the app title
st.title("InvoiceNet: Train your Model")
st.write(
    "This app provides an easy way to use InvoiceNet's fine tuning"
)

prepare_data = st.button("Prepare the training data")
if 'prepared_data' not in st.session_state:
    st.session_state['prepared_data'] = False

if prepare_data:
    if st.session_state['prepared_data'] == False:
        with st_stdout("info"):
            prepare('train_data')
        with st_stdout('success'):
            print('Data is ready for training')
            st.session_state['prepared_data'] = True
    else:
        with st_stdout("error"):
            print("Re-fresh the page to use another training set")

if st.session_state['prepared_data']:
    with st_stdout("success"):
        print('Click on "Train data" !')
            
field = st.selectbox(
     'Choose a field to train your data on',
     ('PDL', 'provider_name'))

steps = st.slider('Number of steps of the training process', 8, 50000, 1000)
train_data = st.button("Train data")

if 'trained_data' not in st.session_state:
    st.session_state['trained_data'] = False

if train_data:
    if st.session_state['prepared_data'] == False:
        with st_stdout("error"):
            print("Don't forget to prepare your data!")
    else:
        with st_stdout("info"):
            train(field, steps=steps)
        with st_stdout("success"):
            st.session_state['trained_data'] = True
            print(f"The model has been trained on {field}")

if st.session_state['trained_data']:
    with st_stdout("success"):
        print('Click on "Get Prediction" !')

predict_file = st.file_uploader('Enter the PDF file', type="pdf")
get_result = st.button("Get prediction")

if get_result and st.session_state['prepared_data'] and st.session_state['trained_data']:
  if predict_file is not None:
    with open("to_predict.pdf", "wb") as buffer:
        shutil.copyfileobj(predict_file, buffer)
    with st_stdout('info'):
        predict([field], "to_predict.pdf")