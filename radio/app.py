from .config import token, bot

from .events import *
from .commands import *

def run():
    bot.run(token)
