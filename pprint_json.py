import json
from pprint import pprint

def load_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as fh:
        data = json.load(fh)
    return data


def pretty_print_json(data):
    return pprint(data)

if __name__ == '__main__':
    data = load_data('G:/playground/alco_shops.json')
    pretty_print_json(data)