from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from actions import *

tea_bp = Blueprint('tea', __name__, template_folder='templates')

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
    print(repr(user.username))
    print(user.username == "mamon")
    if request.method == 'POST':
        title = request.form.get('title')
        province= request.form.get('province')
        type = request.form.get('type')

        if is_tea_exist(title):
            flash('tea already exist')
        else:
            print(title)
            print(province)
            print(type)
            add_tea(title, province, type)

    all_types = get_types()

    choose_category = request.args.get('type', 'all')

    if choose_category == 'all':
        filter_teas = get_teas()
    else:
        filter_teas = get_tea_by_type(choose_category)

    return render_template('tea/MainPage.html',  teas=filter_teas,
                                                                  types = all_types,
                                                                  choose_category = choose_category,
                                                                  is_admin=user.username == 'mamon',
                                                                  user=user.username,
                                                                  )

@tea_bp.route('/to_user_page', methods=['GET', 'POST'])
def to_user_page():
    return redirect(url_for('user_page.user_tea_list'))