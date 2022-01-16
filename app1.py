import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st
import requests
from PIL import Image

#app=Flask(__name__)
#Swagger(app)

pickle_in = open("model.pkl","rb")
classifier=pickle.load(pickle_in)

#@app.route('/')
def welcome():
    return "Welcome All"

#@app.route('/predict',methods=["Get"])
def predict_note_authentication(variance,skewness,curtosis,entropy):
    
    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: variance
        in: query
        type: number
        required: true
      - name: skewness
        in: query
        type: number
        required: true
      - name: curtosis
        in: query
        type: number
        required: true
      - name: entropy
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """
   
    prediction=classifier.predict([[variance,skewness,curtosis,entropy]])
    print(prediction)
    return prediction



def main():
    st.title("Bank Note Authenticator ")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Bank Authenticator ML App </h2>
    </div>
    <style>
    div.stButton > button:first-child {background-color:tomato; color:#ffffff}
    div.stButton > button:hover {background-color:#00FA9A}
    </style>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    variance = st.text_input("Variance","Enter value")
    skewness = st.text_input("Skewness","Enter value")
    curtosis = st.text_input("Curtosis","Enter value")
    entropy = st.text_input("Entropy","Enter value")
    result=""
    res = ""
    if st.button("Predict"):
        result = predict_note_authentication(variance,skewness,curtosis,entropy)
        if (result == 0):
          res = "Authentic"
        elif(result == 1):
          res = "Not Authentic"
        else:
          st.warning("Please enter proper input ")
          st.info("Please check input format before entering ")
    
        st.success("The predicted output is  {} . It means the Bank Note is {} ".format(result,res))
    with st.expander("Created by"):
      url ='https://drive.google.com/file/d/13hl3HCo6kWQwt003gzJn9biNSniaR2Ap/view?usp=sharing'
      image = Image.open('author.jpeg')
      st.image(image, caption='Author: Venkata Narayana Bommanaboina',width=200, use_column_width='always')
      st.write("Connect me-->[link](https://www.linkedin.com/in/bvnarayana515739)")
      st.write("Source code is availabe [link](https://github.com/venkatanarayana143/Bank-Note-Authentication-ML-App)")
    
if __name__=='__main__':
    main()
    
