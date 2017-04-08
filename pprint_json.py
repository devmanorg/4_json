import json


def load_data(filepath):
    with open(filepath, mode='r', encoding='utf-8') as my_file:
        json_text = json.load(my_file)
        return json_text


def pretty_print_json(json_text):
    print(json.dumps(json_text, sort_keys=True, indent=4, ensure_ascii=False, separators=(',', ': ')))


if __name__ == '__main__':
    path = input('Enter filepath to your database:')
    try:
        json_text = load_data(path)
    except FileNotFoundError:
        print('File not found, sorry...')
        raise SystemExit
    pretty_print_json(json_text)
