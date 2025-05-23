from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h4>Hello World!</h4>"