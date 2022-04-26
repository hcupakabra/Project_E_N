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
n = 1
o = 1
i = 1


class Question():
    n = n
    o = o
    i = i
    update = Update
    context = CallbackContext

    def answer(update, context):
        answers = {
            1: "4",
            2: "2"
        }
        text = update.message.text
        context.user_data['text'] = update.message.text
        print(context.user_data)
        if context.user_data['text'] == answers[Question.o]:
            update.message.reply_text("Правильно, следующее задание")
            update.message.reply_text(one_result[Question.n])
            Question.o += 1
            Question.n += 1
            Question.i += 1
            return Question.i
        else:
            update.message.reply_text("Не правильно, попробуй ещё раз")

    def year(update, context):
        year = 0
        text1 = update.message.text
        context.user_data['text1'] = update.message.text
        print(context.user_data)
        if context.user_data['text1'] == '2022':
            year = 1
            update.message.reply_text(one_result[0])
            return 2
