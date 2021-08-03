import json

class BotConfigs():
    def __init__(self):
        self.configJson = json.load(open('configs.json'))

        self.token = self.configJson['token']
        self.guild_id = int(self.configJson['guild_id'])
        self.role_message_id = int(self.configJson['role_message_id'])
        self.prefix = self.configJson['prefix']

    def getToken(self):
        return self.token

    def getGuildId(self):
        return self.guild_id

    def getRoleMessageId(self):
        return self.role_message_id

    def getPrefix(self):
        return self.prefix