from urllib.request import urlopen
from urllib.parse import urljoin

from lxml.html import fromstring

import csv

import re

def parse_city():
	for n in range(17):
		f = urlopen(URL + str(n))
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

			if ((re.match(u'улица', address) or re.match(u'проспект', address) or 
				re.match(u'проезд', address) or re.match(u'бульвар', address) or
				re.match(u'площадь', address) or re.match(u'переулок', address) or
				re.match(u'квартал', address) or re.match(u'шоссе', address) or
				re.match(u'пос', address))):
	
				with open('results.csv', 'a') as f:
					f.write('%s,%s\n' %(name, address))
		
			else:
				with open('no_address.csv', 'a') as f:
					f.write('%s --- %s\n' %(name, address)) 

PARENT_URL = 'http://citysites.ua/ua/city/'
for site in fromstring(urlopen(PARENT_URL).read()).cssselect('a'):
	current_site = site.cssselect('a')[0].get('href')

	if re.search('\.ua', current_site) != None:
		print(current_site)

		URL = current_site + '/catalog/41/page/'
		ITEM_PATH = '.conteiner .company_box .info'

		#city name for possible inserting to output file
		title = fromstring(urlopen(URL).read().decode('utf-8')).cssselect('title')[0].text.split()
		if len(title[2]) > 3:
			city_name = title[2]
		else:
			city_name = title[3]

		with open('results.csv', 'a') as f:
			f.write('\n%s\n\n' %(city_name))
		with open('no_address.csv', 'a') as f:
			f.write('\n%s\n\n' %(city_name))
		print(u'%s processing...\n' %(city_name))
		parse_city()


if __name__ == '__main__':
	parse_city()
