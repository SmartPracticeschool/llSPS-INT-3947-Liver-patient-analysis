# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 21:54:58 2020

@author: SAIF
"""

from flask import Flask
app=Flask(__name__)

@app.route('/')
def hello_world():
    return('Hello Surya')

if __name__== '__main__':
    app.run()  #app.run('debug=true)
    
          
