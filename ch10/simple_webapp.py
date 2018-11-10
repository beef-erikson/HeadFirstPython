from flask import Flask, session
from checker import check_logged_in

app = Flask(__name__)

app.secret_key = 'weakPassword'


@app.route('/')
def hello() -> str:
    return 'Hello from the simple webapp'


# Pages 1-3 uses the check_logged_in from checker.py to determine if logged in to view.
@app.route('/page1')
@check_logged_in
def page1() -> str:
    return 'This is page 1.'


@app.route('/page2')
@check_logged_in
def page2() -> str:
    return 'This is page 2.'


@app.route('/page3')
@check_logged_in
def page3() -> str:
    return 'This is page 3.'


@app.route('/login')
def login() -> str:
    session['logged_in'] = True
    return 'You are now logged in.'


@app.route('/logout')
def logout() -> str:
    if 'logged_in' in session:
        session.pop('logged_in')
    return 'You have successfully logged out.'


@app.route('/status')
def status() -> str:
    if 'logged_in' in session:
        return 'You are currently logged in.'
    return 'You are currently logged out.'


if __name__ == '__main__':
    app.run(debug=True)
