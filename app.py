from flask import Flask, render_template, request
from flask_mail import Mail, Message
import os

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USER')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASS')
mail = Mail(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        purpose = request.form.get('purpose', '').strip()
        message = request.form.get('message', '').strip()

        # Validate inputs
        if not all([name, email, purpose, message]):
            flash('All fields are required', 'danger')
            return redirect(url_for('contact'))

        if len(name) < 3 or len(name) > 50:
            flash('Name must be between 3-50 characters', 'danger')
            return redirect(url_for('contact'))

        if len(message) < 20 or len(message) > 500:
            flash('Message must be between 20-500 characters', 'danger')
            return redirect(url_for('contact'))

        # Send mail
        msg = Message(  # Was using message()
            subject=f"[{purpose.capitalize()}] Message from {name}",
            sender=email,
            recipients=['kretoswaldis@gmail.com'],  # Fixed typo 'receipients'
            body=f"From: {name} <{email}>\n\n{message}"
            )

        try:
            mail.send(msg)
            flash('Your cosmic message has been transmitted!', 'success')
        except Exception as e:
            flash('Message transmission failed. Try again later.', 'danger')

        return redirect(url_for('contact'))

    return render_template('contact.html')



# Add similar routes for other pages

if __name__ == '__main__':
    app.run(debug=True)
