import json


def load_data(filepath):
    with open(filepath, mode='r', encoding='utf-8') as my_file:
        data = json.load(my_file)
        return data


def pretty_print_json(data):
    print(json.dumps(data, sort_keys=True, indent=4, separators=(',', ': ')))


if __name__ == '__main__':
    print('Enter filepath to your database:')
    path = input()
    try:
        data = load_data(path)
    except FileNotFoundError:
        print('File not found, sorry...')
        raise SystemExit
    pretty_print_json(data)
