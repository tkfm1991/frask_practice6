from importlib import import_module
import unittest


class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def test_login(self):
        flask_app = import_module('views')
        flask_app.app.testing = True
        with flask_app.app.test_client() as c:
            param = 'PyQ'
            c.get('/login', query_string=dict(name=param))
            assert flask_app.session['username'] == param

    def test_todo(self):
        flask_app = import_module('views')
        flask_app.app.testing = True
        answer = ['タスクA', 'タスクB', 'タスクC']
        with flask_app.app.test_client() as c:
            c.get('/login', query_string=dict(name="username"))
            c.post('/todo', data=dict(todo='タスクA'), follow_redirects=True)
            c.post('/todo', data=dict(todo='タスクB'), follow_redirects=True)
            c.post('/todo', data=dict(todo='タスクC'), follow_redirects=True)
            assert flask_app.session['todo'] == answer

            c.get('/todo_clear')
            assert 'todo' not in flask_app.session
