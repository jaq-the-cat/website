from flask import render_template, request, redirect, url_for, Blueprint
from flask_login import login_user
from flask_login.utils import logout_user
from application.jaqi import Jaqi
from application import app
from application.forms import LoginForm

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.post('/signin')
def signin():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        pw = login_form.password.data;
        if pw == Jaqi.pw:
            login_user(Jaqi, True)
            return redirect(url_for('index.index'))
    return redirect(url_for('index.index'))

@bp.get('/signout')
def signout():
    logout_user()
    return redirect(url_for('index.index'))

app.register_blueprint(bp)
