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

    async def on_raw_reaction_add(self, theReaction: discord.RawReactionActionEvent):
        if theReaction.message_id != self.role_message_id:
            return
        try:
            role_id = self.emoji_to_role[theReaction.emoji]  
        except KeyError:
            return
        guild = self.get_guild(theReaction.guild_id)
        role = guild.get_role(role_id)
        await theReaction.member.add_roles(role)

    async def on_raw_reaction_remove(self, reaction: discord.RawReactionActionEvent):
        if reaction.message_id != self.role_message_id:
            return
        try:
            role_id = self.emoji_to_role[reaction.emoji]  
        except KeyError:
            return
        guild = self.get_guild(reaction.guild_id)
        role = guild.get_role(role_id)
        member = guild.get_member(reaction.user_id)
        await member.remove_roles(role)

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
   