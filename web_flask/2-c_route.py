#!/usr/bin/python3
"""This script starts a publicly visible Flask server
on port 5000"""

from flask import Flask

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

    st = text
    if '_' in text:
        st = st.replace('_', ' ')

    return f"C {st}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
