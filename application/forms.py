from flask_wtf import FlaskForm
from wtforms import PasswordField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    password = PasswordField(validators=[DataRequired()])
