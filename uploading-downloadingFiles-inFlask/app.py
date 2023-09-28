from flask import Flask,render_template,request,send_file
from io import BytesIO
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__) 
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app)

class Upload(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    filename = db.Column(db.String(50)) 
    data = db.Column(db.LargeBinary)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        File = request.files['file']
        upload = Upload(filename=File.filename, data=File.read())
        db.session.commit() 
        return f'Uploaded: { File.filename}'
    return render_template('index.html')

# next we run these commands in terminal 
'''
python
from app import app, db
app.app_context().push()
db.create_all()
exit()

'''

@app.route('/download/<upload_id>')
def download(upload_id):
    upload = Upload.query.filter_by(id=upload_id).first() 
    return send_file(BytesIO(upload.data), download_name = upload.filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)