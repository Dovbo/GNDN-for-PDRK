from urllib.request import urlopen
from urllib.parse import urljoin

from lxml.html import fromstring

import csv

import re

URL = 'http://www.0629.com.ua/catalog/41/page/'
ITEM_PATH = '.conteiner .company_box .info'

def parse_courses():
	for n in range(17):
		f = urlopen(URL + str(n))
		list_html = f.read().decode('utf-8')
		list_doc = fromstring(list_html)

		for elem in list_doc.cssselect(ITEM_PATH):
			p = elem.cssselect('p')[0]
			if p.text is None:
				continue
			address = p.text
			if (not (re.match(u'улица', address) or re.match(u'проспект', address) or 
				re.match(u'проезд', address) or re.match(u'бульвар', address) or
				re.match(u'площадь', address) or re.match(u'переулок', address) or
				re.match(u'квартал', address) or re.match(u'шоссе', address) or
				re.match(u'пос', address))):
				# print(address, "\n")
				
				a = elem.cssselect('a')[0]
				text_length = len(a.text) - 3
				name  = a.text[0:text_length]
				
				with open('results.csv', 'a') as f:
					f.write('%s,%s/n' %(name, address))
				
				# org = {'name': name, 'address': address}
			# btn_grey button loader
				# print(org)
			# else:
			#	print('!!!!!!!!!!!!!!!!' + address[0:10])



if __name__ == '__main__':
	parse_courses()
