import json
import math
from urllib.request import urlopen

km_in_longtitude = 63
km_in_latitude = 111

def load_data(filepath):
    bars_from_url = urlopen(filepath)    
    bar_json = json.loads(bars_from_url.read().decode("utf-8"))
    return list(bar_json['features'])

def get_biggest_bar(bar_list):
    return max(bar_list, 
    key = lambda bar: bar["properties"]["Attributes"]["SeatsCount"])


def get_smallest_bar(bar_list):
    return min(bar_list, 
    key = lambda bar: bar["properties"]["Attributes"]["SeatsCount"])


def get_distance_to_bar(bar, longitude, latitude):
    x_diff = (longitude-bar["geometry"]["coordinates"][0])*km_in_longtitude
    y_diff = (latitude-bar["geometry"]["coordinates"][1])*km_in_latitude
    return (math.sqrt((x_diff**2)+(y_diff**2)))

def get_closest_bar(bar_list, longitude, latitude):
    return min(bar_list, 
    key = lambda bar: get_distance_to_bar(bar, longitude, latitude))


if __name__ == '__main__':
    url_bars_list = "{0}{1}{2}{3}".format(
        "https://devman.org/media/",
        "filer_public/95/74/", 
        "957441dc-78df-4c99-83b2-e93dfd13c2fa/",
        "bars.json")
    bar_list = load_data(url_bars_list)

    biggest_bar = get_biggest_bar(bar_list)
    smallest_bar = get_smallest_bar(bar_list)
    longitude = float(input("Input longitude  "))
    latitude = float(input("Input latitude  "))
    closest_bar = get_closest_bar(bar_list, longitude, latitude)
    print()
    print()
    print("Biggest bar")
    print("-------------------------------")
    print(biggest_bar["properties"]["Attributes"]["Name"])
    print("-------------------------------")
    print()
    print()
    print("Smallest bar")
    print("-------------------------------")
    print(smallest_bar["properties"]["Attributes"]["Name"])
    print("-------------------------------")
    print()
    print()
    print("Closest bar")
    print("-------------------------------")
    print(closest_bar["properties"]["Attributes"]["Name"])
    print()
    print()
