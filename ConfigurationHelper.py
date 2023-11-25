import json

def get_configuration():
    with open('config.json') as config_file:
        data = json.load(config_file)
        return data
