from flask import render_template, Blueprint
from application import app
from application.forms import LoginForm

bp = Blueprint('index', __name__)

@bp.get('/')
def index():
    login_form = LoginForm()
    return render_template('blog.html', title="Blog", lf=login_form)

app.register_blueprint(bp)
