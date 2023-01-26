import os

class Config(object):
    TG_BOT_TOKEN = os.environ.get("BOT_TOKEN", "5905005671:AAH_pE5TL9TmZJMpLTVASUGggLv00t_U-ug") # Make a bot from https://t.me/BotFather and enter the token here
    
    APP_ID = int(os.environ.get("API_ID", 19911978)) # Get this value from https://my.telegram.org/apps
    
    API_HASH = os.environ.get("API_HASH", "e3f5848d4c384af9e6f1f52ca84c19c7") # Get this value from https://my.telegram.org/apps
    
    OWNER_ID = int(os.environ.get("OWNER_ID", 5826950002

)) # Your(owner's) telegram id
    
    MONGO_STR = os.environ.get("MONGO_STR", "mongodb+srv://Nischaybot:Nischaybot@cluster0.thf9kzz.mongodb.net/?retryWrites=true&w=majority") # Get from MongoDB Atlas

    DOWNLOAD_LOCATION = "app//DOWNLOADS//" # The download location for users. (Don't change anything in this field!)
