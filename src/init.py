from flask import Flask

app = Flask(__name__)
app.run(debug=True)


@app.route("/")
def index():
    return "index"


@app.route("/hello")
def hello():
    return "helloworld"
