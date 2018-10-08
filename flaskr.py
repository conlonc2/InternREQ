'''Flask server to handle routing for InternREQ.com. '''

'''
Authors:
    Tom Birmingham
    Christopher Conlon
    Daniel G.
    Davis Jaekle
    Mohamad M.
'''

from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)


@app.route('/')
def landing():
    return render_template('landingPage.html', title='InternREQ')


@app.route('/login')
def login():
    return render_template('login.html', title="Login")

# This method will eventually post credentials to databse
# -->Credential's fail: push error message
# -->Credential's pass: push user's dash


@app.route('/login', methods=['POST'])
def login_foward():
    user_type = 'Faculty'
    return render_template('dashboard.html', user=user_type, title="Login")


@app.route('/registration')
def registration():
    return render_template('registration.html', title="Registration")


@app.route('/registration', methods=['POST'])
def registrationPost():
    # All variables must be checked against database and be INSERT'ed into...
    firstName = request.form['firstName']
    lastName = request.form['lastName']
    user = request.form['User']
    verify = request.form['verificationKey']
    pswrd = request.form['password']
    confirm = request.form['re-enter']
    email = request.form['Email']

    if(pswrd != confirm):
        return (render_template('registration.html', title='Login') + "<script>alert('Passwords do not match');</script>")

    return ("<h1>" + firstName + " " + lastName + " " + user + " " + verify + " " + email + " " + pswrd + " " + confirm + " " + "</h1>")


# START: Temporary code for testing how to foward based on user input
'''
    This code will eventually turn into a connection to the database when a user presses login from login html.
    
    When the login button is pushed and the form is submited the dashboard() function is called to route user to
        the appropriate page based on what WILL be returned from the user_type column in or database.
'''


@app.route('/dashboard')
def foward_dash():
    return ('<form action="" method="POST"><input<label>Student <input type="radio" name="user" value="Student"></label></br>'
            '<label>Faculty: <input type="radio" name="user" value="Faculty"></label></br>'
            '<label>Employer: <input type="radio" name="user" value="Sponsor"></label></form></br>'
            '<button type="submit">Submit</button>')


# END: Temporary code for testing how to foward based on user input

'''
Based on the user_type returned from database query:
 foward user to appropriate dashboard
'''


@app.route('/dashboard', methods=['POST'])
def dashboard():
    user_type = request.form['user']
    if(user_type == 'Faculty'):
        return ('<h1>Admin dashboard</h1>')

    elif(user_type == 'Sponsor'):
        return ('<h1>Sponsor dashboard</h1>')

    elif(user_type == 'Student'):
        return '<h1>Student dashboard</h1>'


if (__name__ == "__main__"):
    app.run(host='0.0.0.0', port=8080, debug=True)
