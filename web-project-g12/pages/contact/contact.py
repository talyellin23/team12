from flask import Blueprint, render_template, request
from utilities.classes.contactYou import Contact
from datetime import datetime

# catalog blueprint definition
contact = Blueprint('contact', __name__,
                    static_folder='static',
                    static_url_path='/ContactUs',
                    template_folder='templates')


# Routes
@contact.route('/ContactUs')
def contact_page():
    return render_template('ContactUs.html')


@contact.route('/contact_func', methods=['GET', 'POST'])
def contact_func():
    if request.method == 'POST':
        name = request.form['FullName']
        email = request.form['Email']
        phone = request.form['PhoneNumber']
        time = request.form['timeOfContact']
        reason = request.form['reason']
        create = datetime.now()
        mes = Contact(name, email, phone, time, reason, create)
        mes.addContact()
        message6 = 'Thank you for your message, we will contact you soon!'

    return render_template('ContactUs.html', message6=message6)
