from flask import Blueprint, render_template, request, session
from utilities.classes.users import User
from utilities.db.db_manager import DBManager

# register blueprint definition
register = Blueprint('register', __name__,
                     static_folder='static',
                     static_url_path='/Register',
                     template_folder='templates')


# Routes
@register.route('/Register')
def register_func():
    return render_template('Register.html')


@register.route('/registering', methods=['GET', 'POST'])
def registering():
    message2 = ''
    if request.method == 'POST':
        name = request.form['RegName']
        email = request.form['email']
        user1 = User(name, email)
        message2 = user1.searchUser()
        if message2 == 'This user already exist!':
            return render_template('Register.html', message2=message2)
        else:
            password = request.form['psw']
            password2 = request.form['psw-repeat']
            if password != password2:
                message2 = 'Please make sure the passwords are identical!'
            else:
                phone = request.form['PhoneNum']
                birthday = request.form['Bday']
                user = User(name, email, phone, birthday, password)
                user.addUser()
                message2 = 'User added successfully!'
                session['username'] = request.form['RegName']
                session['email'] = email
                session['login'] = True

    return render_template('Register.html', message2=message2)
