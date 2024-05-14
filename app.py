from flask import Flask, render_template, request, redirect, url_for , flash
import pymysql
import secrets
secret_key = secrets.token_hex(16)

application = Flask(__name__)


application.secret_key = secret_key
# MySQL Configuration

db_host = 'localhost'
db_user = 'username'
db_password = 'password'
db_name = 'databasename'

def create_connection():
    return pymysql.connect(host=db_host, user=db_user, password=db_password, db=db_name)

# Route for the login page
@application.route('/')
def login():
    
    return render_template('login.html')
    

# Route to handle login form submission, messages=messages
@application.route('/validate_login', methods=['POST'])
def validate_login():
    username = request.form['username']
    password = request.form['password']

    # Connect to the database
    connection = create_connection()
    cursor = connection.cursor()

    # Query to check if the username and password match
    query = "SELECT * FROM users WHERE username=%s AND password=%s"
    cursor.execute(query, (username, password))
    user = cursor.fetchone()

    # Close database connection
    cursor.close()
    connection.close()

    # If a user is found, redirect to the next page, otherwise, show an error message
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

        connection = create_connection()
        cursor = connection.cursor()

        # Check if the username or email is already registered
        cursor.execute('SELECT * FROM users WHERE username=%s OR email=%s', (username, email))
        user = cursor.fetchone()

        if user:
            flash('Username or email already in use. Please choose another.', 'error')
        else:
            # Insert the new user into the database
            cursor.execute('INSERT INTO users (username, email, password) VALUES (%s, %s, %s)',
                           (username, email, password))
            connection.commit()
            flash('Registration successful. You can now log in.', 'success')


            return redirect(url_for('login'))

    return render_template('register.html')


@application.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('home.html')
    

if __name__ == '__main__':
    application.run(debug=True)