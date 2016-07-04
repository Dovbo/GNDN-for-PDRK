import time
import random
import requests

import stepper


class Step1(stepper.Stepper):

    step_settings_var = 'step1'
    results_dir = 'step1_results'

    from parsers import citysites
    parser = citysites.CitySites()

    def __init__(self):
        self.parser.step_settings_var = self.step_settings_var
        self.parser.results_dir = self.results_dir
        self.parser.custom_request = self.custom_request
        self.process_city = self.parser.process_city
        self.get_items = self.parser.get_items

    def custom_request(self, url):
        time.sleep(random.random() / 1000)
        result = requests.get(url, headers=self.headers)
        return result

if __name__ == '__main__':
    Step1().launcher()
