import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

class MailClient(object):
  
  def __init__(self,server_address,port,sender,password):
    self.server = smtplib.SMTP(server_address,port)
    self.sender = sender
    self.password = password

  def _Login(self):
    self.server.ehlo()
    self.server.starttls()
    self.server.ehlo()
    self.server.login(self.sender,self.password)

  def NewMessage(self,receiver,subject,body):
    msg = MIMEMultipart()
    msg['From'] = self.sender
    msg['To'] = receiver
    msg['Subject']  = subject
    msg.attach(MIMEText(body,'plain'))
    return msg

  def Send(self,message):
    self._Login()
    self.server.sendmail(message['From'],
                         message['To'],
                         message.as_string())
    
