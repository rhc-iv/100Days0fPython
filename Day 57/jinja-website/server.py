#!/usr/bin/env python3

# --- IMPORTS ---

import random
from datetime import date

import requests
from flask import Flask, render_template

# --- CONSTANTS, GLOBALS, ETC. ---

app = Flask(__name__)

MY_NAME = "Robert Carr"


# --- METHODOLOGY ---


@app.route('/')
def home():
    random_number = random.randint(1, 10)
    current_year = date.today().year
    return render_template(
        "index.html",
        num=random_number,
        year=current_year,
        name=MY_NAME,
    )


@app.route("/guess/<name>")
def guess(name):
    gender_url = f"https://api.genderize.io?name={name}"
    gender_response = requests.get(gender_url)
    gender_data = gender_response.json()
    gender = gender_data["gender"]
    age_url = f"https://api.agify.io?name={name}"
    age_response = requests.get(age_url)
    age_data = age_response.json()
    age = age_data["age"]
    return render_template(
        "guess.html",
        person_name=name,
        gender=gender,
        age=age,
    )


@app.route("/blog/<num>")
def get_blog(num):
    blog_url = "https://api.npoint.io/e6e4b41d8c0bef965053"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template(
        "blog.html",
        posts=all_posts,
    )


if __name__ == '__main__':
    app.run(debug=True)
