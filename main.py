import telebot
from menu import *
from constants import *
from token_env import token


bot = telebot.TeleBot(token)


@bot.message_handler(commands=['help', 'start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add(CONVERSATION_HDNG, FOOD_HEADING)
    markup.add(GRAMMAR_HEADING, TRAVEL_HEADING)
    markup.add(ABOUT_HEADING)
    msg = bot.reply_to(message, 'Выберите тему', reply_markup=markup)
    bot.register_next_step_handler(msg, process_step)

def process_step(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    msg = bot.send_message(chat_id=message.chat.id, text='В главное меню: /start')
# ABOUT
    if message.text == ABOUT_HEADING:
        bot.send_message(chat_id=message.chat.id, text=HELP_TXT)
        bot.register_next_step_handler(msg, process_step)
# CONVERSATION
    if message.text == CONVERSATION_HDNG:
        markup.add('Приветствие / Greeting / Salomlashish')
        markup.add('Как ваши дела? / How are you? / Yaxshimi siz?')
        markup.add('До свидания / Goodby / Ko’rishkuncha')
        msg = bot.reply_to(message, '/start', reply_markup=markup)
        bot.register_next_step_handler(msg, process_step)
    if message.text == 'Приветствие / Greeting / Salomlashish':
        bot.send_message(chat_id=message.chat.id, text=GREETINGS_TXT)
        bot.register_next_step_handler(msg, process_step)
    if message.text == 'Как ваши дела? / How are you? / Yaxshimi siz?':
        bot.send_message(chat_id=message.chat.id, text=HOW_ARE_YOU_TXT)
        bot.register_next_step_handler(msg, process_step)
    if message.text == 'До свидания / Goodby / Ko’rishkuncha':
        bot.send_message(chat_id=message.chat.id, text=BY_TXT)
        bot.register_next_step_handler(msg, process_step)
# FOOD
    if message.text == FOOD_HEADING:
        markup.add('Овощи', 'Фрукты', 'Ягоды')
        markup.add('Мясо', 'Напитки', 'Выпечка')
        markup.add('Крупа', 'Молочная продукция')
        markup.add('Специи', 'Приём пищи', 'Разное')
        msg = bot.reply_to(message, '/start', reply_markup=markup)
        bot.register_next_step_handler(msg, process_step)
    if message.text == 'Овощи':
        bot.send_message(chat_id=message.chat.id, text=VEGETABLES_TXT)
        bot.register_next_step_handler(msg, process_step)
    if message.text == 'Фрукты':
        bot.send_message(chat_id=message.chat.id, text=FRUITS_TXT)
        bot.register_next_step_handler(msg, process_step)
    if message.text == 'Ягоды':
        bot.send_message(chat_id=message.chat.id, text=BERRIES_TXT)
        bot.register_next_step_handler(msg, process_step)
    if message.text == 'Мясо':
        bot.send_message(chat_id=message.chat.id, text=MEAT_TXT)
        bot.register_next_step_handler(msg, process_step)
    if message.text == 'Напитки':
        bot.send_message(chat_id=message.chat.id, text=BEVERAGES_TXT)
        bot.register_next_step_handler(msg, process_step)
    if message.text == 'Выпечка':
        bot.send_message(chat_id=message.chat.id, text=BAKED_GOODS_TXT)
        bot.register_next_step_handler(msg, process_step)
    if message.text == 'Крупа':
        bot.send_message(chat_id=message.chat.id, text=GROATS_TXT)
        bot.register_next_step_handler(msg, process_step)
    if message.text == 'Молочная продукция':
        bot.send_message(chat_id=message.chat.id, text=MILK_TXT)
        bot.register_next_step_handler(msg, process_step)
    if message.text == 'Специи':
        bot.send_message(chat_id=message.chat.id, text=SPICE_TXT)
        bot.register_next_step_handler(msg, process_step)
    if message.text == 'Приём пищи':
        bot.send_message(chat_id=message.chat.id, text=MEAL_TXT)
        bot.register_next_step_handler(msg, process_step)
    if message.text == 'MISC_TXT':
        bot.send_message(chat_id=message.chat.id, text=SPICE_TXT)
        bot.register_next_step_handler(msg, process_step)
# TRAVEL
    if message.text == TRAVEL_HEADING:
        markup.add('Такси / Taxi / Taksi')
        msg = bot.reply_to(message, '/start', reply_markup=markup)
        bot.register_next_step_handler(msg, process_step)
    if message.text == 'Такси / Taxi / Taksi':
        bot.send_message(chat_id=message.chat.id, text=TRAVEL_TXT)
        bot.register_next_step_handler(msg, process_step)
# GRAMMAR
    if message.text == GRAMMAR_HEADING:
        markup.add('Время глаголов / Verbs tenses')
        markup.add('Некоторые глаголы / Some verbs')
        markup.add('Падежи / Cases / Kelishiklar')
        markup.add('Родит. падеж / Case genitive / Qaratqich kelishikgi')
        markup.add('Местоимения / Pronoun / Olmoshlar')
        msg = bot.reply_to(message, '/start', reply_markup=markup)
        bot.register_next_step_handler(msg, process_step)
    if message.text == 'Время глаголов / Verbs tenses':
        bot.send_photo(message.chat.id, UZ_VERB_FORMS_PNG)
        bot.register_next_step_handler(msg, process_step)
    if message.text == 'Некоторые глаголы / Some verbs':
        bot.send_photo(message.chat.id, SOME_VERBS)
        bot.register_next_step_handler(msg, process_step)
    if message.text == 'Падежи / Cases / Kelishiklar':
        bot.send_photo(message.chat.id, CASES_PNG)
        # bot.register_next_step_handler(msg, process_step)
        bot.next_step_backend()
    if message.text == 'Родит. падеж / Case genitive / Qaratqich kelishikgi':
        bot.send_photo(message.chat.id, CASE_GENITIVE_PNG)
        bot.register_next_step_handler(msg, process_step)
    if message.text == 'Местоимения / Pronoun / Olmoshlar':
        bot.send_photo(message.chat.id, PRONOUN_PNG)
        bot.register_next_step_handler(msg, process_step)



bot.polling(none_stop=True, interval=0)
