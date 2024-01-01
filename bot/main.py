##############################################
##### AUTHOR: JOÃO PEDRO AVEIRO ##############
##### GITHUB: github.com/jp-aveiro ###########
##############################################

import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

bot = commands.Bot(intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

if __name__ == "__main__":
    # Initialize events
    for filename in os.listdir("bot/cogs/events/"):
        if filename.endswith(".py"):
            bot.load_extension(f"cogs.events.{filename[:-3]}")

    # Initialize commands
    for filename in os.listdir("bot/cogs/commands/"):
        if filename.endswith(".py"):
            bot.load_extension(f"cogs.commands.{filename[:-3]}")

    bot.run(os.getenv("TOKEN"))