"""
-------------------------------------------------
   Project Name:  LearnFlask
   File Name:     __init__.py
   Author:        cjiang
   Date:          2020/5/26 6:25 PM
-------------------------------------------------
"""
from flask import Blueprint

auth = Blueprint('auth', __name__)

from . import views
