import json

import discord
from discord.ext import commands

from discord_slash import SlashCommand, SlashContext

from .models import *

config = None

try:
    config = json.laods(open("config.json", "r"))
except:
    exit("config.json not found")

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='-', intents=discord.Intents.all())
slash = SlashCommand(bot, sync_commands=True)

bot.remove_command("help")

radio_stations = config["radio_stations"]


token = config["token"]


current_station = CurrentStation(radio_stations[0]["name"], radio_stations[0]["url"], radio_stations[0]["logo"])
