# Import regex
import re
# Importing the logging (prints to console).
import logging
import random
from PIL import Image
import os
import json
# importing the updater from the python-telegram-bot library.
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, RegexHandler

# setting up the logger.
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)
# declare an updater variable as NULL.
updater = None
config = None


# the telegram token (note: import via file)
# load config from file
def load_config():
    dir = os.path.dirname(__file__)
    path = os.path.join(dir, 'token.json')
    with open(path) as config_file:
        global config
        config = json.load(config_file)
        config_file.close()


def main():
    print("Starting bot...", end='')
    load_config()
    global updater
    updater = Updater(config["token"])
    dispatcher = updater.dispatcher

    # register handlers/functions
    dispatcher.add_handler(CommandHandler('owo', owo_command))
    dispatcher.add_handler(CommandHandler('meme', meme))
    dispatcher.add_handler(CommandHandler('image', image))

    # MessageHandler
    dispatcher.add_handler(RegexHandler(re.compile("owo", re.IGNORECASE), owo_command))
    dispatcher.add_handler(MessageHandler(Filters.photo, image_received))

    # register error handler
    dispatcher.add_error_handler(error)

    updater.start_polling(clean=True, timeout=99999)

    print("Done")

    updater.idle()


def owo_command(bot, update):
    file = open("text.txt", "r")
    lines = [line.rstrip() for line in file.readlines()]
    update.message.reply_text(random.choice(lines))
    file.close()


def meme(bot, update):
    x = random.randint(0, 200)
    link = "http://t.me/furrymemes/"
    link += str(x)
    update.message.reply_text(link)


def image(bot, update):
    # myImage = Image.open("https://d.facdn.net/art/meheheehehe/1548275203/1548275203.meheheehehe_79.jpg")
    file = open("")
    update.message.reply_photo("AgADBAADE7AxGzXLWVB7eLaPCkE1KvtlwxoABHWQqs-nYXtCMQ4FAAEC")


def image_received(bot, update):
    message = update.message
    message.reply_text(message.photo[-1].file_id)


# logs bot errors thrown
def error(bot, update, error):
    logger.warning('Update "{}" caused error "{}"'.format(update, error))


if __name__ == '__main__':
    main()
