import json
import sys
from json import JSONDecodeError


def main():
    if len(sys.argv) == 2:
        path = sys.argv[1]
    else:
        exit('Try again with right format "$ python pprint_json.py <path to file>"')

    file_data = load_file_data(file_path=path)
    if file_data is None:
        exit('File was not found')

    try:
        dict_file_data = json.loads(file_data)
    except JSONDecodeError:
        exit('Data in the current file is not a dictionary')

    print_json_data(dict_file_data)


def print_json_data(dict_file_data):
    print(json.dumps(dict_file_data,
                     sort_keys=True,
                     indent=4,
                     ensure_ascii=False))


def load_file_data(file_path):
    try:
        with open(file_path, "r") as file:
            return file.read()
    except FileNotFoundError:
        return None


if __name__ == '__main__':
    main()
