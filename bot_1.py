import telebot
bot = telebot.TeleBot('TOKEN')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Hello":
        bot.send_message(message.from_user.id, "Hello, how can I help_ru you?")
    elif message.text == "/help_ru":
        bot.send_message(message.from_user.id, "Type: Hello")
    else:
        bot.send_message(message.from_user.id, "Can't understand. Type /help_ru.")

bot.polling(none_stop=True, interval=1)

