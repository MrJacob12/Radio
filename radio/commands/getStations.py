from radio.config import discord, radio_stations, bot, current_station, slash, SlashContext


@slash.slash(name="stations", description="Get available radio stations", guild_ids=[740664270555185212])
async def _stations(ctx: SlashContext):
    embed=discord.Embed(title="Current radio: {}".format(current_station.name) , description="Available radio stations:", color=0xffffff)
    embed.set_thumbnail(url=radio_stations[0]["logo"])

    for item in radio_stations:
        embed.add_field(name="Title", value=item["name"], inline=False)

    await ctx.send(embed=embed)
