from os import getenv

class Config(object):
      API_HASH = getenv("API_HASH")
      API_ID = int(getenv("API_ID", 0))      
      BOT_TOKEN = getenv("BOT_TOKEN", "")
      CHANNEL = list(x for x in getenv("CHANNEL_ID", "").replace("\n", " ").split(' '))
