from flask import Blueprint, render_template, request, session
from utilities.classes.users import User

# Login blueprint definition
profile = Blueprint('profile', __name__,
                    static_folder='static',
                    static_url_path='/profile.py',
                    template_folder='templates')


# Routes
@profile.route('/UserProfile')
def profile_func():
    return render_template('UserProfile.html')


@profile.route('/updateProfile_func', methods=['GET', 'POST'])
def registering():
    message4 = ''
    if request.method == 'POST':
        email = request.form['currentEmail']
        if session['email'] == email:
            if request.form['psw'] != '':
                password = request.form['psw']
                password2 = request.form['psw-repeat']
                if password != password2:
                    message4 = 'Please make sure the passwords are identical!'
                else:
                    session['password'] = password
                    if request.form['PhoneNum'] != '':
                        phone = request.form['PhoneNum']
                        if request.form['RegName'] != '':
                            name = request.form['RegName']
                            session['username'] = request.form['RegName']
                            user = User(name, email, phone, password=password)
                            message4 = 'User name, phone and password updated successfully!'
                        else:
                            user = User(session['username'], email, phone, password=password)
                            message4 = 'User name and phone updated successfully!'
                    else:
                        if request.form['RegName'] != '':
                            name = request.form['RegName']
                            session['username'] = request.form['RegName']
                            user = User(name, email, password=password)
                            message4 = 'User name and password updated successfully!'
                        else:
                            user = User(session['username'], email, password=password)
                            message4 = 'Password updated successfully!'
            else:
                if request.form['PhoneNum'] != '':
                    phone = request.form['PhoneNum']
                    if request.form['RegName'] != '':
                        name = request.form['RegName']
                        session['username'] = request.form['RegName']
                        user = User(name, email, phone, password=session['password'])
                        message4 = 'User name and phone updated successfully!'
                    else:
                        user = User(session['username'], email, phone, password=session['password'])
                        message4 = 'Phone updated successfully!'
                else:
                    if request.form['RegName'] != '':
                        name = request.form['RegName']
                        session['username'] = request.form['RegName']
                        user = User(name, email, password=session['password'])
                        message4 = 'User name updated successfully!'
                    else:
                        user = User(session['username'], email, password=session['password'])
            if message4 != 'Please make sure the passwords are identical!':
                user.updateUser()
        else:
            message4 = 'Please put registered Email'
            return render_template('UserProfile.html', message4=message4)

    return render_template('UserProfile.html', message4=message4)


@profile.route('/delete_func', methods=['GET', 'POST'])
def delete_func():
    if request.method == "POST":
        user_email = request.form['currentEmail']
        if session['email'] == user_email:
            password = request.form['psw']
            user = User(password, user_email)
            current = user.getUser()
            if current != []:
                current_row = current[0]
                if current_row.Email == user_email and password == current_row.Password:
                    user.deleteUser()
                    message_for_user = 'User deleted!'
                    session['login'] = False
                    session.clear()
                    return render_template('HomePage.html', message5=message_for_user)
            else:
                message_for_user = 'Please make sure the information is accurate!'
                return render_template('UserProfile.html', message5=message_for_user)
        else:
            message_for_user = 'You have to enter your registered email to delete!'
            return render_template('UserProfile.html', message5=message_for_user)
