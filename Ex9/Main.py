from flask import Flask, render_template, flash, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField

app = Flask(__name__)

app.config['SECRET_KEY'] = 'knowledgeshelf'

class SimpleForm(FlaskForm):

    submit = SubmitField("Click Me")

@app.route('/', methods=['GET','POST'])
def index():
    form = SimpleForm()

    if form.validate_on_submit():
        flash("You just clicked the button!!!")

        return redirect(url_for('index'))
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
