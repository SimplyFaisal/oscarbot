import mechanize
from bs4 import BeautifulSoup
import cookielib


class OscarBot(object):

  def __init__(self,_id,pin):
    self._id = _id
    self.pin = pin

  def Register(self,schedule):
    """Navigate to Oscar and register for classes"""
    # oscar login page
    oscar = "https://oscar.gatech.edu/pls/bprod/twbkwbis.P_GenMenu?name=bmenu.P_StuMainMnu"
    
    #mechanize boilerplate
    br = mechanize.Browser()
    cj = cookielib.LWPCookieJar()
    br.set_cookiejar(cj)
    br.set_handle_equiv(True)
    br.set_handle_gzip(True)
    br.set_handle_redirect(True)
    br.set_handle_referer(True)
    br.set_handle_robots(False)
    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
    br.addheaders = [("User-agent", "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1")]

    #open oscar sign-in page and grab login form
    r = br.open(oscar)
    br.form = list(br.forms())[0]
    br["sid"] = self._id
    br["PIN"] = self.pin
    res = br.submit()

    #initial landing page once signed into oscar
    br.open("https://oscar.gatech.edu/pls/bprod/twbkwbis.P_GenMenu?name=bmenu.P_RegMnu")

    #jump to registration sub menu
    br.open("https://oscar.gatech.edu/pls/bprod/bwskfreg.P_AltPin")

    #the year selection form is the second(hence 1st index)
    #defaults to the current year so we can just submit
    br.form = list(br.forms())[1]
    br.submit()

    #now we are at the registration page
    #the text fields are in the second form
    br.form = list(br.forms())[1]
    fields = []

    #the text fields all have the same name and type
    #so we'll just insert them into a list 
    for control in br.form.controls:
      if control.type == "text" and control.name == "CRN_IN":
        fields.append(control)

    #set each text fields equal to a class in the schedule
    for field, course in zip(fields, schedule):
      field.value = str(course)
   
    response = br.submit()
    registered_classes = self.EnrolledClasses(response)
    return registered_classes

  def EnrolledClasses(self,html):
    """Parse HTML and return which classes it successfully registered for.""" 
    classes = []
    soup = BeautifulSoup(html)
    for element in soup.find_all("input"):
      if element["name"] == "TITLE" and element["value"]:
        classes.append(element.get("value"))
    return classes

