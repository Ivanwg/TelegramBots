import telebot
import config
import re
from telebot import types

bot = telebot.TeleBot(config.token)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли
    bot.send_message(message.chat.id, message.text)

@bot.inline_handler(func=lambda query: len(query.query) > 0)
def query_text(query):
    print(query)

if __name__ == '__main__':
     bot.infinity_polling()