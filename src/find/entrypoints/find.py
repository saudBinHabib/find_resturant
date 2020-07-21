
# Imports
import argparse
import json
import os
import urllib.request


def locu_search(city: str, key: str) -> list:
    '''
    :param city: this method takes the city name as a string
    :param key: key as a string
    :return: and return the list of the restaurants with restaurant name and contact number as a set..
    '''

    url = 'https://api.locu.com/v1_0/venue/search/?api_key=' + key
    locality = city.replace(' ', '%20')
    final_url = url + "&locality=" + locality + "&category=restaurant"
    response_object = urllib.request.urlopen(final_url)
    response_object = json.load(response_object)

    return [(restaurant.get('name'), restaurant.get('phone')) for restaurant in response_object['objects']]


def entrypoint():
    '''
    This is the function which will be called by the console script to print the restaurants of a city.
    '''

    parser = argparse.ArgumentParser(description='Argument Parser for the image directories.')
    parser.add_argument('--city', type=str, required=True)
    args = parser.parse_args()
    city = args.city
    key = os.environ.get('LOCU_ACCESS_TOKEN')
    restaurant_list = locu_search(city, key)
    if restaurant_list:
        for restaurant in restaurant_list:
            print('Restaurant Name: ', restaurant[0], ' Contact Number: ', restaurant[1], '\n')
    else:
        print('We don\'t have any restaurant located in this city.')
