from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class Userinput(FlaskForm):
    question = StringField('question',
                           validators=[DataRequired(), Length(min=2, max=20)]
                           )