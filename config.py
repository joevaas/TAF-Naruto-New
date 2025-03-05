# Don't Remove Credit @CodeFlix_Bots, @rohit_1888
# Ask Doubt on telegram @CodeflixSupport


import os
from os import environ,getenv
import logging
from logging.handlers import RotatingFileHandler

#rohit_1888 on Tg

#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7427035170:AAHcAW9e83oxpKMSrdB1QqFOGZXhHMJlLug")
#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "25797857"))
#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "77717127ece56fac64ebea6250db8bb7")
#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002093054178"))
# NAMA OWNER
OWNER = os.environ.get("OWNER", "Moon")
#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "6693549185"))
#Port
PORT = os.environ.get("PORT", "8030")
#Database
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://Venkat3823:Venkat3823@cluster0.ig0oc9y.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "Naruto_TAF")

#Time in seconds for message delete, put 0 to never delete
TIME = int(os.environ.get("TIME", "1200"))


#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL1 = int(os.environ.get("FORCE_SUB_CHANNEL1", "-1002005092018"))
#put 0 to disable
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "-1002433169699"))#put 0 to disable
FORCE_SUB_CHANNEL3 = int(os.environ.get("FORCE_SUB_CHANNEL3", "-1002412330704"))#put 0 to disable
FORCE_SUB_CHANNEL4 = int(os.environ.get("FORCE_SUB_CHANNEL4", "-1002448901304"))#put 0 to disable

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

START_PIC = os.environ.get("START_PIC", "https://4kwallpapers.com/images/wallpapers/naruto-uzumaki-3840x2160-18710.jpg")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://ibb.co/2tr6wx6")

# Turn this feature on or off using True or False put value inside  ""
# TRUE for yes FALSE if no 
TOKEN = True if os.environ.get('TOKEN', "False") == "True" else False 
SHORTLINK_URL = os.environ.get("SHORTLINK_URL", "publicearn.online")
SHORTLINK_API = os.environ.get("SHORTLINK_API", "adabe1c0675be8ffc5ccbc84a9a65bc5a5d3ec69")
VERIFY_EXPIRE = int(os.environ.get('VERIFY_EXPIRE', 600)) # Add time in seconds
IS_VERIFY = os.environ.get("IS_VERIFY", "True")
TUT_VID = os.environ.get("TUT_VID","https://t.me/hwdownload/3")


HELP_TXT = "<b><blockquote>ᴛʜɪs ɪs ᴀɴ ғɪʟᴇ ᴛᴏ ʟɪɴᴋ ʙᴏᴛ ᴡᴏʀᴋ ғᴏʀ @Tamil_Anime_Files\n\n❏ ʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅs\n├/start : sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ\n├/about : ᴏᴜʀ Iɴғᴏʀᴍᴀᴛɪᴏɴ\n└/help : ʜᴇʟᴘ ʀᴇʟᴀᴛᴇᴅ ʙᴏᴛ\n\n sɪᴍᴘʟʏ ᴄʟɪᴄᴋ ᴏɴ ʟɪɴᴋ ᴀɴᴅ sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ ᴊᴏɪɴ ʙᴏᴛʜ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ ᴛʜᴀᴛs ɪᴛ.....!\n\n ᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ <a href=https://t.me/Tamil_Aime_Files>Mᴏᴏɴ Wᴀʟᴋᴇʀ</a></blockquote></b>"


ABOUT_TXT = f"""<b>╭───────────⍟
├➽ Dᴇᴠᴇʟᴏᴩᴇʀ : <a href='tg://user?id={6693549185}'>Mᴏᴏɴ</a>
├➽ Lɪʙʀᴀʀy : <a href=https://github.com/pyrogram>Pʏʀᴏɢʀᴀᴍ</a>
├➽ Lᴀɴɢᴜᴀɢᴇ : <a href=https://www.python.org>Pʏᴛʜᴏɴ 3</a>
├➽ Sᴏᴜʀᴄᴇ Cᴏᴅᴇ : <a href=https://t.me/Tamil_Anime_Files>Tᴀᴍɪʟ Aɴɪᴍᴇ Fɪʟᴇs</a>
├➽ Mᴀɪɴ Cʜᴀɴɴᴇʟ : <a href=https://t.me/Tamil_Anime_Files>Tᴀᴍɪʟ Aɴɪᴍᴇ Fɪʟᴇs</a>
├➽ Mᴀɪɴ Gʀᴏᴜᴘ : <a href=https://t.me/Tamil_Anime_Files>Tᴀᴍɪʟ Aɴɪᴍᴇ Fɪʟᴇs</a></b>
╰───────────────⍟ """


START_MSG = os.environ.get("START_MESSAGE", "<b>Hᴇʟʟᴏ {mention}</b>\n\n<b>I Aᴍ Aɴɪᴍᴇ Bᴏᴛ I Wɪʟʟ Gɪᴠᴇ Yᴏᴜ Aɴɪᴍᴇ Fɪʟᴇs Fʀᴏᴍ <a href=https://t.me/Tamil_Anime_Files>Tᴀᴍɪʟ Aɴɪᴍᴇ Fɪʟᴇs</a></b>.")
try:
    ADMINS=[6567976272]
    for x in (os.environ.get("ADMINS", "6567976272").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hᴇʟʟᴏ {mention}\n\n<b>Yᴏᴜ Nᴇᴇᴅ Tᴏ Jᴏɪɴ Iɴ Mʏ Cʜᴀɴɴᴇʟs Tᴏ Gᴇᴛ Aɴɪᴍᴇ Fɪʟᴇs\n\nKɪɴᴅʟʏ Pʟᴇᴀsᴇ Jᴏɪɴ Cʜᴀɴɴᴇʟs\n\nIғ ʏᴏᴜ ᴅᴏɴ'ᴛ ᴋɴᴏᴡ ʜᴏᴡ ᴛᴏ ɢᴇᴛ ғɪʟᴇ ᴄʜᴇᴄᴋ <a href=https://t.me/Tamil_Anime_Files/893>Tᴜᴛᴏʀɪᴀʟ</a></b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "None")

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "ʙᴀᴋᴋᴀ ! ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ꜱᴇɴᴘᴀɪ!!"

ADMINS.append(OWNER_ID)
ADMINS.append(6497757690)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   
