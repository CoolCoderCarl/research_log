from flask import Flask
from flask import url_for
from flask import request
from flask import render_template
from datetime import datetime

now = datetime.now()
dt_string = now.strftime("%d.%m.%Y_%H.%M.%S")

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Index')

@app.route('/submit', methods=['POST'])
def submit():
    text = request.form['text']
    with open("%s.txt" % dt_string, "w") as text_file:
        text_file.write(text)
    return render_template('index.html', title='Index')


@app.route('/projects')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'


with app.test_request_context():
    print(url_for('index'))


if __name__ == '__main__':

    # app.run(host='0.0.0.0',port=5000, debug=True) # DOCKER
    app.run(port=5000, debug=True)