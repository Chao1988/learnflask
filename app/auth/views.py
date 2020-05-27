"""
-------------------------------------------------
   Project Name:  LearnFlask
   File Name:     views
   Author:        cjiang
   Date:          2020/5/26 6:37 PM
-------------------------------------------------
"""
from flask import render_template
from . import auth


@auth.route('/login')
def login():
    return render_template('auth/login.html')
