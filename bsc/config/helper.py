import json


def get_key_from_file(filename):
    with open(filename, mode='r') as key_file:
        return json.loads(key_file.read())['key']
