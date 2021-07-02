from flask import render_template, url_for, flash, redirect, request, Blueprint, abort
from flask_login import login_user, current_user, logout_user, login_required
from streetsmarts import db, bcrypt
from streetsmarts.models import User, Post
from streetsmarts.users.forms import (RegistrationForm, LoginForm, UpdateAccountForm,
                                   RequestResetForm, ResetPasswordForm)
from streetsmarts.users.utils import save_picture, send_reset_email


users = Blueprint('users', __name__)

#:fire: :fire: :fire: :fire: :fire: :fire: :fire: :fire: :fire: :fire: 

@users.route('/register', methods=['GET', 'POST']) #very important GET or POST METHOD
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    formx = RegistrationForm()
    if formx.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(formx.password.data).decode('utf-8')
        user = User(username=formx.username.data, email=formx.email.data, password= hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')   #flash(f'Account created for {formx.username.data}!', 'success')
        return redirect(url_for('main.login'))
    return render_template('register.html', title = 'Regiter', form = formx)



@users.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data) #checking  password_hash
            next_page = request.args.get('next') #args is dictionary
            return redirect(next_page) if next_page else redirect(url_for('main.home'))

        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title = 'Login', form = form)


@users.route('/logout' )
def logout():
    logout_user()
    return redirect(url_for('main.home'))



@users.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:  #picture.data is form input name from forms.py
            picture_file = save_picture(form.picture.data) # nasa taas ang declaration 
            current_user.image_file = picture_file  #image_file is the name of field image_file in the models
        current_user.username = form.username.data  #note SQL_ALCHEMEY has feature of current_user to be updated as field as simply
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!','success')
        return redirect(url_for('users.account'))
    elif request.method == 'GET':
        form.username.data = current_user.username #this is READ
        form.email.data = current_user.email  #this is READ
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('account.html', title='My Profile', image_file = image_file, form = form)



@users.route("/user/<string:username>") #READ/VIEW, this is for specific user posts
def user_posts(username):
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    post = Post.query.filter_by(author=user)\
        .order_by(Post.date_posted.desc())\
        .paginate(page=page, per_page=10)
    return render_template('user_posts.html', posts=post, user=user)



#request to reset password
@users.route("/reset_password", methods=['GET', 'POST'])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RequestResetForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        send_reset_email(user)
        flash('An email has been sent with instruction to reset your password.', 'info')
        return redirect(url_for('users.login'))
    return render_template('reset_request.html', title='Reset Password', form=form)

#verification
@users.route("/reset_password/<token>", methods=['GET', 'POST'])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    user = User.verify_reset_token(token) #eto yun sa staticmethod
    if user is None:
        flash('That is an invalid token or expired token', 'warning')
        return redirect(url_for('users.reset_request'))

    form = ResetPasswordForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user.password = hashed_password
        db.session.commit()
        flash('Your password has been updated! You are now able to log in', 'success') 
        return redirect(url_for('users.login'))

    return render_template('reset_token.html', title='Reset Password', form=form)


    