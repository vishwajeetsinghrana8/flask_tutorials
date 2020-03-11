from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField,DateTimeField,
                    RadioField,SelectField,TextField,TextAreaField,
                    SubmitField)
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = 'vishwajeet'

class Infoform(FlaskForm):
    breed = StringField('What type of breed are you?',validators=[DataRequired()])
    mood = RadioField('Please select your choose:', choices=[('mood_one','Happy'),('mood_two','Excited')])
    food_choice = SelectField(u'Pick your choice:',choices=[('chi','Chicken'),('fish','Fish'),
                                                            ('Veg','Grass')])
    feedback = TextAreaField()
    submit = SubmitField('Submit')

@app.route('/', methods=['GET','POST'])
def index():
    form = Infoform()

    if form.validate_on_submit():

        session['breed'] = form.breed.data
        session['mood'] = form.mood.data
        session['food'] = form.food_choice.data
        session['feedback'] = form.feedback.data

        return redirect(url_for('thankyou'))

    return render_template('index.html', form=form)

@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

if __name__ == '__main__':
    app.run(debug=True)
