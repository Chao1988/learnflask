"""
-------------------------------------------------
   Project Name:  LearnFlask
   File Name:     forms
   Author:        cjiang
   Date:          2020/5/21 7:22 PM
-------------------------------------------------
"""
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')