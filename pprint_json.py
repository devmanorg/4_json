import json
import sys


def main():
    if len(sys.argv) == 2:
        path = sys.argv[1]
    else:
        raise Exception('Try again with right format "$ python pprint_json.py <path to file>"')

    file_data = load_file_data(file_path=path)

    try:
        dict_file_data = json.loads(file_data)
    except:
        raise Exception('Data in the current file is not a dictionary')

    print(json.dumps(
        dict_file_data,
        sort_keys=True,
        indent=4))


def load_file_data(file_path):
    try:
        with open(file_path, "r") as file_data:
            return file_data.read()
    except:
        raise Exception('File was not found')


if __name__ == '__main__':
    main()
