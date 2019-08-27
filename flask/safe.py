from flask import Flask, escape
app = Flask(__name__)

@app.route('/<variable>')
def safe(variable):
    return '{} is safe !'.format(escape(variable))
