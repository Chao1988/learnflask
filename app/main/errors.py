"""
-------------------------------------------------
   Project Name:  LearnFlask
   File Name:     errors
   Author:        cjiang
   Date:          2020/5/21 4:19 PM
-------------------------------------------------
"""
from flask import render_template
from . import main


@main.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@main.app_errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

