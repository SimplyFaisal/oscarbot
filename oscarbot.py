import mechanize
from bs4 import BeautifulSoup
import cookielib
from info import pin
from info import gtid

oscar = "https://oscar.gatech.edu/pls/bprod/twbkwbis.P_GenMenu?name=bmenu.P_StuMainMnu"

br = mechanize.Browser()
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)
br.set_handle_equiv(True)
br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

#open oscar sign-in page and grab login form
r = br.open(oscar)
br.form = list(br.forms())[0]
br["sid"] = gtid
br["PIN"] = pin
res = br.submit()

#initial landing page once signed into oscar
br.open("https://oscar.gatech.edu/pls/bprod/twbkwbis.P_GenMenu?name=bmenu.P_RegMnu")

#jump to registration sub menu
br.open("https://oscar.gatech.edu/pls/bprod/bwskfreg.P_AltPin")

#there are two forms on the page
#the year selection form is the second(hence 1st index)
#defaults to the current year so we can just submit
br.form = list(br.forms())[1]

br.submit()
print br.response().read()
