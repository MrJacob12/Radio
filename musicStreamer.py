from config import radio_stations, bot
from discord import FFmpegPCMAudio
"""Class to stream music from a url"""
class MusicStreamer:
    """
    Initialize the class with the bot and the url to the music
    """
    def __init__(self):
        self.url = None
        self.player = None
        self.volume = 1.0

    def setPlayer(self, player):
        self.player = player

    def play(self, url):
        self.url = url
        self.player.play(FFmpegPCMAudio(self.url))

    def changeRadioStation(self, station):
        self.player.stop()
        self.play(station)

"""Class to stream music from a radio station"""

musicStreamer = MusicStreamer()