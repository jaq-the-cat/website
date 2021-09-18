from application.models import Post
from flask import render_template, Blueprint, url_for, redirect
from application import app
from application.forms import LoginForm, PostForm

bp = Blueprint('index', __name__)

@bp.get('/')
def index():
    login_form = LoginForm()
    post_form = PostForm()
    return render_template('blog.html',
        title="Blog",
        lf=login_form,
        pf=post_form,
        posts=Post.query.all())

@bp.post('/post')
def post():
    post_form = PostForm()
    if post_form.validate_on_submit():
        Post.add(post_form.title.data, post_form.body.data)
    return redirect(url_for('index.index'))

app.register_blueprint(bp)
