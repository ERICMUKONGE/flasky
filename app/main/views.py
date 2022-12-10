
from datetime import datetime
from flask import render_template, session, redirect, url_for
from . import main
# from .forms import NameForm
from flask_wtf import FlaskForm
from .. import db
from ..models import User, NameForm

@main.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        # ...
        return redirect(url_for('.index'))
    return render_template('index.html',
                           form=form, name=session.get('name'),
                           known=session.get('known', False),
                           current_time=datetime.utcnow())    