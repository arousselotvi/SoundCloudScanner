from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class QueryForm(FlaskForm):
    keyWords = StringField('KeyWords')
    genre = StringField('Genre')
    label = StringField('Label')
    submit = SubmitField('Search')