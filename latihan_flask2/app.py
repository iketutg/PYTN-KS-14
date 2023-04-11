from flask import Flask
from flask import render_template

app = Flask(__name__)


## http://localhost:5000/   or http://{ip-komputer}:5000/ or http://127.0.0.1:5000/ 
@app.route('/')
def index():
    return "Page Index"

@app.route('/hello')
@app.route('/hello/<names>')
def hello(names=None):
    return render_template('hello.html', nama=names)


