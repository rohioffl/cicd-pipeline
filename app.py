import os
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask application
application = Flask(__name__)
application.secret_key = os.getenv('SECRET_KEY')

# Configure SQLAlchemy
db_host = os.getenv('DB_HOST')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_name = os.getenv('DB_NAME')

application.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}'
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(application)

# Define User model
class User(db.Model):
    __tablename__ = 'users'  # Specify the table name explicitly
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)

# Routes
@application.route('/')
def login():
    return render_template('login.html')

@application.route('/validate_login', methods=['POST'])
def validate_login():
    username = request.form['username']
    password = request.form['password']

    # Query to check if the username and password match
    user = User.query.filter_by(username=username, password=password).first()

    # If a user is found, redirect to the home page, otherwise, show an error message
    if user:
        return redirect(url_for('home'))
    else:
        error = 'Invalid login credentials. Please try again.'
        return render_template('login.html', error=error)

@application.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # Check if the username or email is already registered
        existing_user = User.query.filter((User.username == username) | (User.email == email)).first()

        if existing_user:
            flash('Username or email already in use. Please choose another.', 'error')
        else:
            # Create a new User object and add it to the database
            new_user = User(username=username, email=email, password=password)
            db.session.add(new_user)
            db.session.commit()
            flash('Registration successful. You can now log in.', 'success')

            return redirect(url_for('login'))

    return render_template('register.html')

@application.route('/home')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    # Set up development environment
    os.environ['FLASK_ENV'] = 'development'

    # Run the application
    application.run(debug=True)
