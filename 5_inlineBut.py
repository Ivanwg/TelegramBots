from telebot import TeleBot, types
import config

bot = TeleBot(config.token)


@bot.message_handler(commands=['start'])
def start_handler(message: types.Message):
    bot.send_message(message.chat.id, "Hello!")


@bot.message_handler(content_types=["text"])
def text_handler(message):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти на Яндекс", url="https://ya.ru")
    callback_button = types.InlineKeyboardButton(text="Нажми меня", callback_data="test")
    callback_button2 = types.InlineKeyboardButton(text="Нажми меня 2", callback_data="test2")
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


# Inline-запросы
# Срабатывает только если написать @<ник бота> text
@bot.inline_handler(lambda inline_query: inline_query.query == 'text')    #свойство
def query_text(inline_query):
    try:
        r = types.InlineQueryResultArticle('1', 'Result', types.InputTextMessageContent('Result message.'))
        r2 = types.InlineQueryResultArticle('2', 'Result2', types.InputTextMessageContent('Result message2.'))
        bot.answer_inline_query(inline_query.id, [r, r2])
    except Exception as e:
        print(e)


# Срабатывает для всех остальных inline-запросов
@bot.inline_handler(lambda inline_query: True)
def query_text(inline_query):
    try:
        words = inline_query.query.split()
        query_results = []
        for i in range(len(words)):
            query_result = types.InlineQueryResultArticle(i, words[i], types.InputTextMessageContent(f'Вы нажали: "{words[i]}"'))
            query_results.append(query_result)
        bot.answer_inline_query(inline_query.id, query_results)
    except Exception as e:
        print(e)


@bot.chosen_inline_handler(func=lambda chosen_inline_result: True)
def test_chosen(chosen_inline_result):
    pass


if __name__ == '__main__':
    bot.infinity_polling()
