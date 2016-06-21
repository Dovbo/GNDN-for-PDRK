# -*- encoding: UTF-8 -*-

# geocoder for ACTS project
# date: Jun 21, 2016
# version: 0.1.0-dev.1

from urllib2 import urlopen
from json import load

def geocoder(list):
    # function gets a list of {name: "OrganizationTitle", address: "OrganizationAddress"}
    # function returns a geojson object
    result = []
    base_url = "https://geocode-maps.yandex.ru/1.x/?format=json&geocode="
    
    # geocoding
    for item in list:
        
        url = base_url + item['address'].replace(' ','+') + '/'
        response = urlopen(url)
        json_obj = load(response)
        result.append(json_obj['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'])
        # responsing json structure:
            # response {}
                # GeoObjectCollection {}
                    # featureMember [] (!!!list!!! "found" check needed)
                        # GeoObject
                            # point {}
    print result
    return result


test_list = [
    {
        "name" : "",
        "address" : "площадь Свободы, 5, (1 подъезд, 2 этаж), Харьков, Харьковская область"
    },
    {
        "name" : "",
        "address" : "улица Цезаря Кюи, 44, Харьков, Харьковская область"
    },
    {
        "name": "",
        "address": "улица Золочевская, 6, Харьков, Харьковская область"
    }
]
coords = geocoder(test_list)
