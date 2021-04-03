from bs4 import BeautifulSoup
import urllib.request
import re
import requests
import sys

link = 'http://www.cbr.ru/scripts/XML_daily.asp'
request = urllib.request.urlopen(link)
xml = BeautifulSoup(request, 'xml')


def currency_rates(id=None, CharCode = None,  link = link):
    r = requests.get(link)
    date = re.split('ValCurs | name=', str(r.content))
    #print(r.content)

    for item in xml.findAll('CharCode'):

        if item.text == f"{CharCode}":
            return re.split('>|<', str(list(item.next_siblings)[2]))[2], date[1]



try:
  print(*currency_rates(CharCode = "{}".format(sys.argv[1])))

except:
    print('Enter a valid Charcode')
