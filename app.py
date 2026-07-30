from flask import Flask
from models import init_db


from tea.routes import tea_bp
from auth.routes import auth_bp
from user_page.routes import user_bp

app = Flask(__name__)
app.secret_key = 'secret_key'
init_db()

app.register_blueprint(tea_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(user_bp)
app.run(debug=True)