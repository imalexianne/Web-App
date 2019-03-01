from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required
from wtforms.fields.html5 import DateField


class PitchForm(FlaskForm):
    category = StringField('Pitch category',validators=[Required()])
    description_path = TextAreaField('post a pitch')
    posted = DateField('date and time')

    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    description_all = TextAreaField('write a comment')
    submit = SubmitField('Submit')