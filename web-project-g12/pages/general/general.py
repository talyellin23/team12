from flask import Blueprint, render_template

# about blueprint definition
about = Blueprint('about', __name__,
                  static_folder='static',
                  static_url_path='/AboutUs',
                  template_folder='templates')


# Routes
@about.route('/AboutUs')
def about_func():
    return render_template('AboutUs.html')


# Articles blueprint definition
articles = Blueprint('articles', __name__,
                     static_folder='static',
                     static_url_path='/Articles',
                     template_folder='templates')


# Routes
@articles.route('/Articles')
def articles_func():
    return render_template('Articles.html')


# CaloriesPage blueprint definition
calories = Blueprint('calories', __name__,
                     static_folder='static',
                     static_url_path='/CaloriesPage',
                     template_folder='templates')


# Routes
@calories.route('/CaloriesPage')
def calories_func():
    return render_template('CaloriesPage.html')


# FAQ blueprint definition
faq = Blueprint('faq', __name__,
                static_folder='static',
                static_url_path='/FAQ',
                template_folder='templates')


# Routes
@faq.route('/FAQ')
def faq_func():
    return render_template('FAQ.html')
