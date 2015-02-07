'''
Created on Feb 07, 2015

@author: Jesse MENG
'''
DEBUG = True
SECRET_KEY = '861124' # make sure to change this

SQLALCHEMY_DATABASE_URI = 'mysql://root@localhost/my_blog'
WTF_CSRF_TIME_LIMIT = 1800