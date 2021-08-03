import discord
from discord.ext.commands import Cog, command

class ReactionRoles(Cog):
    def __init__(self, bot):
        self.bot = bot

        self.role_message_id = self.bot.configs.getRoleMessageId()
        self.emoji_to_role = {
            discord.PartialEmoji(name='🅰️'): 870719903664050176, 
            discord.PartialEmoji(name='🅱️'): 870719952527716362,
        }

    @Cog.listener()
    async def on_raw_reaction_add(self, reaction: discord.RawReactionActionEvent):
        if reaction.message_id != self.role_message_id:
            return
        try:
            role_id = self.emoji_to_role[reaction.emoji]  
        except KeyError:
            return
        role = self.bot.guild.get_role(role_id)
        print(role)
        await reaction.member.add_roles(role)

    @Cog.listener()
    async def on_raw_reaction_remove(self, reaction: discord.RawReactionActionEvent):
        if reaction.message_id != self.role_message_id:
            return
        try:
            role_id = self.emoji_to_role[reaction.emoji]  
        except KeyError:
            return
        role = self.bot.guild.get_role(role_id)
        member = self.bot.guild.get_member(reaction.user_id)
        await member.remove_roles(role)