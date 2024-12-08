from flask import Flask, request, redirect, url_for
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('static', filename='index.html'))

@app.route('/send_email', methods=['POST'])
def send_email():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    msg = MIMEMultipart()
    msg['From'] = 'your_email@example.com'
    msg['To'] = 'johngabary@actubasics.com'
    msg['Subject'] = 'Nouveau message de votre site personnel'
    
    body = f"Nom: {name}\nEmail: {email}\nMessage:\n{message}"
    msg.attach(MIMEText(body, 'plain'))
    
    server = smtplib.SMTP('smtp.example.com', 587)
    server.starttls()
    server.login('your_email@example.com', 'your_password')
    text = msg.as_string()
    server.sendmail('your_email@example.com', 'johngabary@actubasics.com', text)
    server.quit()

    return 'Votre message a été envoyé avec succès.'

if __name__ == '__main__':
    app.run(debug=True)
