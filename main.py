from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'

with app.test_request_context():
    print(url_for('index'))
    print(url_for('hello'))
