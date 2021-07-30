import discord
import ncssm_bot

intents = discord.Intents.default()
intents.members = True

bot = ncssm_bot.NcssmBot(intents=intents)
bot.run(bot.token)