import json
from flask import Blueprint, render_template, request, redirect, url_for, session
# from pages.bmiResult.results import results_func
from utilities.classes.users import User

bmi = Blueprint('bmiPage', __name__,
                static_folder='static',
                static_url_path='/pages/bmiPage',
                template_folder='templates')

userArea = ''


# Routes
@bmi.route('/BMIPage', methods=['GET', 'POST'])
def bmi_func():
    return render_template('BMIPage.html')


@bmi.route('/getData', methods=['GET', 'POST'])
def bmi_page():
    if request.method == 'GET':
        age = int(request.args['Age'])
        weight = int(request.args['Weight'])
        height = int(request.args['Height'])
        gender = request.args['Gender']
        smoker = request.args['Smoker']
        food = request.args['Answer2']
        bmiUser = float((weight / ((height / 100) ** 2)))
        if gender != 'Female':
            BmrMen = float(88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age))
            bmr = BmrMen
        else:
            BmrWomen = float(447.593 + (9.247 * weight) + (3.098 * height) - (4.33 * age))
            bmr = BmrWomen
        user = User(name=session['username'], email=session['email'])
        result = user.getUser()
        for user in result:
            if result[0].Email == user.Email:
                result[0] = User(session['username'], session['email'], None, None, None, age, weight, height, gender,
                                 smoker, bmiUser, bmr, session['Area'])
                result[0].updateBMI()
                session['BMI'] = float(round(bmiUser, 2))
                session['BMR'] = float(round(bmr, 2))
                session['Smoker'] = smoker
                session['food'] = food
                # session['Area'] = 'Israel'
                return redirect('/BMIResults')
    return render_template('BMIPage.html')


@bmi.route('/getResults', methods=['GET', 'POST'])
def bmi_res():
    return redirect('/BMIResults')


@bmi.route('/getLocation', methods=['GET', 'POST'])
def location():
    return redirect(url_for('request.referrer'))


@bmi.route('/ProcessArea/<string:area>', methods=['POST'])
def ProcessArea(area):
    area = json.loads(area)
    session['Area'] = area
    print(area)
    return redirect(request.referrer)


@bmi.route('/ProcessBoolean/<string:bol>', methods=['POST'])
def ProcessBoolean(bol):
    global boolean
    boolean = json.loads(bol)
    print()
    print(boolean)
    if boolean == '':
        session['Area'] = 'Israel'
    return render_template('BMIPage.html')
