# Import regex
import re
# Importing the logging.
import logging
import random
# importing the updater from the python-telegram-bot library.
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, RegexHandler
from PIL import Image

# setting up the logger.
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)
# declare an updater variable as NULL.
updater = None

# the telegram tokken (note: import via file)
token = "793027805:AAFP4_GRAX86K-RkabVuAwRN4MynoC4ov1U"


def main():
    print("Starting bot...", end='')
    global updater
    updater = Updater(token)
    dispatcher = updater.dispatcher

    # register handlers/functions
    dispatcher.add_handler(CommandHandler('owo', owo_command))
    dispatcher.add_handler(CommandHandler('meme', meme))
    dispatcher.add_handler(CommandHandler('image', image))

    # MessageHandler
    dispatcher.add_handler(RegexHandler(re.compile("owo", re.IGNORECASE), owo))

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
    myImage = Image.open("https://d.facdn.net/art/meheheehehe/1548275203/1548275203.meheheehehe_79.jpg")
    update.message.reply_text(myImage)


# logs bot errors thrown
def error(bot, update, error):
    logger.warning('Update "{}" caused error "{}"'.format(update, error))


if __name__ == '__main__':
    main()
