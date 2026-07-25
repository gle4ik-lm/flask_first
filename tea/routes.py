from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from actions import *
tea_bp = Blueprint('tea_bp', __name__)

def is_logged():
    return 'user' in session

def current_user():
    name = session['user']
    return get_user_by_name(name)


@tea_bp.route('/', methods=['GET', 'POST'])
@tea_bp.route('/home', methods=['GET', 'POST'])
def home():
    session.permanent = True

    if not is_logged():
        return redirect(url_for('auth.login'))


    user = current_user()
    print(user)

    if request.method == 'POST':
        title = request.form.get('title')
        province= request.form.get('province')
        type = request.form.get('type')

        if is_tea_exist(title):
            flash('tea already exist')
        else:
            add_tea(title, province, type)

    return render_template("MainPage.html")
