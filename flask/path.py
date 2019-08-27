from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Nothing to see there !'

@app.route('/str/<string>')
def get_str(string):
    return 'you\'ve typed %s' % string

@app.route('/int/<int:number>')
def get_number(number):
    return 'Your number is %s' % number

@app.route('/float/<float:number>')
def get_floating(number):
    return 'Your floating number is %s' % number

@app.route('/path/<path:the_path>')
def wich_path(the_path):
    return 'The current path is /path/%s' % the_path
