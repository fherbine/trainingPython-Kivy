Glossary:
---------

- hello_world: Simple 'hello world text' dispatched on site route '/'.

Course:
--------

To run a Flask app, first we have to instanciate a Flask object called app.
```app = Flask(__name__)```

Then with decorators, we have to create some path to access our pages:
```
@app.route('/')
def method():
    return 'page content'
```

To run it we have to export 'FLASK_APP' env var and run flask:
```
$ export FLASK_APP="myscript.py"
$ flask run \[--host specific_host\] \[--port specific_port\]
```

To run your app in dev mode you should set 'FLASK_ENV' variable
```$ export FLASK_ENV="development"```
