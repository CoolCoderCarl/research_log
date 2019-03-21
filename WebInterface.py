from click import echo
from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField, form, RadioField

# App config.
# DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '123'


class ReusableForm(Form):
    login = TextField('Login:', validators=[validators.required()])
    email = TextField('Email:', validators=[validators.required(), validators.Length(min=6, max=35)])
    password = TextField('Password:', validators=[validators.required(), validators.Length(min=3, max=35)])

@app.route("/anotherpage", methods=['GET', 'POST'])
def apage():
    return


@app.route("/", methods=['GET', 'POST'])
def lgnfrm():
    form = ReusableForm(request.form)

    print(form.errors)

    if request.method == 'POST':
        login = request.form['login']
        password = request.form['password']
        email = request.form['email']
        print(login, " ", email, " ", password)
        echo("Login is " + login)
        echo("Email is " + email)
        echo("Pass is " + password)


    if form.validate():
        flash('Hello ' + login)
    else:
        flash('All the form fields are required. ')

    return render_template('hello.html', form=form)


class SimpleForm(Form):
    example = RadioField('Label', choices=[('value','description'),('value_two','whatever')])


if __name__ == "__main__":
    app.run()
