from flask import Flask, render_template, redirect, url_for, request, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "90234890")
login_manager = LoginManager(app)
login_manager.login_view = 'login'

users = {
    "usuario1":{"id": 1, "username": "usuario1", "password": "senha123" },
}

class User(UserMixin):
    def __init__(self, id, username):
        self.id = id
        self.username = username

@login_manager.user_loader
def load_user(user_id):
    for username, data in users.items():
        if data['id'] == int(user_id):
            return User(data['id'], username)
    return None


@app.route('/')
@login_required
def home():
    return render_template('home.html', username=current_user.username)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user_data = users.get(username)
    
        if user_data and user_data['password'] == password:
            user = User(user_data['id'], username)
            login_user(user)
            flash('Login Successful!')
            return redirect(url_for('home'))
        else:
            flash('Login error!')

    return render_template('login.html')
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Exit successful!')
    return redirect(url_for('login'))


@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

if __name__ == '__main__':
    app.run(debug=True) 