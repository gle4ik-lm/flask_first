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

@app.route('/temperature', methods=['GET', 'POST'])
def temperature():
    if request.method == 'POST':
        temp = request.form.get('temp')
        int_temp = int(temp)
        flash(f"F:{(int_temp*1.8)+32}")
        # return redirect(url_for('temperature'))

    return render_template('temperature.html')

app.run(debug=True)