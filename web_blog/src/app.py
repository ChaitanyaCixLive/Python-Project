from crypt import methods

from flask import Flask
from flask import render_template
from flask import request
from flask import session

from src.common.database import Database
from src.models.user import User

app = Flask(__name__)
app.secret_key= "Bikash"


@app.route('/login')  #www.mysite.com/api
def login_template():
    return render_template('login.html')

@app.route('/register')  #www.mysite.com/api
def regiter_template():
    return render_template('register.html')

@app.before_first_request
def initialize_database():
    Database.initialize()

@app.route('/auth/login', methods=["POST"])
def login_user():
    #request.form has all the data the is sent with the request
    email = request.form['email']
    password = request.form['password']

    if(User.login_valid(email,password)):
        User.login(email)

    return render_template("profile.html", email = session['email'])

@app.route('/auth/register', methods=["POST"])
def register_user():
    email = request.form['email']
    password = request.form['password']

    User.register(email, password)

    return render_template("profile.html", email=session['email'])

@app.route('/blogs/<string:user_id>')
@app.route('/blogs')
def user_blogs(user_id=None):
    if user_id is not None:
        user = User.get_by_id(user_id)
    else:
        user = User.get_by_email(session['email'])

    blogs = user.get_blogs()

    return render_template("user_blogs.html", blogs=blogs, email = user.email)


if __name__ == '__main__':
    app.run(port=4995)