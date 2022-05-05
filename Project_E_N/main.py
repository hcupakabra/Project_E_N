from telegram import *
from telegram.ext import *
import sqlite3

conn = sqlite3.connect('table.db')
cur = conn.cursor()
cur.execute("SELECT * FROM society")
one_result = cur.fetchone()


class Question(Bot):
    def ask_a_question(update, context):
        if Bot.num_quest != 5:
            text = update.message.text
            context.user_data['text'] = update.message.text
            if context.user_data['text'] == Bot.answer[Bot.otvet]:
                update.message.reply_text(one_result[Bot.num_quest])
                Bot.scores += 1
                Bot.otvet += 1
                Bot.num_quest += 1
                return 2
            else:
                update.message.reply_text(one_result[Bot.num_quest])
                Bot.attempt += 1
                Bot.otvet += 1
                Bot.num_quest += 1
                return 2
        if Bot.num_quest == 5:
            Bot.scores += 1
            Ending.checking_the_ends(update, context)


class Bot():
    num_quest = 1
    otvet = 1
    scores = 0
    attempt = 0
    update = Update
    context = CallbackContext
    answer = {
        1: "4",
        2: "2",
        3: "4",
        4: "2",
        5: "2"
    }

    def get_year(update, context):
        year = 0
        text1 = update.message.text
        context.user_data['text1'] = update.message.text
        if context.user_data['text1'] == '2022':
            year = 1
            update.message.reply_text(one_result[0])
            return 2
        else:
            update.message.reply_text("Такого года пока нет, выбери другой")


class Ending(Bot):
    def checking_the_ends(update, context):
        if Bot.scores <= 3:
            print(Bot.attempt)
            update.message.reply_text(f"ошибок: {Bot.attempt}")
            update.message.reply_text("Нормально, оценка 3")
        if Bot.scores == 4:
            print(Bot.attempt)
            update.message.reply_text(f"ошибок: {Bot.attempt}")
            update.message.reply_text("Хорошо, оценка 4")
        if Bot.scores == 5:
            print(Bot.attempt)
            update.message.reply_text(f"ошибок: {Bot.attempt}")
            update.message.reply_text("Отлично! Оценка 5!")