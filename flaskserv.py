import flask
app = flask.Flask(__name__)

@app.route("/")
def index():
    file = open("index/index.html")
    out = file.read()
    return out
if __name__ == "__main__":
    app.run(port=8080, debug=True)