# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 23:00:15 2020

@author: SAIF
"""

from flask import Flask
app=Flask(__name__)

@app.route('/hello/<name>')
def hello_name(name):
    return 'Hello %s!' % name

if __name__== "__main__":
    app.run(debug=True)