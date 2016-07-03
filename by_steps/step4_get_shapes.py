import os
import json

import step3_get_centroids
import stepper


class Step4(stepper.Stepper):

    step_settings_var = 'step4'
    results_dir = 'step4_results'
    prev_step_results = step3_get_centroids.Step3.results_dir

    def get_items(self):
        address_files = os.listdir(self.prev_step_results)
        items = [os.path.join(self.prev_step_results, x) for x in address_files if not x.endswith('_skipped.json')]
        return items

    def process_city(self, filename):
        city_name, addresses = self.json_opener(filename)
        shaped, skipped = {}, {}

        for address in addresses:
            shaped[address] = addresses[address]
            shaped[address]['shape'] = []

        with open(os.path.join(self.results_dir, city_name + '.json'), 'w') as fl:
            fl.write(json.dumps(shaped, indent=4, ensure_ascii=False))

        with open(os.path.join(self.results_dir, city_name + '_skipped.json'), 'w') as fl:
            fl.write(json.dumps(skipped, indent=4, ensure_ascii=False))

    def post_process(self):
        processed_files = os.listdir(self.results_dir)
        items = [os.path.join(self.results_dir, x) for x in processed_files if not x.endswith('_skipped.json')]
        summary = {}
        for item in items:
                city_name, addresses = self.json_opener(item)
                summary[city_name] = addresses

        with open(os.path.join(self.results_dir, 'step3_summary.json'), 'w') as fl:
            fl.write(json.dumps(summary, indent=4, ensure_ascii=False))

if __name__ == '__main__':
    Step3().launcher()
