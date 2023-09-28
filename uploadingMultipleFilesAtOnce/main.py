from flask import Flask,render_template,request 
from fileinput import filename 

app = Flask(__name__) 

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/success', methods=['POST'])
def success():
    if request.method == 'POST':
        file_list = request.files.getlist('file')
        for file in file_list:
            file.save(f'uploadedFiles/{file.filename}')
        return '<h2>Files uploaded successfully</h2>'

if __name__ == '__main__':
    app.run(debug=True)
