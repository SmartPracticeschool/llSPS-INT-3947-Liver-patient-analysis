# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 23:02:01 2020

@author: SAIF
"""

from flask import Flask
app=Flask(__name__)

@app.route('/flask')
def hello_flask():
    return 'Hello flask'


@app.route('/python/')
def hello_python():
    return 'Hello python'

if __name__== "__main__":
    app.run(debug=True)