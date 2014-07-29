import info
import time

from datetime import datetime
from mail import MailClient
from oscarbot import OscarBot

def main():
  minute = 60
  time_ticket = datetime(2014,8,8,hour=12) 
  current_time = datetime.now()
  while True:
    current_time = datetime.now()
    time.sleep(3*minute)
    print current_time
    if current_time > time_ticket:
      oscar = OscarBot(info.gtid,info.pin)
      classes = oscar.Register([89086])
      mail_client = MailClient("smtp.gmail.com",587,
                        info.address,info.password)
      content = "OscarBot got you into {}".format(classes)
      message = mail_client.NewMessage("d_faisal_a@yahoo.com","OscarBot",content)
      mail_client.Send(message)
      return

main()

if "__name__" == "__main__":
  pass
