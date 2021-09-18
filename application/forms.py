from flask_wtf import FlaskForm
from wtforms import PasswordField
from wtforms.validators import DataRequired, Length
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.fields.simple import TextField

class LoginForm(FlaskForm):
    password = PasswordField(validators=[DataRequired()])

class PostForm(FlaskForm):
    title = TextField('Title', validators=[DataRequired(), Length(max=120)])
    body = TextField('Body', validators=[DataRequired(), Length(max=1000)])
    # image = FileField('image', validators=[FileRequired(), FileAllowed(['jpg', 'jpeg', 'png', 'webp', 'bmp'], 'Images only')])
