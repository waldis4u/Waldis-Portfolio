from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mail import Mail, Message
import os
import smtplib

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'development-key')

# Email Configuration
app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_TLS=True,
    MAIL_USERNAME=os.environ.get('MAIL_USER'),
    MAIL_PASSWORD=os.environ.get('MAIL_PASS'),
    MAIL_DEFAULT_SENDER=os.environ.get('MAIL_USER'),  # Add default sender
    MAIL_DEBUG=True
)

mail = Mail(app)

def test_smtp_connection():
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(os.environ.get('MAIL_USER'), os.environ.get('MAIL_PASS'))
            print("✅ SMTP Connection Successful!")
            return True
    except Exception as e:
        print(f"❌ SMTP Connection Failed: {str(e)}")
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
                recipients=['kretoswaldis@gmail.com'],  # Remove sender parameter
                reply_to=email  # Add reply_to field
            )
            
            # Set the message body
            msg.body = f"""Name: {name}
Email: {email}
Purpose: {purpose.capitalize()}

Message:
{message}"""

            mail.send(msg)
            flash('🌌 Your message has been transmitted successfully!', 'success')
        except Exception as e:
            print(f"Mail error: {str(e)}")
            flash('❌ Message transmission failed. Please try again later.', 'danger')

    return redirect(url_for('home'))  # Redirect to home instead of contact

    return render_template('index.html')
# Add similar routes for other pages


if __name__ == '__main__':
    # Test SMTP connection before starting the app
    test_smtp_connection()
    app.run(debug=True)
