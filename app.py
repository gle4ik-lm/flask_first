from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = '***'


products = {

    }

@app.route('/', methods=['GET', 'POST'])

@app.route('/product', methods=['GET', 'POST'])
def product():

    if request.method == 'POST':
        name = request.form.get('name')
        price = request.form.get('price')
        category = request.form.get('category')

        price = float(price)

        if name in products:
            flash('Product name already exists')
        else:
            products.update({name: {'price': price, 'category': category}})
            flash('Product added successfully')
        return redirect(url_for('product'))

    return render_template('product.html', products=products)

@app.route('/delete/<name_product>')
def delete(name_product):
    products.pop(name_product)
    flash(f'Product {name_product} was deleted!')

    return redirect(url_for('product', products=products))

@app.route('/edit/<name_product>', methods=['GET', 'POST'])
def update(name_product):
    if request.method == 'POST':
        edit_price = request.form.get('edit_price')
        edit_category = request.form.get('edit_category')



        products.update({name_product: {'price': edit_price, 'category': edit_category}})


        return redirect(url_for('product', products=products))

    product = products.get(name_product)
    old_price = product['price']
    old_category = product['category']

    return render_template('edit.html',price=old_price, category=old_category
    )

app.run(debug=True)