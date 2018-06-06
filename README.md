# Flask Tutorial

Going through the official [Flask tutorial](http://flask.pocoo.org/docs/1.0/tutorial/).

## Project Layout

- `flaskr/`, a Python package containing your application code and files.
- `tests/`, a directory containing test modules.
- `venv/`, a Python virtual environment where Flask and other dependencies are installed.
- Installation files telling Python how to install your project.

```
/home/user/Projects/flask-tutorial
├── flaskr/
│   ├── __init__.py
│   ├── ...
│   ├── templates/
│   │   ├── ...
│   └── static/
│       └── style.css
├── tests/
│   ├── ...
├── venv/
├── setup.py
└── MANIFEST.in
```

## Blueprints and Views

A **view** function is the code you write to respond to requests to your application. Flask matches the incoming request URL to the view that handles it and the view returns data that Flask turns into an outgoing response. 

A **blueprint** is a way to organize related views. Views are registered with the blueprint and the blue print is register with the application. 

\__init__.py
```
app.register_blueprint(auth.bp)
```

auth.py
```
@bp.route('/register', methods=('GET', 'POST'))
def register():
```

The url_for() function generates the URL to a view based on a name and arguments. The name associated with a view is also called the endpoint, and by default it’s the same as the name of the view function.

When using a blueprint, the name of the blueprint is prepended to the name of the function. I.e. the above endpoint would be `auth/login`.

## Templates

Templates are files that contain static data as well as placeholders for dynamic data. A template is rendered with specific data to produce a final document. Flask uses the Jinja template library to render templates.

## Tests

The test code is located in the tests directory. This directory is next to the root package, not inside it. The config file contains setup functions called fixtures that each test will use. Tests are in Python modules that start with test_, and each test function in those modules also starts with test_.

```
@pytest.fixture
def app():
	...
	
@pytest.fixture
def client(app):
	...
```

Pytest uses fixtures by matching their function names with the names of arguments in the test functions. For example, the test_hello function you’ll write next takes a client argument. Pytest matches that with the client fixture function, calls it, and passes the returned value to the test function.

test_factory.py
```
def test_hello(client):
```

`pytest.mark.parametrize` tells Pytest to run the same test function with different arguments. You use it here to test different invalid input and error messages without writing the same code three times.

```
@pytest.mark.parametrize(('username', 'password', 'message'), (
    ('a', 'test', b'Incorrect username.'),
    ('test', 'a', b'Incorrect password.'),
))
def test_login_validate_input(auth, username, password, message):
```