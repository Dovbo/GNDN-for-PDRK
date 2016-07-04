import os
import json
import requests

import stepper
import step2_address_validation


class Step3(stepper.Stepper):

    step_settings_var = 'step3'
    results_dir = 'step3_results'
    prev_step_results = step2_address_validation.Step2.results_dir

    coder = 'yandex'
    base_url = "https://geocode-maps.yandex.ru/1.x/?format=json&geocode="

    def yandex(self, address, city_name):
        splitted = [x.strip() for x in address.split(',')]
        url = self.base_url + '%s,+%s,+%s' % (city_name, splitted[0], splitted[1])
        result = requests.get(url, headers=self.headers)
        result = json.loads(result.content.decode('utf8'))
        coords = result['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'].split(' ')
        return [float(x) for x in coords]

    def google(self, address, city_name):
        pass

    def here(self, address, city_name):
        pass

    def get_items(self):
        address_files = os.listdir(self.prev_step_results)
        items = [os.path.join(self.prev_step_results, x) for x in address_files if not x.endswith('_skipped.json')]
        return items

    def process_city(self, filename):
        city_name, addresses = self.json_opener(filename)
        print('process_city ', city_name)

        geojsoned = []
        skipped = {}

        for address, value in addresses.items():
            try:
                coords = getattr(self, self.coder)(address, city_name)
                geojsoned.append({
                    "geometry": {"type": "Point", "coordinates": coords},
                    "type": "Feature",
                    "properties": {"orgs": value['orgs'],
                                   "ADDRESS": address}
                })
            except IndexError:
                skipped[address] = addresses[address]

        geojsoned_final = {"type": "FeatureCollection", "features": geojsoned}

        with open(os.path.join(self.results_dir, city_name + '.geojson'), 'w') as fl:
            fl.write(json.dumps(geojsoned_final, indent=4, ensure_ascii=False))

        with open(os.path.join(self.results_dir, city_name + '_skipped.json'), 'w') as fl:
            fl.write(json.dumps(skipped, indent=4, ensure_ascii=False))

    # def post_process(self):
    #     # get summary file
    #     processed_files = os.listdir(self.results_dir)
    #     items = [os.path.join(self.results_dir, x) for x in processed_files if x.endswith('.geojson')]
    #     summary = []
    #     for item in items:
    #         with open(item, 'r') as fl:
    #             geojson = json.loads(fl.read())
    #         summary.extend(geojson['features'])

    #     final = {"type": "FeatureCollection", "features": summary}
    #     with open(os.path.join(self.results_dir, 'all_cities.geojson'), 'w') as fl:
    #         fl.write(json.dumps(final, indent=4, ensure_ascii=False))


if __name__ == '__main__':
    Step3().launcher()
