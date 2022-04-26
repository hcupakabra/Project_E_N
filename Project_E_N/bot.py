import logging

import dp as dp
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, ReplyKeyboardMarkup
from telegram.ext import *
import sqlite3
from telebot import *
from telegram.ext import updater
from main import *

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
conn = sqlite3.connect('table.db')
logger = logging.getLogger(__name__)
states = {}


def start(update: Update, context: CallbackContext):
    user = update.message.from_user
    logger.info("User %s started the conversation.", user.first_name)
    update.message.reply_text("Привет, я Телеграм-бот."
                              " Твой личный репетитор по обществу."
                              "Давайте начнем")
    update.message.reply_text("напишите год, в котором вы хотели бы взять пробник:")
    return 1


def end(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    query.edit_message_text(text="See you next time!")
    return ConversationHandler.END


def stop():
    updater.stop


def main():
    updater = Updater('5319178029:AAHAWCy4ecGfQoXNh5v7YG2M7DWKow69WhA')
    dp = updater.dispatcher
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            1: [MessageHandler(Filters.text & ~Filters.command, Question.year)],
            2: [MessageHandler(Filters.text & ~Filters.command, Question.answer)],
            3: [MessageHandler(Filters.text & ~Filters.command, Question.answer)]
        }, fallbacks=[CommandHandler('stop', stop)])
    dp.add_handler(conv_handler)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
