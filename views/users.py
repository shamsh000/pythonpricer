from flask import Flask, Blueprint, request, session, render_template, redirect, url_for
from models.user import User, UserErrors

user_blueprint = Blueprint('user', __name__)


@user_blueprint.route("/register", methods=['GET', 'POST'])
def register_user():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        try:
            User.register_user(email, password)
            session['email'] = email
            return email
        except UserErrors.UserError as e:
            return e.message

    return render_template('/users/register.html')


@user_blueprint.route("/login", methods=['GET', 'POST'])
def login_user():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']

        try:
            if User.is_login_valid(email, password):
                session['email'] = email
                return email
        except UserErrors.UserError as e:
            return e.message

    return render_template('/users/login.html')
