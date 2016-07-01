from urllib.request import urlopen
from urllib.parse import urljoin
from lxml.html import fromstring

import urllib.request
import csv
import re
import time
import random

street_types = [u'улица',u'проспект', u'проезд', u'бульвар', u'площадь', u'переулок', u'квартал', u'шоссе', u'пос', u'тупик', u'набережная', u'ул.', u'вулиця', u'площа', u'шоссе', u'пр.', u'набережна', u'спуск', u'балка', u'пл.', u'мкр.', u'м-н', u'микрорайон', u'пр-т', u'провулок', u'шосе', u'квартал', u'пер.', u'кв.', u'поселок']
PARENT_URL = '<parent url>'
LOCAL_URL = '<local url>'
ITEM_PATH = '<item path>'
RESULTS = 'results.csv'
NO_ADDRESS = 'no_address.csv'
PHONE_ONLY = 'phone_only.csv'

def parse_city():
	for n in range(41):
		req = urllib.request.Request(URL + str(n), headers = {'User-Agent' : 'Corruption Tracker'})
		f = urlopen(req)
		time.sleep(random.random() / 100)
		list_html = f.read().decode('utf-8')
		list_doc = fromstring(list_html)
		#print(list_doc)
		for elem in list_doc.cssselect(ITEM_PATH):
			p = elem.cssselect('p')[0]
			if p.text is None:
				continue
			address = p.text
			a = elem.cssselect('a')[0]
			text_length = len(a.text) - 3
			name  = a.text[0:text_length]
			splitted_address = re.split(',', address)
			
			if splitted_address[0] in  [city_name, 'м. ' + city_name,     'г. ' + city_name, 'м.' + city_name, 'г.' + city_name] and re.split(    ',', address)[1] != '':
				address = splitted_address[1].strip() + ', ' + ','.jo    in(splitted_address[2:])
			elif len(splitted_address) > 2 and splitted_address[1] ==     '':
				address = splitted_address[2].strip() + ', ' + ','.jo    in(splitted_address[3:])
			
			if re.split(' ', address)[0] in street_types:
				with open(RESULTS, 'a') as f:
					f.write('%s\t%s\n' %(name, address))
			elif  address[0] == '+' or address[0] == '(':
				with open(PHONE_ONLY, 'a') as f:
					f.write('%s\t%s\n' %(name, address))
			else:
				with open(NO_ADDRESS, 'a') as f:
					f.write('%s --- %s\n' %(address, name))

parent_req = urllib.request.Request(PARENT_URL, headers = {'User-Agent' : 'Corruption Tracker'})
for site in fromstring(urlopen(parent_req).read()).cssselect('a'):
	current_site = site.cssselect('a')[0].get('href')
	time.sleep(random.random() / 100)

	if re.search('\.ua', current_site) != None:
		print(current_site)

		URL = current_site + LOCAL_URL
		#city name for possible inserting to output file
		title = fromstring(urlopen(URL).read().decode('utf-8')).cssselect('title')[0].text.split()
		time.sleep(random.random() / 100)
		if len(title[2]) > 3 and not title[3][0].isupper():
			city_name = title[2]
		elif len(title[2]) > 3 and title [3][0].isupper():
			city_name = title[2] + ' ' + title[3]
		elif title[4][0].isupper():
			city_name = title[3] + ' ' + title[4]
		else:
			city_name = title[3]
		if city_name in ['Тернопiль', 'Тернопіль']:
			city_name = 'Тернопіль'
		if city_name == 'Чернівців:':
			city_name = 'Чернівці'

		with open(RESULTS, 'a') as f:
			f.write('\n%s\n\n' %(city_name))
		with open(NO_ADDRESS, 'a') as f:
			f.write('\n%s\n\n' %(city_name))
		with open(PHONE_ONLY, 'a') as f:
			f.write('\n%s\n\n' %(city_name))
		print(title, '\n')
		print(u'%s processing...\n' %(city_name))
		parse_city()


if __name__ == '__main__':
	parse_city()
	
