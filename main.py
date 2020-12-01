from flask import Flask, url_for
from jinja2 import Template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'


template = Template('Hello {{ name }}!')
template.render(name='John Doe')

with app.test_request_context():
    print(url_for('index'))
    print(url_for('hello'))
url_for('static', filename='style.css')