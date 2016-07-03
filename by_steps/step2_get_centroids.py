import os
import json
import requests

import step1_parsing_address

headers = {'User-Agent': 'Corruption Tracker'}
results_dir = 'step2_results'

if not os.path.exists(results_dir):
    os.makedirs(results_dir)


def process_city(filename):
    city_name = filename.split('/')[1].split('.')[0]
    print('process_city ', city_name)
    with open(filename, 'r') as fl:
        addresses = json.loads(fl.read())

    base_url = "https://geocode-maps.yandex.ru/1.x/?format=json&geocode="
    centroided = {}
    skipped = {}

    for address in addresses:
        splitted = [x.strip() for x in address.split(',')]
        print(splitted)
        if len(splitted) == 2:
            url = base_url + '%s,+%s,+%s' % \
                (city_name, splitted[0], splitted[1])
            result = requests.get(url, headers=headers)
            print(result)
            result = json.loads(result.content.decode('utf8'))
            coords = result['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'].split(' ')
            print(coords)

            centroided[address] = addresses[address]
            centroided[address]['centroid'] = ','.join(coords)
        else:
            skipped[address] = addresses[address]

    with open(os.path.join(results_dir, city_name + '.json'), 'w') as fl:
        fl.write(json.dumps(centroided, indent=4, ensure_ascii=False))

    with open(os.path.join(results_dir, city_name + '_skipped.json'), 'w') as fl:
        fl.write(json.dumps(skipped, indent=4, ensure_ascii=False))


def launcher():

    address_files = os.listdir(step1_parsing_address.results_dir)
    address_jsons = [os.path.join(step1_parsing_address.results_dir,
        x) for x in address_files if x.endswith('.json')]

    for address_json in address_jsons:
        process_city(address_json)

    # process_city('step1_results/Львів.json')


if __name__ == '__main__':
    launcher()
