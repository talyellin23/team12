from flask import Blueprint, render_template, redirect, url_for

# homepage blueprint definition
homepage = Blueprint('homepage', __name__,
                     static_folder='static',
                     static_url_path='/HomePage',
                     template_folder='templates')


# Routes
@homepage.route('/')
@homepage.route('/HomePage')
def index():
    return render_template('HomePage.html')


@homepage.route('/HomePage')
def redirect_homepage():
    return redirect(url_for('homepage.index'))
