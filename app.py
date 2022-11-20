from flask import Flask

flaskapp = Flask(__name__)

@flaskapp.route("/")
def home():
    return {"status":"working"}
