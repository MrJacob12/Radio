import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='-', intents=discord.Intents.all())
slash = SlashCommand(bot, sync_commands=True)

bot.remove_command("help")

radio_stations = [{"name": "ESKA", "url": "https://uk3-play.adtonos.com/8102/eska-sosnowiec", "logo": "https://www.eska.pl/media/eska/desktop/images/logo-eska.svg"}, {"name": "Radio ZET","url": "https://n-15-5.dcs.redcdn.pl/sc/o2/Eurozet/live/audio.livx", "logo": "https://gfx-player.radiozet.pl/design/player_radiozet/images/logo.svg"} ]


token = "ODgxNDcwMzkzMzUxODA3MDA2.YStTRg.6eQXovlo1UcCz7Wg_vCC3XzRKEI"

class CurrentStation:
    def __init__(self, name, url, logo):
        self.name = name
        self.url = url
        self.logo = logo
    def set(self, name, url, logo):
        self.name = name
        self.url = url
        self.logo = logo
    def get(self):
        return self.name, self.url, self.logo

current_station = CurrentStation(radio_stations[0]["name"], radio_stations[0]["url"], radio_stations[0]["logo"])