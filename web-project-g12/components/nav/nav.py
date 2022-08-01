from flask import Blueprint, render_template

# nav blueprint definition
nav = Blueprint('nav', __name__,
                static_folder='static',
                static_url_path='/projectNav',
                template_folder='templates')


# Routes
@nav.route('/projectNav')
def nav_func():
    return render_template('projectNav.html')
