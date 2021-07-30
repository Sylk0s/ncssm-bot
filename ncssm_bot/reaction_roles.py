import discord
import bot_configs as conf



class NcssmBot(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configs = conf.BotConfigs()
        self.token = self.configs.getToken()

        self.role_message_id = 870716858616135680
        self.emoji_to_role = {
            discord.PartialEmoji(name='🅰️'): 870719903664050176, 
            discord.PartialEmoji(name='🅱️'): 870719952527716362,
        }

    async def on_raw_reaction_add(self, TheReaction: discord.RawReactionActionEvent):
        if TheReaction.message_id != self.role_message_id:
            return
        try:
            role_id = self.emoji_to_role[TheReaction.emoji]  
        except KeyError:
            return
        guild = self.get_guild(TheReaction.guild_id)
        role = guild.getrole(role_id)
        await TheReaction.member.add_roles(role)
        

