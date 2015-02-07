'''
Created on Feb 7, 2015

@author: Jesse Meng
'''

from flask import Blueprint, render_template 

simple_page = Blueprint('simple_page', __name__,
                        template_folder='templates',url_prefix='/pages')

@simple_page.route('/simple')
def show():
    return render_template('hello.html')
