import os
import json

import step1_parsing_address
import stepper


class Step2(stepper.Stepper):

    step_settings_var = 'step2'
    results_dir = 'step2_results'
    prev_step_results = step1_parsing_address.Step1.results_dir

    def get_items(self):
        address_files = os.listdir(self.prev_step_results)
        items = [os.path.join(self.prev_step_results, x) for x in address_files if x.endswith('.json')]
        return items

    def process_city(self, filename):
        city_name, addresses = self.json_opener(filename)
        print('process_city ', city_name)
        valid, skipped = {}, {}

        for address in addresses:

            # krov kishki raspidorasilo with addresses
            if not address or \
                not any(c.isalpha() for c in address) or \
                    not any(c.isdigit() for c in address):
                skipped[address] = addresses[address]
            else:
                valid[address] = addresses[address]
            # end of krov kishki raspidorasilo with addresses

        with open(os.path.join(self.results_dir, city_name + '.json'), 'w') as fl:
            fl.write(json.dumps(valid, indent=4, ensure_ascii=False))

        with open(os.path.join(self.results_dir, city_name + '_skipped.json'), 'w') as fl:
            fl.write(json.dumps(skipped, indent=4, ensure_ascii=False))


if __name__ == '__main__':
    Step2().launcher()
