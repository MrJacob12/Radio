from discord_slash.utils.manage_commands import create_option

from config import discord, radio_stations, bot, current_station, slash, SlashContext
from musicStreamer import musicStreamer

async def change_status(bot, msg):
    await bot.change_presence(game=discord.Game(name=msg))

#? GET /radio/<station>
@slash.slash(name="stations", description="Get available radio stations", guild_ids=[740664270555185212])
async def _stations(ctx: SlashContext):
    embed=discord.Embed(title="Current radio: {}".format(current_station.name) , description="Available radio stations:", color=0xffffff)
    embed.set_thumbnail(url=radio_stations[0]["logo"])

    for item in radio_stations:
        embed.add_field(name="Title", value=item["name"], inline=False)

    await ctx.send(embed=embed)

#? CHANGE STATION
@slash.slash(name="change", description="Change actual radio station", guild_ids=[740664270555185212], options=[create_option(name="station", description="The radio station to change", required=True, option_type=3, )])
async def _change(ctx: SlashContext, station: str):
    for x in radio_stations:
        if x["name"].lower() == station.lower():
            current_station.set(x["name"], x["url"], x["logo"])
            await bot.change_presence(activity=discord.Game(name="Radio: " + current_station.name))
            musicStreamer.changeRadioStation(x["url"])
            await ctx.send("Radio station changed to {}".format(current_station.name))
            return 0
    await ctx.send("Radio station not found")
