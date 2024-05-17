# (c) MRKP BOTS
# A Part of MegaDL-Bot <https://github.com/mrkpbots/MegaDL-Bot>


import os

class Config:
    API_ID = int(os.environ.get("API_ID", 26116576))
    API_HASH = os.environ.get("API_HASH", "f10db65c08a8f32bf81c939c700feb73")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7082653994:AAEeGhOteM2B4nuaUClwOvlWieoBkzKNhEo")
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    TG_MAX_SIZE = 2040108421
    OWNER_ID = int(os.environ.get("OWNER_ID", 6669835291))
    LOG_CHANNEL = 0
    UPDATES_CHANNEL =0


class TEXT:
  ABOUT = """
🤖 **Name:** 


"""

  HELP_USER = """
This is **{bot_name}**

This Bot Can Download Files & Videos From Mega Links & Upload To Telegram. Just Send Any Mega.nz Link & See The Magic. You Can Also Add or Change Caption: Just Select An Uploaded File/ Video or Forward Me Any Telegram File & Then Write The Text You Want To Be Caption On The File As A Reply To That File & The Text You Wrote Will Be Attached As Caption 😁! 

**Made With ❤️ By @mrkpbots! 👑**
"""

  START_TEXT = """
👋🏻 **Hi** {user_mention},

I'm **{bot_name}**
I Can Download Files & Videos From Mega.nz Links & Upload To Telegram. Please Check Help To Learn More 😉!

**Maintained By: {bot_owner}**❤️!
"""
