import os
from datetime import datetime

from flask import Flask, render_template, request, url_for

now = datetime.now()
dt_string = now.strftime("%d.%m.%Y_%H.%M.%S")

app = Flask(__name__)

log_for_logs_path = "logs_for_logs"
if log_for_logs_path:
    pass
else:
    os.makedirs(log_for_logs_path)


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", title="Index")


@app.route("/submit", methods=["POST"])
def submit():
    text = request.form["text"]
    with open(log_for_logs_path + "/" + "%s.txt" % dt_string, "w") as text_file:
        text_file.write(text)
    return render_template("index.html", title="Index")


@app.route("/projects")
def projects():
    return "The project page"


@app.route("/about")
def about():
    return "The about page"


with app.test_request_context():
    print(url_for("index"))


if __name__ == "__main__":

    app.run(host="0.0.0.0", port=5000, debug=True)  # DOCKER
    # app.run(port=5000, debug=True)