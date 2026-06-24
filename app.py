from flask import Flask, render_template
import datetime
app = Flask(__name__)
current_time = datetime.datetime.now()
is_open = "11:00:00" < current_time.strftime("%H:%M:%S" ) < "22:00:00"
today = datetime.datetime.now().weekday()
is_friday = True if today == 4 else False



menu = {
"Капучино": 80,
"Лате": 85,
"Еспресо": 60,
"Чізкейк": 120,
"Панкейки": 95
}

@app.route('/')
def index():
    return render_template('index.html', status = is_open)

@app.route('/menu')
def coffee_shop_menu():
    return render_template('menu.html', status = is_friday, menu = menu)

app.run(debug=True)

