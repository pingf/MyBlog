'''
Created on Dec 21, 2014

@author: fcmeng
'''

import os
from src import app
from src import manager
from src import db

@manager.command
def hello():
    print("hello")
    
@manager.command
def run():
    port = int(os.environ.get('PORT', 4444))
    app.run(host='0.0.0.0', port=port) 
       
if __name__ == "__main__":
    manager.run()
