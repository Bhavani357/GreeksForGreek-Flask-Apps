from flask import Flask,render_template,request 

app = Flask(__name__) 

@app.route('/')
def student():
    return render_template("students.html")

@app.route('/result', methods=['POST','GET'])
def results():
    result = {}
    if request.method == 'POST':
        result = request.form
    return render_template("results.html", result = result)

if __name__ == '__main__':
    app.run(debug=True)