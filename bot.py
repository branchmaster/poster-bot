from telegram import Bot
from telegram.ext import Updater
from telegram.ext import Dispatcher

from config import TG_TOKEN


class TelegramBot:
    def __init__(self, tg_token):
        self.tg_token = tg_token

        self.updater = Updater(self.tg_token, workers=4, use_context=True)
        self.dispatcher = self.updater.dispatcher
        self.__last = None
        self.__last_time = None

    def run(self):
        self.updater.start_polling()
        self.updater.idle()

bot = TelegramBot(TG_TOKEN)
