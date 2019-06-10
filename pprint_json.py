# !/usr/bin/python
# -*- coding: UTF-8 -*-
import json
import sys


def main():
    if len(sys.argv) == 2:
        path = sys.argv[1]
        file_dict = open(path, "r").read()

        print(json.dumps(json.loads(file_dict), sort_keys=True, indent=4))

    else:
        print("Необходимо передать путь к json файлу в формате: python pprint_json.py <path to file>")

    return 0


if __name__ == "__main__":
    main()
