from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mail import Mail, Message
import os
from dotenv import load_dotenv
import smtplib

load_dotenv()

app = Flask(__name__)

app.secret_key = os.getenv('SECRET_KEY')

# Email Configuration
app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,  # ← Change to 465 (SSL)
    MAIL_USE_SSL=True,  # ← Change to SSL
    MAIL_USERNAME=os.getenv('MAIL_USER'),
    MAIL_PASSWORD=os.getenv('MAIL_APP_PASSWORD'),
    MAIL_DEFAULT_SENDER=(os.getenv('MAIL_USER'), "Waldiss_portfolio"),
    MAIL_DEBUG=True
)

mail = Mail(app)

def test_smtp_connection():
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:  # ← Use SMTP_SSL
            server.login(os.getenv('MAIL_USER'), os.getenv('MAIL_APP_PASSWORD'))
            print("✅ SMTP Connection Successful!")
            return True
    except Exception as e:
        print(f"❌ SMTP Connection Failed: {type(e).__name__}, {str(e)}")
        return False

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
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

        if purpose not in ['collaboration', 'project', 'consultation', 'other']:
            flash('Please select a valid purpose', 'danger')
            return redirect(url_for('contact'))

        if len(message) < 20 or len(message) > 500:
            flash('Message must be between 20-500 characters', 'danger')
            return redirect(url_for('contact'))

        # Send mail
        try:
            msg = Message(
                subject=f"[{purpose.capitalize()}] Message from {name}",
                sender=app.config['MAIL_DEFAULT_SENDER'],  # ← Explicit sender
                recipients=['kretoswaldis@gmail.com'],
                reply_to=email
                )
            msg.body = f"""Name: {name}
Email: {email}
Purpose: {purpose.capitalize()}

Message:
{message}"""
            mail.send(msg)
            flash('🌌 Your message has been transmitted successfully!', 'success')
        except Exception as e:
            print(f"Mail error: {type(e).__name__}, {str(e)}")
            flash('❌ Message transmission failed. Please try again later.', 'danger')
        return redirect(url_for('home'))

    return render_template('index.html')

if __name__ == '__main__':
    if test_smtp_connection():
        app.run(debug=True)
    else:
        print("Exiting due to SMTP connection failure.")
