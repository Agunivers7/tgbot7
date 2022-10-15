class Config(object):
    LOGGER = True

    # REQUIRED
    API_KEY = "5546235142:AAGUa1r-5_N1joxXLWDvcjf8uUJjs2SgShA"
    OWNER_ID = "1323557247"  # If you dont know, run the bot and do /id in your private chat with it
    OWNER_USERNAME = "Spoidermon12"

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = 'postgres://apex:aadhi@8.219.177.252:5432/apexdb'  # needed for any database modules
    MESSAGE_DUMP = None  # needed to make sure 'save from' messages persist
    LOAD = []
    NO_LOAD = ['translation', 'rss']
    WEBHOOK = False
    URL = None

    # OPTIONAL
    SUDO_USERS = [1323557247]  # List of id's (not usernames) for users which have sudo access to the bot.
    SUPPORT_USERS = [1323557247]  # List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    WHITELIST_USERS = [1323557247]  # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = False  # Whether or not you should delete "blue text must click" commands
    STRICT_GBAN = False
    WORKERS = 8  # Number of subthreads to use. This is the recommended amount - see for yourself what works best!
    BAN_STICKER = 'CAADAgADOwADPPEcAXkko5EB3YGYAg'  # banhammer marie sticker
    ALLOW_EXCL = False  # Allow ! commands as well as /
    BMERNU_SCUT_SRELFTI = 0

class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True
