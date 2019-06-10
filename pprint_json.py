import json
import sys


def main():
    if len(sys.argv) == 2:
        path = sys.argv[1]

        with open(path, "r") as file:
            print(json.dumps(json.loads(file.read()),
                             sort_keys=True,
                             indent=4))


if __name__ == "__main__":
    main()
