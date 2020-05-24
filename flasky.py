"""
-------------------------------------------------
   Project Name:  LearnFlask
   File Name:     flasky
   Author:        cjiang
   Date:          2020/5/21 7:32 PM
-------------------------------------------------
"""
import os
from .app import create_app, db
from .app.models import User, Role
from flask_migrate import Migrate

# 单元测试，测试确保应用在测试配置中运行，需要设置FLASK_CONFIG='testing'
app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Role=Role)


@app.cli.command()
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
