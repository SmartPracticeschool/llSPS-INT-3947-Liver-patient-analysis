# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 22:06:15 2020

@author: SAIF
"""

from flask import Flask
app=Flask(__name__)

@app.route('/hello')
def hello():
    return("Hello khashafath")

if __name__== "__main__":
    app.run(debug=True)
