from termcolor import colored
from ..config import bot, radio_stations, discord, channel
from ..musicStreamer import musicStreamer

@bot.event
async def on_ready():
    print(colored(f'{bot.user} has connected to Discord!','green'))
    channel_ = bot.get_channel(channel)
    musicStreamer.setPlayer(await channel_.connect())
    musicStreamer.play(radio_stations[0]["url"])
    await bot.change_presence(activity=discord.Game(name="Radio: " + radio_stations[0]["name"]))