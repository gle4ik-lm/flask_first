from flask import Blueprint, render_template, session, request, redirect, url_for, flash
from actions import *
from models import User

user_bp = Blueprint('user_page', __name__, template_folder='templates')

def is_logged():
    return 'user' in session

def current_user():
    name = session['user']
    return get_user_by_name(name)

@user_bp.route('/user_page', methods=['GET', 'POST'])
def user_tea_list():
    user = current_user()
    if request.method == 'POST':
        return render_template("user_page/user_page.html")

    all_types = get_types_for_page(user.id)

    choose_category = request.args.get('type', 'all')

    if choose_category == 'all':
        filter_teas = get_teas_for_user(user.id)
    else:
        filter_teas = get_tea_by_type_for_user(choose_category, user.id)

    return render_template('user_page/user_page.html', teas=filter_teas,
                           type=all_types,
                           choose_category=choose_category
                           )

@user_bp.route('/<name_tea>', methods=['GET', 'POST'])
def add_tea_in_page(name_tea):
    print("ROUTE WORKS")
    user = current_user()
    info = get_tea_info(name_tea)
    print(info)
    if info.title in UserTeaPage:
        flash('tea already exist')
    else:
        add_tea_in_list(info.title, info.province, info.type, user.id)
    return redirect(url_for('user_page.user_tea_list'))

@user_bp.route('/delete/<name_tea>', methods=['GET', 'POST'])
def delete_tea_in_page(name_tea):
    user = current_user()
    delete_tea(name_tea, user.id)
    return redirect(url_for('user_page.user_tea_list'))