#!/usr/bin/python3
import urllib.request
from bs4 import BeautifulSoup
import re

def get_html(url):
	response = urllib.request.urlopen(url)
	return response.read()

def parse(html):
	soup = BeautifulSoup(html, "lxml")
	table = soup.find('tbody')
	
	people = []
	for row in table.find_all('tr')[1:]:
		cols = row.find_all('td')
		
		if cols[1].text == None or cols[2].a == None or cols[2].text == None:
			continue
		name = cols[2].text.strip()
		if name[len(name) - 1] not in [u'а', u'ч']:
			name = name[:len(name) - 1]
		date = cols[1].text.strip()
		
		link = 'http://marsovet.org.ua' + str(cols[2].a).split('"')[1]
		people.append({
			'name': name,
			'date': date,
			'link': link
		})
	print(people[0])
	return people
def parse_people(they):
	for heshe in they: #TODO we need enter every link and check conclusion for words 'не підлягає' or something similar
		print('%s\n%s\n\n' %(heshe['name'], heshe['link']))
	
def main():
	people = parse(get_html('http://marsovet.org.ua/articles/show/menu/1899'))
	parse_people(people)
if __name__ == '__main__':
	main()
