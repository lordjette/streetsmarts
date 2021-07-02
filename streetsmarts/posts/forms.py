from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(message='The field is required')])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')
