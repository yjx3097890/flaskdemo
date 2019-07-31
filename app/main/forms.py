from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileRequired


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    photo = FileField(validators=[FileRequired()]) 
    submit = SubmitField('Submit')
