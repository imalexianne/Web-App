from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required


# class ReviewForm(FlaskForm):

#     title = StringField('Review title',validators=[Required()])
#     review = TextAreaField('Movie review', validators=[Required()])
#     submit = SubmitField('Submit')


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class PitchForm(FlaskForm):
    category = StringField('Pitch category',validators=[Required()])
    description_path = TextAreaField('user pitch')
    submit = SubmitField('Submit')


# class PitchForm(FlaskForm):
#     category = StringField('Pitch category',validators=[Required()])
#     description = TextAreaField('user pitch')
#     submit = SubmitField('Submit')
