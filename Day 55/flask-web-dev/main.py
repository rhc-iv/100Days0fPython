#!/usr/bin/env python3

# --- IMPORTS ---

from flask import Flask

# --- CONSTANTS & GLOBALS ---

app = Flask(__name__)


def make_bold(func):
    def wrapper(*args, **kwargs):
        return '<b>' + func(*args, **kwargs) + '</b>'
    return wrapper


def make_emphasis(func):
    def wrapper(*args, **kwargs):
        return '<em>' + func(*args, **kwargs) + '</em>'
    return wrapper


def make_underlined(func):
    def wrapper(*args, **kwargs):
        return '<u>' + func(*args, **kwargs) + '</u>'
    return wrapper


# --- METHODOLOGY ---


@app.route("/")
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1> ' \
           '<p>This is a paragraph.</p>'\
           '<img src="https://media.giphy.com/media/273P92MBOqLiU/giphy.gif">'


@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def say_bye():
    return 'Bye!'


@app.route("/<name>")
def greet(name):
    return f"Hello {name}!"


if __name__ == '__main__':
    app.run(debug=True)
