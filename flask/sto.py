from flask import Flask
app = Flask(__name__)

@app.route('/')
def sauce():
    return 'which sauce with your doner?'

@app.route('/salade')
def salade():
    return 'Just a way to have less meat.'

@app.route('/tomates')
def tomatoes():
    return 'Always crude !'

@app.route('/oignons')
def oignons():
    return 'Never try to kiss someone after even your mother !'

