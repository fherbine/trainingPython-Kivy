Glossary:
---------

- hello_world: Simple 'hello world text' dispatched on site route '/'.
- sto: A kebab flask app wich have several routes with simple text in it.
- path: Get variables via url path.
- safe: simple str path use with escape func.

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

With flask we can cast url path into variabvles:
```
@app.route('/basepath/\<var_type:variable\>')
def function(variable):
    return '%s' % variable
```

> Note that var_type precision is useless if type is str because it's default.

PATH VARS TYPES:
----------------

|  Type  |                Desc                |
|--------|------------------------------------|
| string | (default) Text without slashes     |
| int    | positives integers                 |
| float  | positives floating points numbers  |
| path   | as `str` but also accept slashes   |
| uuid   | accepts UUID str                   |

To protect from url injection `pydoc flask.escape`, use 'escape function':
```
@app.route('/\<string\>')
def pstring(string):
    return '%s' % escape(string)
```

We can use 'flask.url_for(func, **kwargs)' to get corresponding URL to a
specific flask function. To use it we should create a test context:
```
@app.route('/user/\<usn\>')
def profile(usn):
    return 'Username is %s' % usn

with app.test_request_context():
    print(url_for('profile', 'Felix Herbinet'))
```

`/user/Felix%20Herbinet`

Lancer l'app flask depuis le py:
```
\# contenu de l'app

if \_\_name\_\_ == '\_\_main\_\_':
    app.run(host='host\<str\>', port=<port>, debug=True)

```
