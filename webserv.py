import flask
import sys
import PIL as pil
from werkzeug.utils import secure_filename
app = flask.Flask(__name__, template_folder="sites")
app.config.update(UPLOAD_FOLDER="src")
@app.route("/<url>")
def link(url):
    #print(url)
    try:
        if url == "index" or url == "" or url == "sites/index.html":
            return flask.render_template("index.html"), 200
        elif url == "profile" or url == "sites/profile.html":
            return flask.render_template("profile.html"), 200
        elif url == "projects" or url == "sites/projects.html":
            return flask.render_template("projects.html"), 200
        else:
            return open(url).read(), 200
    except:
        return "Could not Load resource", 404
if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)
