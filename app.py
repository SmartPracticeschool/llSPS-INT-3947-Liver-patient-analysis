# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 18:27:56 2020

@author: SAIF
"""

import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import joblib

app = Flask(__name__)
model = joblib.load("liver.sav")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/y_predict',methods=['POST'])
def y_predict():
    '''
    For rendering results on HTML GUI
    '''
    x_test = [[x for x in request.form.values()]]
    print(x_test)
    if x_test[0][1]=="Male":
        x_test[0][1]=0
    else:
        x_test[0][1]=1
    x_test=[[int(x) for x in x_test[0]]]
    prediction = model.predict(x_test)
    print(prediction)
    output=prediction[0]
    if output==1:
        test="You are infected, please consult doctor!"
    else:
        test="You are fine!!"
    return render_template('index.html', prediction_text=test)

@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model.y_predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)