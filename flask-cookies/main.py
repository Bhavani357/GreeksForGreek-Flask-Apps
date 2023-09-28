from flask import Flask, request, make_response ,render_template

app = Flask(__name__) 

@app.route('/setcookie')
def setcookie():
    resp = make_response('Setting the cookie') 
    resp.set_cookie('GFG', 'ComputerScience Portal') 
    return resp 

@app.route('/getcookie')
def getcookie():
    value_of_the_key_gfg = request.cookies.get('GFG')
    return 'GFG is a '+ value_of_the_key_gfg

@app.route('/', methods= ['GET'])
def Login():
    return render_template('login.html')

@app.route('/details', methods=['GET','POST']) 
def login():
    if request.method == 'POST':
        name = request.form['username']
        output = 'Hi, Welcome '+ name+ ""
        resp = make_response(output)
        resp.set_cookie('username', name)
    return resp 

@app.route('/users_count')
def visitors_count():
    count = int(request.cookies.get('visitors count', 0)) 
    count = count +1 
    output = 'You visited this page for '+ str(count)+' times'
    resp = make_response(output)
    resp.set_cookie('visitors count', str(count))
    return resp 

@app.route('/get')
def get_visitors_count():
    count = request.cookies.get('visitors count')
    return count



if __name__ == '__main__':
    app.run(debug=True)