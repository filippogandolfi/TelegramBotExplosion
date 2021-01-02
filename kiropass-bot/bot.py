#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.

"""
Simple Bot to reply to Telegram messages.

First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ChatPermissions

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

impostor = 892604891
tester = 72896167
kiroCounter = 0

# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')

def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')

def echo(update, context):
    """Echo the user message."""
    update.message.reply_text(update.message.text)

def notStonksReply(update, context):
    """Echo the user message."""
    update.message.reply_text(update.message.text)

def stonksReply(update, context):
    """Echo the user message."""
    update.message.reply_text()

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def get_id(update, context):
    yesitstheimpostor = False
    itsabrosky = False
    global kiroCounter
    user = update.message.from_user
    msg = update.message.text
    print('You talk with user {} and his user ID: {} '.format(user['username'], user['id']))
    if user['id'] == impostor:
        yesitstheimpostor = True
        print('CAZZO! ECCO LA MERDA!')
        kiroCounter+=1
    else:
        itsabrosky = True
        print('Finalmento! ECCO UN BRO!')
    
    # on noncommand i.e message - echo the message on Telegram
    if yesitstheimpostor == True:
        update.message.reply_text('KIRO FAI SILENZIO')
        if update.message.text == 'Scusate miei padroni':
            if kiroCounter > 1:
                kiroCounter-=2
        print(kiroCounter)
        if kiroCounter >= 10:
            permission.can_send_messages(impostor,False)
            update.message.reply_text('BENE, VAI FUORI!')
    elif itsabrosky == True:
        print('Tu sei il mio bro')
    #else:
    #    update.message.reply_text('SEI UN HACKER?')
    #   pass
    # if kiroCounter == 10:  
    # 


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("1453858981:AAH5P7sNc-lc07_fwxe0O6ft99iL6q2IFBE", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    
    dp.add_handler(MessageHandler(Filters.text, get_id))
    
    # on noncommand i.e message - echo the message on Telegram
    #if bool(yesitstheimpostor) == True:
    #    dp.add_handler(MessageHandler(Filters.text, notStonksReply))
    #else:
    #    dp.add_handler(MessageHandler(Filters.text, stonksReply))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
