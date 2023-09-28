from flask import Flask,render_template,request 
from flask_mail import Mail, Message 

app = Flask(__name__)
mail = Mail(app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'durgabhavaniyasarla232@gmail.com'
app.config['MAIL_PASSWORD'] = '21d6b1999'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)


@app.route('/')
def index():
    msg = Message(
        'Hello',
        sender = 'durgabhavaniyasarla232@gmail.com',
        recipients = ['venky@gmail.com']
    )

    msg.body = 'Hello Flask message sent from Flask-Mail' 
    mail.send(msg) 
    return 'Sent'

if __name__ == '__main__':
    app.run(debug=True)