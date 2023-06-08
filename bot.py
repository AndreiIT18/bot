import logging
from os import name
from telegram.ext import Updater, CommandHandler, MessageHandler, filters


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
level=logging.INFO)
logger = logging.getLogger(name)

def start(Updater, context):
    """Send a message when the command /start is issued."""
    Updater.message.reply_text('start')

def help(Updater, context):
    """Send a message when the command /help is issued."""
    Updater.message.reply_text('Help!')

def echo(Updater, context):
    """Echo the user message."""
    Updater.message.reply_text(Updater.message.text)

def main():
    """Start the bot."""
    Updater = Updater('6207705030:AAGpN6hKdnNWZtPA9MH9VkDzkKEBWYFAV1M', use_context=True)
    dp = Updater.dispatcher

    dp.add_handler(CommandHandler("start",start))

    dp.add_handler(CommandHandler("help", help))

    dp.add_handler(MessageHandler(filters.text, echo))

    Updater.start_polling()
    Updater.idle()

if name == 'main':
    main()