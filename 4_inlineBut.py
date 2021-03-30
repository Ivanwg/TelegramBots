from telebot import TeleBot, types
import config

bot = TeleBot(config.token)


@bot.message_handler(commands=['start'])
def start_handler(message: types.Message):    #для подсказок
    bot.send_message(message.chat.id, "Hello!")


@bot.message_handler(content_types=["text"])   #регистр не влияет?
def text_handler(message):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти на Яндекс", url="https://ya.ru")
    callback_button = types.InlineKeyboardButton(text="Нажми меня", callback_data="test")
    callback_button2 = types.InlineKeyboardButton(text="Нажми меня 2", callback_data="test2")    #callback_data что это
    callback_button3 = types.InlineKeyboardButton(text="Нажми меня 3", callback_data="test")
    keyboard.add(url_button, callback_button, callback_button2, callback_button3)
    bot.send_message(message.chat.id, "Привет! Нажми на кнопку и перейди в поисковик.", reply_markup=keyboard)


# Если сообщение из чата с ботом
@bot.callback_query_handler(func=lambda callback: callback.message and callback.data == "test")
def callback_handler(callback):
    bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id, text="Пыщь " + callback.data)


@bot.callback_query_handler(func=lambda callback: callback.message and callback.data == "test2")
def callback_handler(callback):
    bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id, text="Пыщь 2")


# Если сообщение из инлайн-режима
@bot.callback_query_handler(func=lambda call: call.inline_message_id)
def callback_inline(call):
    if call.data == "test":
        bot.edit_message_text(inline_message_id=call.inline_message_id, text="Бдыщь")


if __name__ == '__main__':
    bot.infinity_polling()
