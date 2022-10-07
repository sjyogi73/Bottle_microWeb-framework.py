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
    <div style="display:flex" >
        
        <img style="height:30px;width: 30px;margin:25px 30px" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSPHRvtFUvNT9Rrpz2HE4gu05hPPg8m7DweCg&usqp=CAU"/>
        <h1>WELCOME - THE THE - BOTTLE - FRAMEWORK</h1>
    </div>
        
    '''


@app.route('/home')
def index():
    return template('index')


@app.route('/routing/<path>')
def pass_path(path='name'):
    return template('Hello this is an - Nested pass path of location - {{path}}', path=path)


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


@route('/home/<filename:path>')
def server_static(filepath):
    return static_file(filepath, root='/index.html')


# Error Reporter
@app.error(404)
def error_message(error):
    return '''
        <h3>Please Give Valid Request Because Its Request Not Found(404)</h3>
        <h1 style="margin:5em,color:red"> ERROR - 404</h1>
    '''


run(app, host="127.0.0.1", port="4572", debug="true")
