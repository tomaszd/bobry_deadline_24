'''
Created on 24 lut 2016

@author: opera
'''
import requests
from BeautifulSoup import BeautifulSoup
url = "http://www.magiccardmarket.eu/?mainPage=showSearchResult&searchFor="

karta = "Tarmogoyf"
full_url = url + karta
data = requests.get(full_url)
soup = BeautifulSoup(data.text)
print "type(soup)", type(soup)
len(soup.findAll('tr')[2].findAll('td'))
card_details = {}
# for example in soup.findAll('tr')[2].findAll('td') :
#  thumb, expan, rarity, img, href, singles, avail, price
#  print i
thumb, expan, rarity, href, comment, singles, avail, price = soup.findAll('tr')[2].findAll('td')
print "thumb", thumb
print "expan", expan
print "rarity", rarity
print "href", href
print "comment", comment
print "singles", singles
print "avail", avail
print "price", price


import pdb
pdb.set_trace()
