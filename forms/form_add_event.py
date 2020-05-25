from flask_wtf import FlaskForm
from wtforms.fields import StringField, FileField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, ValidationError

from werkzeug.utils import secure_filename

from blueprints.macros.convert_ru_to_eng import convert_ru_to_eng


class FormAddEvent(FlaskForm):
    address = StringField('Approximate address', validators=[DataRequired()])
    content = TextAreaField('Description', validators=[DataRequired()])
    photo = FileField('Photo')
    submit = SubmitField('Post')

    def validate_photo(self, field):
        if field.data:
            filename = secure_filename(convert_ru_to_eng(field.data.filename))
            if filename.rsplit('.', 1)[1] not in ('png', 'jpeg', 'jpg'):
                raise ValidationError("Invalid extension for photos, use .png or. jpeg(.jpg)")
