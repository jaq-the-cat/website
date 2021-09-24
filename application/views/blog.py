from application.models import Post
from flask import render_template, Blueprint, url_for, redirect
from application import app
from application.forms import LoginForm, PostForm

bp = Blueprint('index', __name__)

@bp.get('/blog')
def blog():
    return render_template('blog.jinja2',
        title="Blog",
        lf=LoginForm(),
        pf=PostForm(),
        posts=Post.query.all(),
        selected=['selected', '', ''])

@bp.get('/about')
def about():
    return render_template('about.jinja2',
        title="About",
        lf=LoginForm(),
        pf=PostForm(),
        selected=['', 'selected', ''])

@bp.get('/contact')
def contact():
    return render_template('contact.jinja2',
        title="Contact",
        lf=LoginForm(),
        pf=PostForm(),
        selected=['', '', 'selected'])

@bp.post('/post')
def post():
    post_form = PostForm()
    if post_form.validate_on_submit():
        Post.add(post_form.title.data, post_form.body.data)
    return redirect(url_for('index.blog'))

app.register_blueprint(bp)
