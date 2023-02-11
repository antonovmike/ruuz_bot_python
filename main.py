import telebot
from telebot import types
from pathlib import Path

file = open('./test.env')
env = file.readlines()[0]
file.close()
index = len(env) - 1
bot = telebot.TeleBot(env[:index])


@bot.message_handler(content_types=['text'])
def start(message):
    if message.text:
        keyboard = types.InlineKeyboardMarkup()
        key_greetings = types.InlineKeyboardButton(text='Приветствие / Greeting', callback_data='greetings')
        keyboard.add(key_greetings)
        key_how_are_you = types.InlineKeyboardButton(text='Как ваши дела? / How are you?', callback_data='how_are_you')
        keyboard.add(key_how_are_you)
        key_by= types.InlineKeyboardButton(text='До свидания / Goodby', callback_data='by')
        keyboard.add(key_by)
        key_help= types.InlineKeyboardButton(text='Про этот бот / About this bot', callback_data='help')
        keyboard.add(key_help)
        question = 'Что вы хотите перевести?'
        bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)


f = open("example_1.txt","r")
lines = f.readlines()
index = len(lines[1])-1
item = lines[2]
number = item[:2]


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "greetings":
        txt = Path('dictionaries/greetings').read_text()
        bot.send_message(call.message.chat.id, txt)
    if call.data == "how_are_you":
        txt = Path('dictionaries/how_are_you').read_text()
        bot.send_message(call.message.chat.id, txt)
    if call.data == "by":
        txt = Path('dictionaries/by').read_text()
        bot.send_message(call.message.chat.id, txt)
    if call.data == "help":
        txt = Path('dictionaries/help').read_text()
        bot.send_message(call.message.chat.id, txt)


bot.polling(none_stop=True, interval=1)
