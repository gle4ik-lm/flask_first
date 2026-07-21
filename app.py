from flask import Flask, render_template, request, flash, redirect, url_for, session
from models import init_db, Company
from actions import *
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'secret_key'

# підключення до БД
init_db()

def is_logged():
    return 'company' in session

def current_company():
    name = session['company']
    return get_company_by_name(name)

@app.route('/', methods=['GET', 'POST'])

@app.route('/products', methods=['GET', 'POST'])
def products():

    session.permanent = True
    if not is_logged():
        return redirect(url_for('login'))

    company = current_company()

    if request.method == 'POST':
        name = request.form.get('name')
        price = request.form.get('price')
        category = request.form.get('category')

        price = float(price)

        if product_exists(name, company.id):
            flash(f'Product {name} already exists!', category='error')
        else:
            add_product(name, price, category, company.id)
            flash(f'Product {name} was added!', category='success')

        return redirect(url_for('products'))


    all_categories = get_categories(company.id)
    choose_category = request.args.get('category', 'all')

    if choose_category == 'all':
        filter_products = get_products(company.id)
    else:

        filter_products = get_products_by_category(choose_category, company.id)

    return render_template('product.html',
                           products=filter_products,
                           categories=all_categories,
                           choose_category=choose_category)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('company')
        password = request.form.get('password')

        if company_exist(name):
            flash(f'Company {name} already exists!')
            return redirect(url_for('register'))
        else:

            print(f"name={name!r}")
            print(f"password={password!r}")
            hash_pass = generate_password_hash(password)
            add_company(name, hash_pass)

            flash(f'Company {name} was created!')
            return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form.get('company')
        password = request.form.get('password')

        if not company_exist(name):
            print(f"name={name!r}")
            print(f"password={password!r}")
            flash(f'Company {name} does not exist!')
            return redirect(url_for('login'))

        company = get_company_by_name(name)

        # перевіряємо хеш паролей, чи співпадають вони
        if not check_password_hash(company.password, password):
            flash(f'Password incorrect!')
            return redirect(url_for('login'))

        # в cookie файл зберігаємо назву компанії
        session['company'] = company.name

        flash(f'Welcome {name}!')
        return redirect(url_for('products'))

    return render_template('login.html')


# динамічне посилання з параметрами <>
@app.route('/products/<name_product>', methods=['GET', 'POST'])
def delete(name_product):
    company = current_company()
    if request.method == 'POST':
        delete_product(name_product, company_id=company.id)
        flash(f'Product {name_product} was deleted!', category='success')
        return redirect(url_for('products'))
    return redirect(url_for('products'))

@app.route('/edit/<name_product>', methods=['GET', 'POST'])
def update(name_product):
    if request.method == 'POST':
        edit_price = request.form.get('edit_price')
        edit_category = request.form.get('edit_category')
        edit_product(name_product, edit_price, edit_category, company_id=session['company'])
        flash(f'Product {name_product} was updated!', category='success')
        return redirect(url_for('products'))



    product = Product.get(Product.name == name_product)
    return render_template('edit.html', price=product.price, category=product.category, name = product.name)



app.run(debug=True)