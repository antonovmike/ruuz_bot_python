import telebot
from telebot import types

file = open('./test.env')
env = file.readlines()[0]
file.close()
index = len(env) - 1
bot = telebot.TeleBot(env[:index])


@bot.message_handler(content_types=['text'])
def start(message):
    if message.text:
        keyboard = types.InlineKeyboardMarkup()
        key_greetings = types.InlineKeyboardButton(text='Приветствие', callback_data='greetings')
        keyboard.add(key_greetings)
        key_how_are_you = types.InlineKeyboardButton(text='Как ваши дела?', callback_data='how_are_you')
        keyboard.add(key_how_are_you)
        key_fine_and_you= types.InlineKeyboardButton(text='Я в порядке. Спасибо. А вы?', callback_data='fine_and_you')
        keyboard.add(key_fine_and_you)
        key_by= types.InlineKeyboardButton(text='До свидания', callback_data='by')
        keyboard.add(key_by)
        question = 'Что вы хотите перевести?'
        bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "greetings":
        bot.send_message(call.message.chat.id, 'ASSALOM ALEYKUM - вежливое приветствие\n\nVAALEYKUM ASSALOM - вежливый ответ на приветствие\n\nSALOM - неформальное приветствие, используется только в отношении хороших знакомых')
    if call.data == "how_are_you":
        bot.send_message(call.message.chat.id, 'YAXSHIMI SIZ? - как Ваши дела?\n\nTAZUVMI SIZ? - как Ваши дела?\n\nISHLARINGIZ QALAY? - как твои дела?')
    if call.data == "fine_and_you":
        bot.send_message(call.message.chat.id, 'HA YAXSHI, RAHMAT. SIZDA CHI? - Хорошо, спасибо. А у Вас?\n\nMEN YAXSHIMAN. RAHMAT! SIZCHI? - Хорошо, спасибо, а Ваши?')
    if call.data == "by":
        bot.send_message(call.message.chat.id, 'KO’RISHKUNCHA / KO’RISHKUNCHA XAYR - до свидания\n\nXAYR - пока\n\nUCHRASHUVGACHA/UCHRASHAMIZ - увидимся\n\nSAGIBOLING - пока / будьте здоровы')


bot.polling(none_stop=True, interval=1)
