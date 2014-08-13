import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

class MailClient(object):
  
  def __init__(self, sender, password, server_address=None,port=None):
    server_address = server_address or "smtp.gmail.com"
    port = port or 587
    self.server = smtplib.SMTP(server_address,port)
    self.sender = sender
    self.password = password

  def Open(self):
    self.server.ehlo()
    self.server.starttls()
    self.server.ehlo()
    self.server.login(self.sender,self.password)
    return True

  def Close(self):
    self.server.close()
    return True

  def NewMessage(self, receiver, subject, body):
    msg = MIMEMultipart()
    msg['From'] = self.sender
    msg['To'] = receiver
    msg['Subject']  = subject
    msg.attach(MIMEText(body,'plain'))
    return msg

  def Send(self, message):
    self.server.sendmail(message['From'],
                         message['To'],
                         message.as_string())
    return True

if __name__ == "__main__":    
  pass
