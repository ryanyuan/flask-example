from flask import abort, render_template

from . import home
from logic.logic import Logic


@home.route('/')
def homepage():
    """
    Render the homepage template on the / route
    """
    a = Logic()
    print(a.run())
    return render_template('home/index.html', title="Welcome")
