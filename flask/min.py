#!/usr/bin/env python3
"""Simple flask app"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_Koech():
    return 'Good Morning Shadrack'