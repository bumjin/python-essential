#!/usr/bin/env python

import urllib
import urllib2
import re
from cookielib import CookieJar

#html = urllib.urlopen("http://jshawl.com/python-playground/").read()

#print html.read()

#urllib.urlretrieve('http://jshawl.com/python-playground/terminal.png', 'terminal.png')

#print re.findall('[\w]+@[\w.]+', html)

cj = CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

formValues = {
	"username":"user",
	"password":"pass"
}

data = urllib.urlencode(formValues)

response = opener.open('http://jshawl.com/python-playground/login.php', data)
#print response.read()

secure = opener.open('http://jshawl.com/python-playground/protected2.php', data)
print secure.read()