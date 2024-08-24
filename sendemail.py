import smtplib
import getpass
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email():
    # Sender and recipient email addresses
    sender_address = 'bmccullum2111@gmail.com'
    recipient_address = 'mohammed.ismail.njb@gmail.com'
    
    # Prompt for the sender's email password
    password = getpass.getpass(prompt="Enter your email password: ")
    
    # Create the email subject and body
    subject = 'Test Email'
    body = '''Hi Mohammed Ismail Najeeb,

This is a test email sent from a Python script.

Best regards,
Your Python Script'''

    # Set up the MIME
    msg = MIMEMultipart()
    msg['From'] = sender_address
    msg['To'] = recipient_address
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # Create the SMTP session for sending the email
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)  # Use Gmail's SMTP server
        server.starttls()  # Start TLS for security
        server.login(sender_address, password)  # Log in to the email account
        text = msg.as_string()  # Convert the message to a string
        server.sendmail(sender_address, recipient_address, text)  # Send the email
        print("Email sent successfully!")
    except smtplib.SMTPAuthenticationError:
        print("Failed to send email: Authentication error.")
    except Exception as e:
        print(f"Failed to send email: {e}")
    finally:
        server.quit()  # Terminate the SMTP session

send_email()
