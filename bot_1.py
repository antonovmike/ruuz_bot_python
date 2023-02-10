import telebot
bot = telebot.TeleBot('5128374047:AAFiDR4Vr2nCHq1_xpF-P-0QOFzUlNDP0ew')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Hello":
        bot.send_message(message.from_user.id, "Hello, how can I help you?")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Type: Hello")
    else:
        bot.send_message(message.from_user.id, "Can't understand. Type /help.")

bot.polling(none_stop=True, interval=1)

