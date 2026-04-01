import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(to, message):
    try:
        msg = MIMEMultipart()
        msg['From'] = 'your-email@gmail.com'
        msg['To'] = to
        msg['Subject'] = 'Registration successful'
        msg.attach(MIMEText(message, 'plain'))
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(msg['From'], 'your-password')
        text = msg.as_string()
        server.sendmail(msg['From'], msg['To'], text)
        server.quit()
    except Exception as e:
        print(str(e))