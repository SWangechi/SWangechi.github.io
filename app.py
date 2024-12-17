from flask import Flask, request, render_template
from flask_mail import Mail, Message

app = Flask(__name__)

# Mail configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'sgituire@gmail.com'  # Replace with your email
app.config['MAIL_PASSWORD'] = 'jmqr bxzp mckx uaeg'  # Replace with your email password

mail = Mail(app)

@app.route('/send_message', methods=['POST'])
def send_message():
    try:
        # Retrieve form data
        name = request.form['name']
        email = request.form['email']
        message_content = request.form['message']

        # Send email
        msg = Message(
            subject=f"Message from {name}",
            sender=email,
            recipients=['sgituire@gmail.com'],  # Replace with your receiving email
            body=f"Name: {name}\nEmail: {email}\n\nMessage:\n{message_content}"
        )
        mail.send(msg)
        # Render success page
        return render_template('success.html', name=name)
    except Exception as e:
        return f"An error occurred: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
