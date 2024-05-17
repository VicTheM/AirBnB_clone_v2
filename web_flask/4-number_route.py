#!/usr/bin/python3
"""This script starts a publicly visible Flask server
on port 5000"""

from flask import Flask
from markupsafe import escape

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route("/")
def say_hello():
    """Greetings among men of like minds"""

    return "Hello HBNB!"


@app.route("/hbnb")
def greet():
    """Specific greeting"""

    return "HBNB"



@app.route("/c/<text>")
def greetC(text):
    """Handles url parameters"""

    st = escape(text)
    if '_' in st:
        st = st.replace('_', ' ')

    return f"C {st}"



@app.route("/python")
@app.route("/python/<text>")
def greetP(text='is cool'):
    """Handles url parameters"""

    return f"Python {escape(text).replace('_', ' ')}"



@app.route("/number/<int:n>")
def number(n):
    """Receives n only if it is an integer"""

    return f"{escape(n)} is an integer"



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
