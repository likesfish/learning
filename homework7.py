from flask import Flask

app = Flask(__name__)

@app.route("/")
def homepage():
    sentence = "Once I needed to be in a group and didn't have any <a href='/fish'>fish</a>"
    return sentence

@app.route("/fish")
def fish():
    return "fish live underwater"
