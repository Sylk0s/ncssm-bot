from discord.ext.commands import Cog, command
from discord import Embed

class BotInfo(Cog):
    def __init__(self, bot):
        self.bot = bot

    @command(name="info")
    async def get_info(self, ctx):

        print("works")

        infoEmbed = Embed(
            title="NCSSM Bot Info", 
            description=f"A discord bot written by a few NCSSM online students for the NCSSM online discord. Use {self.bot.prefix}help for info about specific uses",
            colour=0x8090f0,
            )
        infoEmbed.add_field(name="Developers: ", value=f"{self.bot.guild.get_member(403610859370446851).mention}\n{self.bot.guild.get_member(867105239273046066).mention}\n{self.bot.guild.get_member(409739691219222528).mention}", inline=False)

        await ctx.channel.send(embed=infoEmbed)

    @command(name="hello")
    async def say_hello(self, ctx):
        await ctx.send(f"Hello {ctx.author.mention}!")