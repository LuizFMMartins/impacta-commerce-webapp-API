from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_wold():

    return "<p>Hello , Wold!</p>"
