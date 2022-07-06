import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

def main():
    app.run(
        host=os.environ.get("HOST_NAME", "0.0.0.0"),
        port=int(os.environ.get("HOST_PORT", 11103)),
    )