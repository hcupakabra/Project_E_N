import logging

import dp as dp
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, ReplyKeyboardMarkup
from telegram.ext import *
import sqlite3
from telebot import *
from telegram.ext import updater

conn = sqlite3.connect('table.db')
cur = conn.cursor()
cur.execute("SELECT * FROM society")
one_result = cur.fetchone()
num = 1
otvet = 1
i = 1
scores = 0
attempt = 0


class Question():
    num_quest = num
    otvet = otvet
    scores = scores
    attempt = attempt
    update = Update
    context = CallbackContext

    def ask_a_question(update, context):
        if Question.num_quest != 5:
            text = update.message.text
            context.user_data['text'] = update.message.text
            if context.user_data['text'] == Bot.answers[Question.otvet]:
                update.message.reply_text("Правильно, следующее задание")
                update.message.reply_text(one_result[Question.num_quest])
                if Question.attempt == 0:
                    Question.scores += 1
                    Question.otvet += 1
                    Question.num_quest += 1
                    return 2
                elif Question.attempt != 0:
                    Question.otvet += 1
                    Question.num_quest += 1
                    Question.scores = Question.scores
                    return 2
            else:
                update.message.reply_text("Не правильно, попробуй ещё раз")
                Question.attempt += 1
                print(Question.attempt)
        if Question.num_quest == 5:
            Ending.checking_the_ends(update, context)


class Bot():
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


class Ending():
    def checking_the_ends(update, context):
        if Question.scores <= 2:
            update.message.reply_text("Нормально, оценка 3")
        if Question.scores == 3:
            update.message.reply_text("Хорошо, оценка 4")
        if Question.scores == 4:
            update.message.reply_text("Отлично! Оценка 5!")