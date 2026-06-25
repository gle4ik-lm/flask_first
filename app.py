from flask import Flask, render_template, request, redirect, flash, url_for

app = Flask(__name__)
app.secret_key = '***'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')


        flash(f'Hello, {name}!')

        return redirect(url_for('index'))
    return render_template('index.html')

app.run(debug=True)