# (c) @AbirHasan2005

import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", 12345))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    SESSION_NAME = os.environ.get("SESSION_NAME", "Captcha-Bot")
    MONGODB_URI = os.environ.get("MONGODB_URI", "")
    OWNER_ID = int(os.environ.get("OWNER_ID", 1995544704)
    GROUP_CHAT_ID = int(os.environ.get("GROUP_CHAT_ID", -100))
    CAPTCHA_API_TOKEN = os.environ.get("CAPTCHA_API_TOKEN", "")
