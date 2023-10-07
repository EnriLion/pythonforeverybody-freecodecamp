import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter -')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup ('a') # < a href ..>(anchor tag)
for tag in tags:
    print(tag.get('href', None))

# output

# python urllinks.py
# Enter - http://www.dr-chuck.com/page1.htm
# http://www.dr-chuck.com/page2.htm
