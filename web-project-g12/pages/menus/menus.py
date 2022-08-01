from flask import Blueprint, render_template, request, session, redirect, url_for
from utilities.classes.users import User

# Login blueprint definition
menus = Blueprint('menus', __name__,
                  static_folder='static',
                  static_url_path='/pages/menus',
                  template_folder='templates')


@menus.route('/menus', methods=['GET', 'POST'])
def menu_page():
    if session['food'] == 'Vegetarian':
        message11 = 'Vegetarian'
    elif session['food'] == 'Vegan':
        message11 = 'Vegan'
    else:
        message11 = 'eat all'
    return render_template('menus.html', message11=message11)
