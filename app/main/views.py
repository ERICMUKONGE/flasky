
from datetime import datetime
from flask import render_template, session, redirect, url_for
from . import main
from flask_wtf import FlaskForm
from .. import db
from ..models import User

@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html',
                           form=FlaskForm, name=session.get('name'),
                          known=session.get('known', False),
                           current_time=datetime.utcnow())    