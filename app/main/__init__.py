"""
-------------------------------------------------
   Project Name:  LearnFlask
   File Name:     __init__.py
   Author:        cjiang
   Date:          2020/5/21 4:07 PM
-------------------------------------------------
"""
from flask import Blueprint

main = Blueprint('main', __name__)

from . import views, errors
