from flask import Flask
from datetime import timedelta


app = Flask(__name__)
app.secret_key = '123'
app.config['SESSION_PERMANENT'] = True
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)

from pages.login.login import login

app.register_blueprint(login)

from pages.register.register import register

app.register_blueprint(register)

from pages.profile.profile import profile

app.register_blueprint(profile)

from pages.homepage.homepage import homepage

app.register_blueprint(homepage)

from pages.general.general import about

app.register_blueprint(about)

from pages.general.general import articles

app.register_blueprint(articles)

from pages.general.general import calories

app.register_blueprint(calories)

from pages.general.general import faq

app.register_blueprint(faq)

from pages.contact.contact import contact

app.register_blueprint(contact)

from pages.bmiPage.bmiPage import bmi

app.register_blueprint(bmi)

from pages.bmiResult.results import results

app.register_blueprint(results)

from pages.menus.menus import menus

app.register_blueprint(menus)

if __name__ == '__main__':
    app.run(debug=True)
