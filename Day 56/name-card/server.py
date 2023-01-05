#!/usr/bin/env python3

# --- IMPORTS ---

from flask import Flask, render_template

# --- CONSTANTS, GLOBALS, ETC. ---

app = Flask(__name__)

# --- METHODOLOGY ---


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)