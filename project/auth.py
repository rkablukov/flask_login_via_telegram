# auth.py

from flask import Blueprint, render_template, redirect, url_for, request, flash, current_app, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from .utils import HashCheck
from .models import User
from . import db

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return render_template('login.html')


@auth.route('/tglogin')
def tglogin():
    tg_data = {
        "id": request.args.get('id', None),
        "first_name": request.args.get('first_name', None),
        "last_name": request.args.get('last_name', None),
        "username": request.args.get('username', None),
        "photo_url": request.args.get('photo_url', None),
        "auth_date": request.args.get('auth_date', None),
        "hash": request.args.get('hash', None)
    }
    secret = current_app.config['BOT_TOKEN'].encode('utf-8')

    if not HashCheck(tg_data, secret).check_hash():
        # Hash не верен
        return redirect(url_for('auth.login'))
    else:
        # if this returns a user, then the id already exists in database
        user = User.query.filter_by(id=tg_data['id']).first()

        if not user:  # if a user is found, we update user info
            # create new user with the form data. Hash the password so plaintext version isn't saved.
            user_data = dict((i, tg_data[i]) for i in tg_data if hasattr(User, i))
            new_user = User(**user_data)

            # add the new user to the database
            db.session.add(new_user)
            db.session.commit()

            user = new_user

        # if the above check passes, then we know the user has the right credentials
        login_user(user, remember=True)
        return redirect(url_for('main.profile'))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))
