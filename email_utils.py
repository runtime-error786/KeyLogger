import smtplib
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders
import os
import time

def send_mail(email, password, subject, message, attachment_paths):
    sender = email
    receiver = email  # Sending to self for testing

    # Create the message object
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = receiver
    msg['Subject'] = subject

    # Attach the main message with explicit UTF-8 encoding

    # Create a text file containing the message body and attach it
    message_file_path = "message.txt"
    try:
        with open(message_file_path, "w", encoding="utf-8") as message_file:
            message_file.write(message)
        
        # Attach the message file as a text file
        if os.path.exists(message_file_path):
            with open(message_file_path, "rb") as message_file:
                part = MIMEBase("application", "octet-stream")
                part.set_payload(message_file.read())
                encoders.encode_base64(part)
                part.add_header(
                    "Content-Disposition",
                    f"attachment; filename={os.path.basename(message_file_path)}",
                )
                msg.attach(part)
        else:
            print(f"Failed to create message file: {message_file_path}")
    except Exception as e:
        print(f"Failed to create or attach the message file: {e}")

    # Attach additional files
    for attachment_path in attachment_paths:
        if os.path.exists(attachment_path):
            try:
                with open(attachment_path, "rb") as attachment_file:
                    part = MIMEBase("application", "octet-stream")
                    part.set_payload(attachment_file.read())
                    encoders.encode_base64(part)
                    part.add_header(
                        "Content-Disposition",
                        f"attachment; filename={os.path.basename(attachment_path)}",
                    )
                    msg.attach(part)
            except Exception as e:
                print(f"Failed to attach file {attachment_path}: {e}")
        else:
            print(f"Attachment not found: {attachment_path}")

    # Retry mechanism for sending email
    max_retries = 3
    retry_delay = 5  # seconds

    for attempt in range(max_retries):
        try:
            # Connect to SMTP server
            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()  # Secure the connection
                server.login(sender, password)  # Login
                server.sendmail(sender, receiver, msg.as_string())  # Send the email
                print("Email sent successfully!")
                break
        except smtplib.SMTPException as e:
            print(f"Attempt {attempt + 1}/{max_retries} failed: {e}")
            if attempt < max_retries - 1:
                print(f"Retrying in {retry_delay} seconds...")
                time.sleep(retry_delay)
            else:
                print("Failed to send email after multiple attempts.")

