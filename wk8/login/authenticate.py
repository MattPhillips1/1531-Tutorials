from flask import Flask, redirect, request, render_template, url_for
from flask_login import LoginManager,login_user, current_user,
login_required, logout_user
from model import User
from server import app,login_manager


def check_password(user_id, password):
    """
    Authenticates a password and
    uses the login_user function to tell flask-login who
    the new user is
    """
    if password == "admin_password":
        user = get_user(user_id)
        login_user(user)
        return True
    return False


def get_user(user_id):
    """
    Your get user should get user details from the database
    """
    return User(user_id, "Matt")


@login_manager.user_loader
def load_user(user_id):
    """
    Allows flask-login to fetch the current_user
    """
    # get user information from db
    user = get_user(user_id)
    return user


@app.route('/',methods=["GET","POST"])
def login():
    if request.method == "POST":
        user_id = int(request.form["zid"])
        password = request.form["password"]
        if check_password(user_id, password):
            return redirect(url_for('index'))
    return render_template("basic_login.html")


@app.route('/index')
@login_required
def index():
    """
    Users are only allowed to get to this stage if they have been successfully logged in
    by flask-login
    """
    return render_template("logged.html")


@app.route('/logout')
def logout():
    """
    Logs the user out so the @login_required decorator will fail
    """
    logout_user()
    return redirect(url_for('login'))


if __name__=="__main__":
    app.run(debug=True)
