# Add any form classes for Flask-WTF here
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField
from wtforms.validators import DataRequired, Length, Regexp
from flask_wtf.file import FileAllowed

class MovieForm(FlaskForm):
    title = StringField('Movie Title:',validators=[DataRequired(),Length(max=100)])
    description = TextAreaField('Movie Description:', validators=[DataRequired(),Length(max=500)])
    poster = FileField('Movie Poster:',validators=[FileAllowed('jpg', 'jpeg', 'png'), 'Images Only!'])