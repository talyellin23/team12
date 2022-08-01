from flask import Blueprint, render_template

# footer blueprint definition
footer = Blueprint('footer', __name__,
                   static_folder='static',
                   static_url_path='/projectFooter',
                   template_folder='templates')


# Routes
@footer.route('/projectFooter')
def footer_func():
    return render_template('projectFooter.html')
