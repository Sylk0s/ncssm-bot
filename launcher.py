import discord
from ncssm_bot.ncssm_bot import NcssmBot

intents = discord.Intents.all()

bot = NcssmBot(intents=intents)
bot.run(bot.token)