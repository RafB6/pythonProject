from flask import Flask

app = Flask(__name__)

@app.route("/")
def firstTestPage():
    return "<p>Skibidi </p>"