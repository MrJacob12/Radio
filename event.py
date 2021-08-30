from discord import player
from termcolor import colored
from config import bot, radio_stations, discord
from musicStreamer import musicStreamer

@bot.event
async def on_ready():
    print(colored(f'{bot.user} has connected to Discord!','green'))
    channel = bot.get_channel(881466889006641152)
    musicStreamer.setPlayer(await channel.connect())
    musicStreamer.play(radio_stations[0]["url"])
    await bot.change_presence(activity=discord.Game(name="Radio: " + radio_stations[0]["name"]))
