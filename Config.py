import json

with open('config.json') as j:
    Config = json.load(j)

if __name__ == '__main__':
    print(Config)
