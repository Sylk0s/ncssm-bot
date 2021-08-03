from discord.ext.commands import Bot
from ncssm_bot.bot_configs import BotConfigs
from ncssm_bot.reaction_roles import ReactionRoles


class NcssmBot(Bot):
    def __init__(self, *args, **kwargs):
        self.configs = BotConfigs()
        self.token = self.configs.getToken()
        self.guild = None
        self.prefix = self.configs.getPrefix()

        super().__init__(*args, **kwargs, command_prefix=self.prefix)

    async def on_ready(self):
        print(f'Logged on as {self.user}!')
        self.guild = self.get_guild(self.configs.getGuildId())
        self.add_cog(ReactionRoles(self))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
   