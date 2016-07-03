import os
import time
import random
import json
from bs4 import BeautifulSoup
import requests

import stepper
import local_settings


class Step1(stepper.Stepper):

    step_settings_var = 'step1'
    results_dir = 'step1_results'

    def custom_request(self, url):
        time.sleep(random.random() / 1000)
        result = requests.get(url, headers=self.headers)
        return result

    def get_items(self):
        print('getting cities...')
        result = self.custom_request(local_settings.root_url)
        soup = BeautifulSoup(result.content, "html.parser")
        urls = [x.find('a').get('href') for x in soup.find_all("div", "text")]
        items = [x for x in urls if x.endswith('ua')]
        return items

    def process_city(self, url):
        main_page = self.custom_request(url + '/catalog')
        main_soup = BeautifulSoup(main_page.content, "html.parser")
        city_name = main_soup.find_all(attrs={"name": "keywords"})[0].get('content').split(' ')[2]
        print('process_city ', city_name, url)

        # url is always same, /catalog/41 , but in case if not:

        # state_services = main_soup.find_all('span', text='Городские службы')
        # if not state_services:
        #     state_services = main_soup.find_all('span', text='Міські служби')
        # state_services_url = state_services[0].parent.get('href')

        service_categories = main_soup.find_all("div", {'data-pid': "41"})[0].find_all('a')
        with open(os.path.join(self.results_dir, city_name + '_no_address.csv'), 'w') as no_address_fl:
            services = {}

            for category in service_categories:
                category_name = category.find_all('span')[0].get_text()
                category_url = url + category.get('href')
                print('process category:', category_name, category_url)

                category_page = self.custom_request(category_url)
                category_soup = BeautifulSoup(category_page.content, "html.parser")
                service_boxes = category_soup.find_all('div', "company_box")
                next_page = category_soup.find_all("a", "btn_grey button loader")
                while True:
                    if next_page:
                        category_page = self.custom_request(url + next_page[0].get('href'))
                        category_soup = BeautifulSoup(category_page.content, "html.parser")
                        next_page = category_soup.find_all("a", "btn_grey button loader")
                        service_boxes.extend(category_soup.find_all('div', "company_box"))
                    else:
                        break

                for service in service_boxes:
                    name = service.find_all('a')[0].get_text().strip()
                    try:
                        address = service.find_all('div', 'contacts gray_box rounding')[0].find_all('p')[0].get_text()
                        if not address or \
                            not any(c.isalpha() for c in address) or \
                                not any(c.isdigit() for c in address):

                            service_row = '%s|%s|%s\n' % (
                                name, address, category_name)
                            no_address_fl.write(service_row)

                        else:
                            for single_address in address.split('\r\n'):
                                if single_address in services:
                                    services[single_address]['orgs'].append({
                                        'name': name,
                                        'category': category_name
                                    })
                                else:
                                    services[single_address] = {}
                                    services[single_address]['orgs'] = [{
                                        'name': name,
                                        'category': category_name
                                    }]

                    except IndexError:
                        service_row = '%s|%s|%s\n' % (
                            name, '', category_name)
                        no_address_fl.write(service_row)

            with open(os.path.join(self.results_dir, city_name + '.json'), 'w') as fl:
                fl.write(json.dumps(services, indent=4, ensure_ascii=False))


if __name__ == '__main__':
    Step1().launcher()
