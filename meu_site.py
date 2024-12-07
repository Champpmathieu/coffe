from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/users/<name_user>')
def user(name_user):
    return render_template('usuarios.html', name_user=name_user)


if __name__ == '__main__':
    app.run(debug=True) 