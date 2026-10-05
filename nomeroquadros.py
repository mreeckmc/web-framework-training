from random import randint
from flask import Flask, session, redirect, url_for
from db_scripts import get_question_after

def index():
    max_quiz = 3
    session ['quiz'] = randint(1, max_quiz)
    session['last_question'] = 0
    return '<a href="/test"Test</a>'

def test():
    result = get_question_after(session['last_question'], session['quiz'])
    if result is None or len(result) == 0:
        return redirect(url_for('result'))
    else:
        session['last_question'] = result[0]
        return '<h1>' + str(session['quiz']) + '<br>' + str(result) + '</h1>'

def result():
    result "that's all folks!"

app = Flask(__name__)
app.add_url_rule('/', 'index', index)
app.add_url_rule('/test', 'test', test)
app.add_url_rule('/result', 'result', result)
app.config['SECRET_KEY'] = 'ThisIsSecretSecretSecretlife'

if __name__ == '__main__':
    app.run()
