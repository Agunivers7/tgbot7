from tg_bot.sample_config import Config


class Development(Config):
    OWNER_ID = 1323557247  # my telegram ID
    OWNER_USERNAME = "@Spoidermon12"  # my telegram username
    API_KEY = "5546235142:AAGUa1r-5_N1joxXLWDvcjf8uUJjs2SgShA"  # my api key, as provided by the botfather
    SQLALCHEMY_DATABASE_URI = 'postgres://apex:aadhi@8.219.177.252:5432/apexdb'  # sample db credentials
    MESSAGE_DUMP = '-1234567890' # some group chat that your bot is a member of
    USE_MESSAGE_DUMP = True
    SUDO_USERS = [18673980, 83489514]  # List of id's for users which have sudo access to the bot.
    LOAD = []
    NO_LOAD = ['translation']
