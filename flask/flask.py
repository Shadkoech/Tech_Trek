#!/usr/bin/env python3
"""Simple flask app"""

from flask import Flask

# An instance of flask class is the WSGI application.
app = Flask(__name__)

@app.route('/')
def hello_Koech():
    return 'Good Morning Shadrack'