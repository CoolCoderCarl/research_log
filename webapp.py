import os
from datetime import datetime

from flask import Flask, render_template, request, url_for

dt_file_name = datetime.now().strftime("%d.%m.%Y_%H.%M.%S")

app = Flask(__name__)

RESEARCH_LOGS_PATH = "research_logs"
try:
    os.makedirs(RESEARCH_LOGS_PATH)
except OSError:
    pass


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", title="index")


@app.route("/submit", methods=["POST"])
def submit():
    text = request.form["text"]
    # Disable button submit if text is empty ?
    if text == "":
        return render_template("index.html", title="index")
    else:
        with open(f"{RESEARCH_LOGS_PATH}/entry-{dt_file_name}.txt", "w") as text_file:
            text_file.write(text)
        return render_template("index.html", title="index")


@app.route(f"/{RESEARCH_LOGS_PATH}", defaults={"req_path": ""})
@app.route("/<path:req_path>")
def files(req_path):
    base_dir = RESEARCH_LOGS_PATH
    abs_path = os.path.join(base_dir, req_path)
    list_files = os.listdir(abs_path)
    return render_template("files.html", files=list_files)


@app.route(f"/{RESEARCH_LOGS_PATH}/<path:filename>")
def read(filename):
    with open(f"{RESEARCH_LOGS_PATH}/{filename}", "r") as f:
        return render_template(
            "content.html", filename=filename, text_from_file=f.read()
        )


@app.route("/about")
def about():
    return render_template("about.html")


with app.test_request_context():
    print(url_for("index"))


if __name__ == "__main__":
    # app.run(host="0.0.0.0", port=5000, debug=True)  # DOCKER
    app.run(port=5000, debug=True)
