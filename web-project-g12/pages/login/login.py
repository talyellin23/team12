from flask import Blueprint, render_template, request, session, redirect, url_for
from utilities.classes.users import User

# Login blueprint definition
login = Blueprint('login', __name__,
                  static_folder='static',
                  static_url_path='/pages/login',
                  template_folder='templates')


@login.route('/Login', methods=['GET', 'POST'])
def log_in_func():
    message_not_post = ''
    if request.method == "POST":
        password = request.form['psw']
        email = request.form['email']
        user = User(name='default', email=email, password=password)
        name = user.getName(email)
        login_bl = user.login()
        if login_bl == 'Login Successfully':
            session['username'] = name
            session['email'] = email
            session['password'] = password
            session['Area'] = 'Israel'
            session['login'] = True
            return redirect('/HomePage')
        else:
            return render_template('Login.html', message3=login_bl)
    return render_template('Login.html', message3=message_not_post)


@login.route('/logout_func', methods=['GET', 'POST'])
def logout_func():
    session['login'] = False
    session.clear()
    return redirect(url_for('homepage.index'))

