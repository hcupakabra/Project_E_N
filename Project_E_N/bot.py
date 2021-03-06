import logging
import updater
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
    update.message.reply_text("Прежде чем вы начнёте работать ознакомьтесь с правиламиn\n"
                              "За каждый правильный ответ вам будут начисляться баллы\n"
                              "при неправильном ответе вам не начисляются баллы\n"
                              "не пытайтесь писать число больше номера последнего варианта ответа(4)\n"
                              "Оценка выставляется по колличеству баллов:\n"
                              "Оценка 3: 3 балла и меньше\n"
                              "Оценка 4: 4 балла\n"
                              "Оценка 5: пать баллов\n")
    update.message.reply_text("напишите год, в котором вы хотели бы взять пробник(пока, что  есть только 2022 год):")
    return 1


def stop():
    updater.stop


def main():
    updater = Updater('5319178029:AAE_1NA0HviCrZE06xGjPVPDglkPKw2fJEY')
    dp = updater.dispatcher
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            1: [MessageHandler(Filters.text & ~Filters.command, Bot.get_year)],
            2: [MessageHandler(Filters.text & ~Filters.command, Question.ask_a_question)],
        }, fallbacks=[CommandHandler('stop', stop)])
    dp.add_handler(conv_handler)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()