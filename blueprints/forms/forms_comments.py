from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField, SubmitField
from wtforms.validators import DataRequired


class FormAddComment(FlaskForm):
    content = TextAreaField('Description', validators=[DataRequired()])
    submit = SubmitField('Post')


class FormEditComment(FlaskForm):
    content = TextAreaField('Description', validators=[DataRequired()])
    submit = SubmitField('Post')
