import urllib
from BeautifulSoup import *

url = raw_input('enter url- ')
count = int(raw_input('enter count- '))
position = int(raw_input('enter position- '))

print url

for i in range(count):
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    tags = soup('a')
    url = tags[position-1].get('href', None)
    print url
