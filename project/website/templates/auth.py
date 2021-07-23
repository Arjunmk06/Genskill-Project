from flask import Blueprint, render_template, request, flash

auth =  Blueprint('auth', __name__)

@auth.route('/login', methods = ['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template('login.html')

@auth.route('/logout')
def logout():
    return render_template('home.html')

@auth.route('/sign-up', methods = ['GET', 'POST'])
def singup():
    if request.method =='POST':
        email = request.form.get('email')
        firstName = request.form.get("firstName")
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        print("ddd")
        #check the user data criteria
        if len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(firstName) < 2:
            flash('First Name must be greater than 1 characters.', category='error')
        elif password1!=password2:
            flash('Password does not match.', category='error')
        elif len(password1) < 7:
            flash('password must be greater than 6 characters.', category='error')
        else:
            ##add the user to database
            flash('Account created ', category='success')
    return render_template('signup.html')