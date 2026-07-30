from flask import Blueprint, render_template, request, session, redirect, url_for, flash
from actions import *
from werkzeug.security import generate_password_hash, check_password_hash

auth_bp = Blueprint('auth', __name__, template_folder='templates')


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if is_user_exist(username):
            flash('Username already exists')
            return redirect(url_for('auth.register'))
        else:
            print(request.form)
            print(username)
            print(password)
            hash_pass = generate_password_hash(password)
            add_user(username, hash_pass)
            session['user'] = username
            return redirect(url_for('tea.home'))

    return render_template('auth/register.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if not is_user_exist(username):
            flash('Username does not exist')
            return redirect(url_for('auth.login'))

        user = get_user_by_name(username)

        if not check_password_hash(user.password, password):
            flash(f'Password incorrect!')
            return redirect(url_for('auth.login'))

        session['user'] = user.username
        flash(f'Welcome {username}!')
        return redirect(url_for('tea.home'))
    return render_template('auth/login.html')

@auth_bp.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('auth.login'))

