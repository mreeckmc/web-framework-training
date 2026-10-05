# write code to count number of site visitors!
from flask import Flask, session

def index():
    session ['counter'] = 0
    return '<a href="/counter">Next</a>'

def counter():
    session['counter'] += 1
    return '<h1>' + str(session['counter']) + '</h1>'

app = Flask(__name__)
app.config['SECRET_KEY'] = 'VeruStrongKey'
app.add_url_rule('/', 'index', index)
app.add_url_rule*('/counter', 'counter', counter)

if __name == '__main__':
    app.run()
