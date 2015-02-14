'''
Created on Feb 7, 2015

@author: Jesse Meng
'''
from flask import Flask, request, Response, session, flash, redirect
from flask import Blueprint, render_template, url_for
from flask.ext.login import login_user, logout_user, current_user, login_required

from src.forms import LoginForm
from src.models import User
from src import login_manager

user_page = Blueprint('user', __name__,
                        template_folder='templates',url_prefix='/user')

login_manager.login_view = '/user/login'
@login_manager.user_loader  
def load_user(id):
    return User.query.get(int(id))

@user_page.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        if current_user.is_authenticated():
            return redirect(url_for('simple.show'))
        form = LoginForm()
        return render_template('login.html', form=form)
    else: 
        email = request.form['email']
        password = request.form['password']
        
        registered_user = User.query.filter_by(email=email,password=password).first()
        if registered_user is not None:
            login_user(registered_user)
            flash('Logged in successfully')    
            # TODO: login success page
            return redirect(url_for('simple.show'))

        
@user_page.route('/logout', methods=['GET'])
def logout():
    logout_user()
    return redirect(url_for('user.login'))
