# -*- coding: utf-8 -*-

# GEOCODER FOR ACTS PROJECT
# Date: Jun 22, 2016
# Version: 0.2.0-dev.2

import sys
import argparse
from urllib2 import urlopen
from json import load, dumps


def SetInputFiles():
    input_files = argparse.ArgumentParser()
    input_files.add_argument ("--file", "-f", nargs = "+", default = ["results.csv"])
    return input_files

def YA_geocode(address):
    coords = []
    base_url = "https://geocode-maps.yandex.ru/1.x/?format=json&geocode="
    url = base_url + address.replace(" ", "+") + "/"
    response = urlopen(url)
    json_obj = load(response)
    list = json_obj['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'].split(" ")
    coords.append(float(list[0]))
    coords.append(float(list[1]))
    return coords
    
if __name__ == "__main__":
    args = SetInputFiles()
    input_files = args.parse_args(sys.argv[1::])
    geojson = {"type": "FeatureCollection", "features": []}
    for filename in input_files.file:
        print filename
        with open(filename, "r") as file:
            reader = file.readline()
            while len(reader) > 0:
                geopoint={
                    "type": "Feature",
                    "properties": {
                        
                    },
                    "geometry": {
                        "type": "Point"
                    }
                }
                if ";" in reader:
                    div = reader.find(";")
                    geopoint["properties"]["address"] = city + ", " + reader[:div]
                    geopoint["properties"]["name"] = reader[div+1:].replace("\n", "")
                    geojson["features"].append(geopoint)
                elif reader != "\n":
                    city = reader.replace("\n", "")
                reader = file.readline()
    for object in geojson['features']:
        address = object['properties']['address']
        object['geometry']['coordinates'] = YA_geocode(address)
    
    writter = dumps(geojson)
    with open("geocode-result.geojson", "w") as file:
        file.write(writter)
