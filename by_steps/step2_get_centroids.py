import os
import copy
import json
import step1_parsing_address

headers = {'User-Agent': 'My User Agent 1.0'}
results_dir = 'step2_results'

if not os.path.exists(results_dir):
    os.makedirs(results_dir)


def get_centroids(filename):


    city_name = filename.split('/')[1].split('.')[0]
    print(city_name)




def launcher():

    address_files = os.listdir(step1_parsing_address.results_dir)
    address_jsons = [os.path.join(step1_parsing_address.results_dir,
        x) for x in address_files if x.endswith('.json')]

    # for address_json in address_jsons:
    #     get_centroids(address_json)


    get_centroids('step1_results/Львів.json')


if __name__ == '__main__':
    launcher()