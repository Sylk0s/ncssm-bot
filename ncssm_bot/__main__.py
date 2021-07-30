import discord
import ncssm_bot

intents = discord.Intents.default()

bot = ncssm_bot.NcssmBot(intents=intents)
bot.run(bot.token)