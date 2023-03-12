import os
import nextcord
from nextcord.ext import commands
import json

bot = commands.Bot(command_prefix='rls!', case_insensitive=True, help_command=None, intents=nextcord.Intents.all(), activity=nextcord.Activity(name="rls!help | Whitelisting Made Easy", type=nextcord.ActivityType.watching), status=nextcord.Status.online)

with open("C:/Users/steph/Desktop/Coding/RLS/config/config.json") as f:
    config = json.load(f)

for filename in os.listdir("./src/app/cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"src.app.cogs.{filename[:-3]}")
        print(f"INFO: Loaded {filename[:-3]}")

bot.run(config["BOT_TOKEN"])
