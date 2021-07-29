import json

class BotConfigs():
    def __init__(self):
        self.configJson = json.load(open('configs.json'))

        self.token = self.configJson['token']

    def getToken(self):
        return self.token