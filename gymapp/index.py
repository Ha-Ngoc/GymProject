from flask import render_template, request, redirect
from flask_login import logout_user, login_user, current_user

from gymapp import app, login_manager, dao


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login_view():
    return render_template('login.html')

@app.route('/login', methods=['post'])
def login_process():
    username = request.form.get('username')
    password = request.form.get('password')

    u = dao.authenticate(username, password)
    if u:
        login_user(user=u)
    return redirect('/admin')


@app.route('/logout')
def logout_process():
    logout_user()
    return redirect('/login')

@login_manager.user_loader
def get_account(id):
    return dao.get_account_by_id(id)
@app.route('/register')
def register_view():
    return render_template('register.html')

if __name__ == '__main__':
    with app.app_context():
        from gymapp import admin
        app.run(debug=True)