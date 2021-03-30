import telebot
import time
import config
import os
import random
from telebot import types
#почему файл не отображался в запускаемых???

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')

@bot.message_handler(content_types=['text'])
def send_sticker(message):
    if message.text.lower() in ['привет', 'hello']:
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAOQYFPCFrWJ5C4Wlxh54EDVFYLL5QQAAlQAA0G1Vgxqt_jHCI0B-h4E')
    elif message.text.lower() == 'пока':
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAORYFPCQxF93zUTf2n9h_mGbPNQpiUAAlIAA0G1VgwCEOJkaX8Pch4E')

@bot.message_handler(content_types=['sticker'])
def stick(message):
    print(message.sticker.file_id)
    bot.send_message(message.chat.id, 'Крутой стикер, а посмотри, какой стикер нравится мне:)')
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAP_YGAv68g3rR4mjLiZnZzLmY1GZuAAAlEAAw220hkqwngctN7UWh4E')
bot.polling()