from bottle import \
    run, \
    Bottle, \
    route, \
    error, \
    template, \
    get, \
    request, \
    post, \
    static_file

app = Bottle()


@app.route('/')
def method():
    return '''
        <h1>WELCOME THE THE BOTTLE FRAMEWORK</h1>
    '''


@app.route('/routing/<path>')
def pass_path(path='name'):
    return template('Hello this is an Nested pass path of location {{path}}', path=path)


@app.route('/object/<id:int>')
def callback(id):
    assert isinstance(id, int)


@app.get('/login')
def login():
    return '''
        <form action="/login" method="post">
           <p> Username:</p> <input name="username" type="text" placeholder="Enter a user name"/>
            <p>Password:</p> <input name="password" type="password"placeholder="Enter a user Password" />
            <br>
            <input value="Login" type="submit" />
        </form>
    '''


@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='/path/to/your/static/files')


# Error Reporter
@app.error(404)
def error_message(error):
    return '''
        <h3>Its an 404 error</h3>
    '''


run(app, host="localhost", port="4572", debug="true")
