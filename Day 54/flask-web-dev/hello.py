#!/usr/bin/env python3

# --- IMPORTS ---

from flask import Flask

# --- CONSTANTS & GLOBALS ---

app = Flask(__name__)

# --- METHODOLOGY ---


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/bye')
def say_bye():
    return 'Bye!'

if __name__ == '__main__':
    app.run()