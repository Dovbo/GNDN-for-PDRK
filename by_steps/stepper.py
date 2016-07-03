import os
import json
import datetime

import local_settings


class Stepper:
    """
    To use class in steps should be defined variables
    'results_dir', 'prev_step_results', 'step_settings_var'
    and methods 'get_items' and 'process_city'.
    Method 'post_process' is optional

    """

    headers = {'User-Agent': 'Corruption Tracker'}

    def ensure_results_dir(self):
        if not os.path.exists(self.results_dir):
            os.makedirs(self.results_dir)

    def json_opener(self, filename):
        city_name = filename.split('/')[1].split('.')[0]
        print('process_city ', city_name)
        with open(filename, 'r') as fl:
            addresses = json.loads(fl.read())
        return city_name, addresses

    def launcher(self):
        self.ensure_results_dir()
        try:
            items = getattr(local_settings, self.step_settings_var)
        except AttributeError:
            items = self.get_items()
            items.sort()
            with open('local_settings.py', 'a') as fl:
                fl.write('\n\n' + self.step_settings_var + '=' + str(items))

        for item in items:
            start = datetime.datetime.now()
            self.process_city(item)
            print(item, 'processed in ', datetime.datetime.now() - start, '\n\n')

        self.post_process()

    def post_process(self):
        pass
