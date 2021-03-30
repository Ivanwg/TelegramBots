import telebot
import time
import config
import os
import random
from telebot import types

bot = telebot.TeleBot(config.token)


# Мое сообщение, тест github
@bot.message_handler(commands=['test'])
def find_file_ids(message):
    for filename in os.listdir('music/'):
        if filename.split('.')[-1] == 'ogg':
            f = open('music/' + filename, 'rb')
            msg = bot.send_voice(message.chat.id, f)
            # А теперь отправим вслед за файлом его file_id
            bot.send_message(message.chat.id, filename + '\n' + msg.voice.file_id, reply_to_message_id=msg.message_id)
        time.sleep(3)


@bot.message_handler(commands=['file_id'])
def file_id(message):
    a = ['AwACAgIAAxkDAAMcYEX3mtwFtHZ1y3Acg0HXx6ny1LsAAqYKAAKbxjFKvkWo_mtaYxceBA',
         'AwACAgIAAxkDAAMeYEX3nbBKikGI470_tWWSnrBbdFMAAqcKAAKbxjFKufHutpjfzBAeBA',
         'AwACAgIAAxkDAAMgYEX3od1NN2DR9_Hrj01ktFGS_fcAAqgKAAKbxjFKa2CqARcKeXoeBA',
         'AwACAgIAAxkDAAMiYEX3pTivlyQiJWQyo9ndCPiLYy8AAqkKAAKbxjFKKSmuitfBvqMeBA']
    bot.send_voice(message.chat.id, random.choice(a))

@bot.message_handler(commands=["geophone"])
def geophone(message):
    # Эти параметры для клавиатуры необязательны, просто для удобства
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_phone = types.KeyboardButton(text="Отправить номер телефона", request_contact=True)
    button_geo = types.KeyboardButton(text="Отправить местоположение", request_location=True)
    my_button = types.KeyboardButton(text="Моя кнопка")
    keyboard.add(button_phone, my_button, button_geo)
    bot.send_message(message.chat.id, "Отправь мне свой номер телефона или поделись местоположением, жалкий человечишка!", reply_markup=keyboard)

@bot.message_handler(content_types=["location"])
def location(message):
    if message.location is not None:
        print(message.location)
        print("latitude: %s; longitude: %s" % (message.location.latitude, message.location.longitude))
        
@bot.message_handler(content_types=["contact"])
def contact(message):
    if message.contact is not None:
        print(message.contact)
        bot.send_message(message.chat.id, f'<b>Спасибо, {message.from_user.first_name} {message.from_user.last_name}</b>!', parse_mode='html')
    if message.contact.user_id != message.chat.id:
        bot.send_message(message.chat.id, "Это не твой номер, кретин!!")

# filter on a specific message
@bot.message_handler(func=lambda message: message.text == "Моя кнопка")
def command_text_hi(m):
    bot.send_message(m.chat.id, "I love you too!")



if __name__ == '__main__':
    bot.infinity_polling()
#bot.polling()
