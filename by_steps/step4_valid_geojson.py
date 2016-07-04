import os
import json

import step3_get_centroids
import stepper
from orgtypes import ORG_TYPES, ORG_TYPES_MATCHER


class Step4(stepper.Stepper):

    step_settings_var = 'step4'
    results_dir = 'step4_results'
    prev_step_results = step3_get_centroids.Step3.results_dir

    def get_items(self):
        address_files = os.listdir(self.prev_step_results)
        items = [os.path.join(self.prev_step_results, x) for x in address_files if x.endswith('.geojson')]
        return items

    def process_city(self, filename):
        city_name, geoobjects = self.json_opener(filename)
        print('process_city ', city_name)

        for item in geoobjects['features']:
            if 'address' in item['properties']:
                item['properties']['ADDRESS'] = item['properties'].pop('address')
            item['properties']['ID'] = None
            item['properties']['PARENT'] = None
            item['properties']['CENTROID'] = None

            org_types = []
            org_names = []
            orgs = item['properties'].pop('orgs')
            for org in orgs:
                if org['category'] in ORG_TYPES_MATCHER:
                    org_types.append(ORG_TYPES_MATCHER[org['category']])
                    org_names.append(org['name'])

                else:
                    raise Exception('Not recognized organization type: %s' %org['category'])

            item['properties']['ORG_TYPES'] = '|'.join(org_types)
            item['properties']['ORG_NAMES'] = '|'.join(org_names)

        with open(os.path.join(self.results_dir, city_name + '.geojson'), 'w') as fl:
            fl.write(json.dumps(geoobjects, indent=4, ensure_ascii=False))

        # exit()

    def post_process(self):
        processed_files = os.listdir(self.results_dir)
        items = [os.path.join(self.results_dir, x) for x in processed_files if not x.endswith('_skipped.json')]
        summary = {}
        for item in items:
                city_name, addresses = self.json_opener(item)
                summary[city_name] = addresses

        with open(os.path.join(self.results_dir, 'all_cities.geojson'), 'w') as fl:
            fl.write(json.dumps(summary, indent=4, ensure_ascii=False))

if __name__ == '__main__':
    Step4().launcher()
