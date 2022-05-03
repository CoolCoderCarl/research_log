import os
from datetime import datetime

from flask import Flask, Response, render_template, request, url_for

dt_file_name = datetime.now().strftime("%d.%m.%Y_%H.%M.%S")

app = Flask(__name__)

research_logs_path = "research_logs"
try:
    os.makedirs(research_logs_path)
except OSError:
    pass


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", title="Index")


@app.route("/time_feed")
def time_feed():
    def generate():
        yield datetime.now().strftime("%d.%m.%Y|%H:%M:%S")

    return Response(generate(), mimetype="text")


@app.route("/submit", methods=["POST"])
def submit():
    text = request.form["text"]
    # TO DO
    # If text empty pass
    with open(
        research_logs_path + "/" + "entry-%s.txt" % dt_file_name, "w"
    ) as text_file:
        text_file.write(text)
    return render_template("index.html", title="Index")


@app.route("/files", defaults={"req_path": ""})
@app.route("/<path:req_path>")
def files(req_path):
    base_dir = research_logs_path
    abs_path = os.path.join(base_dir, req_path)
    list_files = os.listdir(abs_path)
    return render_template("files.html", files=list_files)


@app.route("/files/<path:filename>")
def read(filename):
    with open(research_logs_path + "/" + filename, "r") as f:
        return render_template(
            "content.html", filename=filename, text_from_file=f.read()
        )


@app.route("/about")
def about():
    return render_template("about.html")


with app.test_request_context():
    print(url_for("index"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)  # DOCKER
    # app.run(port=5000, debug=True)
