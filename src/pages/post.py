'''
Created on Feb 7, 2015

@author: Jesse Meng
'''
from flask import Flask, request, Response, session, flash, redirect
from flask import Blueprint, render_template, url_for
from flask.ext.login import login_user, logout_user, current_user, login_required

from src.forms import LoginForm
from src.models import Post,User

posts_page = Blueprint('post', __name__,
                        template_folder='templates',url_prefix='/posts')


@posts_page.route('/by_uid/<user_id>', methods=['GET'])
def list_by_uid(user_id):
    posts = User.query.filter_by(id=user_id).first().posts
    print(type(posts),'---')
    return render_template('posts_by_uid.html',posts=posts)
    
