import sqlite3
from flask import Flask, request, render_template, flash, redirect

app = Flask(__name__)
app.secret_key = '***'

@app.route('/', methods=['GET', 'POST'])
def index():
    connection = sqlite3.connect('wishlist.db')
    cursor = connection.cursor()

    cursor.execute('''

    CREATE TABLE IF NOT EXISTS wishlist(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT
    )
    ''')

    if request.method == 'POST':
        wish = request.form.get('wish')
        if wish is None or wish == '':
            flash("Порожній подарунок не можна додати!")
        else:
            cursor.execute("INSERT INTO wishlist (title) VALUES (?)", (wish,))
            connection.commit()
            flash("Подарунок додано!")
            return redirect("/")

    search_wish = request.args.get("get_wish")

    if search_wish:
        cursor.execute(
            "SELECT * FROM wishlist WHERE title = ?",
            (search_wish,)
        )

        row = cursor.fetchone()

        if row is None:
            flash("Такого подарунка немає.")
        else:
            flash("Такий подарунок вже є.")
    cursor.execute("SELECT * FROM wishlist")
    wishes = cursor.fetchall()
    return render_template('index.html', wishes=wishes)


    connection.close()







app.run(debug=True)