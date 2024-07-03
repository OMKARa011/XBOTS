import logging

from telethon import TelegramClient

from os import getenv
from AltBots.data import ALTRON


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)


# VALUES REQUIRED FOR XBOTS
API_ID = "22674581"
API_HASH = "4482f9af75b0c784ba27905aa72737d9"
CMD_HNDLR = getenv("CMD_HNDLR", default=".")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)

BOT_TOKEN = getenv("BOT_TOKEN", "5822366668:AAEVzM85cDVr-kvcEk0JF8lyXEoNW_VdRPA")
BOT_TOKEN2 = getenv("BOT_TOKEN2", "6563344304:AAFEy2LZe8K0IMxUCfx4jLbmyDoTKQg7YZA")
BOT_TOKEN3 = getenv("BOT_TOKEN3", "6364853958:AAEur1dPP-Bf439H1-YaO7Tavu9nFQ6ZtWc")
BOT_TOKEN4 = getenv("BOT_TOKEN4", "6475527198:AAFc-CW6fZjlWQmUVqBw9r6VO04SjDOoBNk")
BOT_TOKEN5 = getenv("BOT_TOKEN5", "6267420020:AAF993wVJbMiRfNEQ9ppznTTtOf3hL-qJN8")
BOT_TOKEN6 = getenv("BOT_TOKEN6", "6500524583:AAGiBd47WuVvRiP_mAcfM-mnvsXu9LH1nXI")
BOT_TOKEN7 = getenv("BOT_TOKEN7", "5820742464:AAGIelfuaQo71gmKWA9aGGvt-kMqEA3uGPI")
BOT_TOKEN8 = getenv("BOT_TOKEN8", "6240690943:AAFvalNRu5cQKViXQf_QJl4MraOUBbImXf8")
BOT_TOKEN9 = getenv("BOT_TOKEN9", "6447515256:AAE5zEJyE7PLZugg7bgLTTphlpKsouucJhA")
BOT_TOKEN10 = getenv("BOT_TOKEN10", "6417722976:AAHDSk5ykA7QL4pr7Qk4e8MKQgzXUThplsM")

SUDO_USERS = list(map(lambda x: int(x), getenv("SUDO_USERS", default="5935765877").split()))
for x in ALTRON:
    SUDO_USERS.append(x)
OWNER_ID = int(getenv("OWNER_ID", default="5935765877"))
SUDO_USERS.append(OWNER_ID)


# ------------- CLIENTS -------------

X1 = TelegramClient('X1', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
X2 = TelegramClient('X2', API_ID, API_HASH).start(bot_token=BOT_TOKEN2)
X3 = TelegramClient('X3', API_ID, API_HASH).start(bot_token=BOT_TOKEN3)
X4 = TelegramClient('X4', API_ID, API_HASH).start(bot_token=BOT_TOKEN4)
X5 = TelegramClient('X5', API_ID, API_HASH).start(bot_token=BOT_TOKEN5)
X6 = TelegramClient('X6', API_ID, API_HASH).start(bot_token=BOT_TOKEN6)
X7 = TelegramClient('X7', API_ID, API_HASH).start(bot_token=BOT_TOKEN7)
X8 = TelegramClient('X8', API_ID, API_HASH).start(bot_token=BOT_TOKEN8)
X9 = TelegramClient('X9', API_ID, API_HASH).start(bot_token=BOT_TOKEN9)
X10 = TelegramClient('X10', API_ID, API_HASH).start(bot_token=BOT_TOKEN10)
