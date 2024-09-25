import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import traceback

class MailHandler():
    def __init__(self, from_address, password):
        self.from_address = from_address
        self.password = password

    def send_mail(self, to_address, subject, mail_body):
        try:
            msg = MIMEText(mail_body)
            msg['Subject'] = subject
            msg['From'] = self.from_address
            msg['To'] = to_address
    
            smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
            smtpobj.ehlo()
            smtpobj.starttls()
            smtpobj.ehlo()
            smtpobj.login(self.from_address, self.password)
            smtpobj.sendmail(self.from_address, to_address, msg.as_string())
            smtpobj.close()
            return True
        except:
            return False
    
    def read_mail_body_template(self, filepath):
        with open(filepath, "r", encoding="utf-8") as file:
            mail_body_template = file.read()
        return mail_body_template