from flask import Blueprint, render_template, session

from utilities.classes.users import User
from utilities.classes.experts import Expert

results = Blueprint('bmiResult', __name__,
                    static_folder='static',
                    static_url_path='/pages/bmiResult',
                    template_folder='templates')


# Routes
@results.route('/BMIResults', methods=['GET', 'POST'])
def results_page():
        bmiRes = session['BMI']
        if bmiRes <= 18.4 and session['Smoker'] == "Yes":
            massage = "You are underweight. It is recommended to consume more calories per day, so that the body gets all the nutrients it needs.In addition, we noticed that you smoker, so we recommend rehab centers in your area to improve your health."
        elif bmiRes <= 18.4 and session['Smoker'] == "No":
            massage = "You are underweight. It is recommended to consume more calories per day, so that the body gets all the nutrients it needs."
        elif 18.4 <= bmiRes <= 24.9 and session['Smoker'] == "Yes":
            massage = "Well done! Your weight is normal,it means you maintain a healthy lifestyle,we recommend to meet our trainers to improve yourself even more.In addition, we noticed that you smoker, so we recommend rehab centers in your area to improve your health."
        elif 18.4 <= bmiRes <= 24.9 and session['Smoker'] == "No":
            massage = "Well done! Your weight is normal,it means you maintain a healthy lifestyle,we recommend to meet our trainers to improve yourself even more."
        elif 25 <= bmiRes <= 29.9 and session['Smoker'] == "Yes":
            massage = "You are over weight.This may be because your daily calorie intake is large relative to the energy your body expends during the day.,we recommend to meet our trainers and nutritionists.In addition, we noticed that you smoker, so we recommend rehab centers in your area to improve your health."
        elif 25 <= bmiRes <= 29.9 and session['Smoker'] == "No":
            massage = "You are over weight.This may be because your daily calorie intake is large relative to the energy your body expends during the day.,we recommend to meet our trainers and nutritionists."
        elif 30 <= bmiRes <= 60 and session['Smoker'] == "Yes":
            massage = "Your weight is significantly higher than the norm. We highly recommend going to one of the doctors from the table below.In addition, we noticed that you smoker, so we recommend rehab centers in your area to improve your health."
        else:
            massage = "Your weight is significantly higher than the norm. We highly recommend going to one of the doctors from the table below."
        session['massage'] = massage
        user = User(name='default', email=session['email'])
        current = user.getUser()
        if current != []:
            current[0] = User(name=session['username'], email=session['email'])
            experts = current[0].getExperts()
        return render_template('BMIResults.html', expertsRes=experts, length=len(experts))





