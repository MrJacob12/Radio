from discord_slash.utils.manage_commands import create_option

from ..config import discord, radio_stations, bot, current_station, slash, SlashContext, channel
from ..musicStreamer import musicStreamer

@slash.slash(name="change", description="Change actual radio station", guild_ids=[740664270555185212], options=[create_option(name="station", description="The radio station to change", required=True, option_type=3, )])
async def _change(ctx: SlashContext, station: str):
    for x in radio_stations:
        if x["name"].lower() == station.lower():
            current_station.set(x["name"], x["url"], x["logo"])
            await bot.change_presence(activity=discord.Game(name="Radio: " + current_station.name))
            musicStreamer.changeRadioStation(x["url"])
            await ctx.send("Radio station changed to {}".format(current_station.name))
    await ctx.send("Radio station not found")
