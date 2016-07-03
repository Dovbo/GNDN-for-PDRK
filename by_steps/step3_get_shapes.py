import os
import json

import step2_get_centroids

headers = {'User-Agent': 'Corruption Tracker'}
results_dir = 'step3_results'

if not os.path.exists(results_dir):
    os.makedirs(results_dir)


def process_city(filename):
    city_name = filename.split('/')[1].split('.')[0]
    print('process_city ', city_name)
    with open(filename, 'r') as fl:
        addresses = json.loads(fl.read())

    shaped = {}
    skipped = {}

    for address in addresses:
        shaped[address] = addresses[address]
        shaped[address]['shape'] = []

    with open(os.path.join(results_dir, city_name + '.json'), 'w') as fl:
        fl.write(json.dumps(shaped, indent=4, ensure_ascii=False))

    with open(os.path.join(results_dir, city_name + '_skipped.json'), 'w') as fl:
        fl.write(json.dumps(skipped, indent=4, ensure_ascii=False))


def launcher():

    address_files = os.listdir(step2_get_centroids.results_dir)
    address_jsons = [os.path.join(step2_get_centroids.results_dir,
        x) for x in address_files if not x.endswith('skipped.json')]

    for address_json in address_jsons:
        process_city(address_json)

    # process_city('step2_results/Львів.json')


if __name__ == '__main__':
    launcher()
