import telebot
from telebot import types

env = '5128374047:AAFiDR4Vr2nCHq1_xpF-P-0QOFzUlNDP0ew'
file = open('./test.env')
env_2 = file.readlines()[0]
# env_3 = '{}'.format(env_2)
file.close()
# print(env_4)
bot = telebot.TeleBot(env)


@bot.message_handler(content_types=['text'])
def start(message):
    if message.text:
        keyboard = types.InlineKeyboardMarkup()
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
    if call.data == "how_are_you":
        bot.send_message(call.message.chat.id, 'YAXSHIMI SIZ?')
    if call.data == "fine_and_you":
        bot.send_message(call.message.chat.id, 'MEN YAXSHIMAN. RAHMAT! SIZCHI?')
    if call.data == "by":
        bot.send_message(call.message.chat.id, 'KO’RISHKUNCHA XAYR')



bot.polling(none_stop=True, interval=1)
