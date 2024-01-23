# -*- coding: utf-8 -*-

from flask import Flask, request
import pandas as pd
import numpy as np
import pickle
import flasgger
from flasgger import Swagger


app = Flask(__name__)  #this is ->at which point you want to start this application
Swagger(app)   # It is giving indication to flask to generate UI part

pickle_in=open('classifier.pkl','rb')
classifier=pickle.load(pickle_in)

@app.route('/')  # This decorater. This is welcome page or root page
def welcome():
    return "Welcome All!!"

@app.route('/predict',methods=["GET"]) # api with "Gate" method
def predict_note_authentication():
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
    variance = request.args.get('variance')
    skewness = request.args.get('skewness')	
    curtosis = request.args.get('curtosis')	
    entropy = request.args.get('entropy')
    
    prediction = classifier.predict([[variance, skewness, curtosis, entropy]])
    return "The Predicted Value is" + str(prediction)

'''
@app.route('/predict_file',methods=["POST"]) # api with "POST" method
def predict_note_file():
    #df_test = pd.read_csv(request.fipredict_TestFileles.get("TestFile"))
    #prediction = classifier.predict(df_test)
    
    #return "The Predicted Value for the TestFile.csv" + str(list(prediction))
    df_test=pd.read_csv(request.files.get("file"))
    print(df_test.head())
    prediction=classifier.predict(df_test)
    
    return str(list(prediction))
'''

@app.route('/predict_file',methods=["POST"])
def predict_note_file():
    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:
      - name: file
        in: formData
        type: file
        required: true
      
    responses:
        200:
            description: The output values
        
    """
    df_test=pd.read_csv(request.files.get("file"))
    print(df_test.head())
    prediction=classifier.predict(df_test)
    
    return str(list(prediction))


if __name__=='__main__':
    app.run()               #Flask application will start executing from this