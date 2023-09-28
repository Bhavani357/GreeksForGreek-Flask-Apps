from flask import Flask , render_template

app = Flask(__name__) 

@app.route('/')
def normal():
    message = "hi static folder this is from app.py"
    return render_template('simple.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)