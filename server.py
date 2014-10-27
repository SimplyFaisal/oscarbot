import info
import time

from datetime import datetime
from mail import MailClient
from oscarbot import OscarBot

def main():
  time_ticket = datetime(2014,8,8,hour=12) 
  current_time = datetime.now()
  while True:
    current_time = datetime.now()
    time.sleep(60)
    if current_time > time_ticket:
      StartRegistration([20820, 21843, 26327, 20873, 23562])
      return

def StartRegistration(classes):
  oscar = OscarBot(info.gtid, info.pin)
  enrolled = oscar.Register(classes)
  mail_client = MailClient(info.address,info.password)
  mail_client.Open()
  content = "OscarBot signed you up for {} !".format(enrolled)
  message = mail_client.NewMessage(info.cell, "OscarBot", content)
  mail_client.Send(message)
  mail_client.Close()

if __name__ == "__main__":
  main()
