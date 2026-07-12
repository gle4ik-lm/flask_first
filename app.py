

from flask import Flask, render_template, request, flash, redirect, url_for
from models import init_db
from actions import *

app = Flask(__name__)
app.secret_key = 'secret_key'

# підключення до БД
init_db()


@app.route('/', methods=['GET', 'POST'])
@app.route('/products', methods=['GET', 'POST'])
def products():
    if request.method == 'POST':
        name = request.form.get('name')
        price = request.form.get('price')
        category = request.form.get('category')

        price = float(price)

        if product_exists(name):
            flash(f'Product {name} already exists!', category='error')
        else:
            add_product(name, price, category)
            flash(f'Product {name} was added!', category='success')

        return redirect(url_for('products'))


    all_categories = get_categories()


    choose_category = request.args.get('category', 'all')

    if choose_category == 'all':
        filter_products = get_products()
    else:

        filter_products = get_products_by_category(choose_category)

    return render_template('product.html',
                           products=filter_products,
                           categories=all_categories,
                           choose_category=choose_category)


# динамічне посилання з параметрами <>
@app.route('/delete/<name_product>')
def delete(name_product):
    flash(f'Product {name_product} was deleted!', category='success')

    return redirect(url_for('products'))

@app.route('/edit/<name_product>', methods=['GET', 'POST'])
def update(name_product):
    if request.method == 'POST':
        edit_price = request.form.get('edit_price')
        edit_category = request.form.get('edit_category')
        edit_product(name_product, edit_price, edit_category)
        flash(f'Product {name_product} was updated!', category='success')
        return redirect(url_for('products'))

    product = Product.get(Product.name == name_product)


    return render_template('edit.html',price=product.price, category=product.category)

app.run(debug=True)