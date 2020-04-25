from flask import Flask

# name= app.py
app = Flask(__name__)


@app.route('/')
def hello_world():
    return "<h1>Hello, World!</h1>"
