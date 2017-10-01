import json

with open('config.json') as j:
    Conf = json.load(j)
    Conf = Conf['pyarena']

if __name__ == '__main__':
    print(Config)
