import logging

from telegram.ext import Updater, CommandHandler

from bot import bot
from handlers.commands import start
from jobs.sample import broadcast_job

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

def main():
    bot.dispatcher.add_handler(CommandHandler('start', start))

    bot.run()


if __name__ == '__main__':
    main()
