import telebot
from menu import *
from constants import *
from token_env import token


bot = telebot.TeleBot(token)


@bot.message_handler(commands=['help_ru', 'start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    # names = [CONVERSATION_HDNG, FOOD_HEADING, GRAMMAR_HEADING, TRAVEL_HEADING, ABOUT_HEADING]
    # for i in names: markup.add(i)
    markup.add(RU_UZ, EN_UZ)
    msg = bot.reply_to(message, 'Выберите тему', reply_markup=markup)
    bot.register_next_step_handler(msg, process_step)

def process_step(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    # msg = bot.send_message(chat_id=message.chat.id, text='Презапустить бот: /start', reply_markup=markup)
# MAIN
    if message.text == RU_UZ or message.text == MENU_HEADING_RU:
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add(CONVERSATION_HDNG_RU, FOOD_HEADING_RU)
        markup.add(GRAMMAR_HEADING_RU, TRAVEL_HEADING_RU)
        markup.add(ABOUT_HEADING_RU)
        msg = bot.send_message(chat_id=message.chat.id, text='Презапустить бот: /start', reply_markup=markup)
        bot.register_next_step_handler(msg, process_step)
        # bot.register_next_step_handler_by_chat_id(chat_id=, callback=)
    if message.text == EN_UZ or message.text == MENU_HEADING_EN:
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add(CONVERSATION_HDNG_EN, FOOD_HEADING_EN)
        markup.add(GRAMMAR_HEADING_EN, TRAVEL_HEADING_EN)
        markup.add(ABOUT_HEADING_EN)
        msg = bot.send_message(chat_id=message.chat.id, text='Restart bot: /start', reply_markup=markup)
        bot.register_next_step_handler(msg, process_step)

# ABOUT
    if message.text == ABOUT_HEADING_RU:
        bot.send_message(chat_id=message.chat.id, text=HELP_TXT_RU)
        msg = bot.send_message(chat_id=message.chat.id, text='Презапустить бот: /start', reply_markup=markup)
        bot.register_next_step_handler(msg, process_step)
    if message.text == ABOUT_HEADING_EN:
        bot.send_message(chat_id=message.chat.id, text=HELP_TXT_EN)
        msg = bot.send_message(chat_id=message.chat.id, text='Restart bot: /start', reply_markup=markup)
        bot.register_next_step_handler(msg, process_step)
# CONVERSATION
    if message.text == CONVERSATION_HDNG_RU:
        markup.add('Приветствие / Salomlashish')
        markup.add('Как ваши дела? / Yaxshimi siz?')
        markup.add('До свидания / Ko’rishkuncha')
        markup.add(MENU_HEADING_RU)
        msg = bot.send_message(chat_id=message.chat.id, text='Презапустить бот: /start', reply_markup=markup)
        bot.register_next_step_handler(msg, process_step)
    if message.text == 'Приветствие / Salomlashish':
        bot.send_message(chat_id=message.chat.id, text=GREETINGS_TXT)
        msg = bot.send_message(chat_id=message.chat.id, text='Презапустить бот: /start', reply_markup=markup)
        bot.register_next_step_handler(msg, process_step)
    if message.text == 'Как ваши дела? / Yaxshimi siz?':
        bot.send_message(chat_id=message.chat.id, text=HOW_ARE_YOU_TXT)
        msg = bot.send_message(chat_id=message.chat.id, text='Презапустить бот: /start', reply_markup=markup)
        bot.register_next_step_handler(msg, process_step)
    if message.text == 'До свидания / Ko’rishkuncha':
        bot.send_message(chat_id=message.chat.id, text=BY_TXT)
        msg = bot.send_message(chat_id=message.chat.id, text='Презапустить бот: /start', reply_markup=markup)
        bot.register_next_step_handler(msg, process_step)
# FOOD
    if message.text == FOOD_HEADING_RU:
        markup.add('Овощи', 'Фрукты', 'Ягоды')
        markup.add('Мясо', 'Напитки', 'Выпечка')
        markup.add('Крупа', 'Молочная продукция')
        markup.add('Специи', 'Приём пищи', 'Разное')
        markup.add(MENU_HEADING_RU)
        msg = bot.send_message(chat_id=message.chat.id, text='Презапустить бот: /start', reply_markup=markup)
        bot.register_next_step_handler(msg, process_step)
    if message.text == 'Овощи':
        bot.send_message(chat_id=message.chat.id, text=VEGETABLES_TXT)
        msg = bot.send_message(chat_id=message.chat.id, text='Презапустить бот: /start', reply_markup=markup)
        bot.register_next_step_handler(msg, process_step)
    if message.text == 'Фрукты':
        bot.send_message(chat_id=message.chat.id, text=FRUITS_TXT)
        msg = bot.send_message(chat_id=message.chat.id, text='Презапустить бот: /start', reply_markup=markup)
        bot.register_next_step_handler(msg, process_step)
    if message.text == 'Ягоды':
        bot.send_message(chat_id=message.chat.id, text=BERRIES_TXT)
        msg = bot.send_message(chat_id=message.chat.id, text='Презапустить бот: /start', reply_markup=markup)
        bot.register_next_step_handler(msg, process_step)
    if message.text == 'Мясо':
        bot.send_message(chat_id=message.chat.id, text=MEAT_TXT)
        msg = bot.send_message(chat_id=message.chat.id, text='Презапустить бот: /start', reply_markup=markup)
        bot.register_next_step_handler(msg, process_step)
    if message.text == 'Напитки':
        bot.send_message(chat_id=message.chat.id, text=BEVERAGES_TXT)
        msg = bot.send_message(chat_id=message.chat.id, text='Презапустить бот: /start', reply_markup=markup)
        bot.register_next_step_handler(msg, process_step)
    if message.text == 'Выпечка':
        bot.send_message(chat_id=message.chat.id, text=BAKED_GOODS_TXT)
        msg = bot.send_message(chat_id=message.chat.id, text='Презапустить бот: /start', reply_markup=markup)
        bot.register_next_step_handler(msg, process_step)
    if message.text == 'Крупа':
        bot.send_message(chat_id=message.chat.id, text=GROATS_TXT)
        msg = bot.send_message(chat_id=message.chat.id, text='Презапустить бот: /start', reply_markup=markup)
        bot.register_next_step_handler(msg, process_step)
    if message.text == 'Молочная продукция':
        bot.send_message(chat_id=message.chat.id, text=MILK_TXT)
        msg = bot.send_message(chat_id=message.chat.id, text='Презапустить бот: /start', reply_markup=markup)
        bot.register_next_step_handler(msg, process_step)
    if message.text == 'Специи':
        bot.send_message(chat_id=message.chat.id, text=SPICE_TXT)
        msg = bot.send_message(chat_id=message.chat.id, text='Презапустить бот: /start', reply_markup=markup)
        bot.register_next_step_handler(msg, process_step)
    if message.text == 'Приём пищи':
        bot.send_message(chat_id=message.chat.id, text=MEAL_TXT)
        msg = bot.send_message(chat_id=message.chat.id, text='Презапустить бот: /start', reply_markup=markup)
        bot.register_next_step_handler(msg, process_step)
    if message.text == 'MISC_TXT':
        bot.send_message(chat_id=message.chat.id, text=SPICE_TXT)
        msg = bot.send_message(chat_id=message.chat.id, text='Презапустить бот: /start', reply_markup=markup)
        bot.register_next_step_handler(msg, process_step)
# TRAVEL
    if message.text == TRAVEL_HEADING_RU:
        markup.add('Такси / Taksi')
        markup.add(MENU_HEADING_RU)
        msg = bot.send_message(chat_id=message.chat.id, text='Презапустить бот: /start', reply_markup=markup)
        bot.register_next_step_handler(msg, process_step)
    if message.text == 'Такси / Taksi':
        bot.send_message(chat_id=message.chat.id, text=TRAVEL_TXT)
        msg = bot.send_message(chat_id=message.chat.id, text='Презапустить бот: /start', reply_markup=markup)
        bot.register_next_step_handler(msg, process_step)
# GRAMMAR
    if message.text == GRAMMAR_HEADING_RU:
        markup.add('Время глаголов')
        markup.add('Некоторые глаголы')
        markup.add('Падежи / Kelishiklar')
        markup.add('Родит. падеж / Qaratqich kelishikgi')
        markup.add('Местоимения / Olmoshlar')
        markup.add(MENU_HEADING_RU)
        msg = bot.send_message(chat_id=message.chat.id, text='Презапустить бот: /start', reply_markup=markup)
        bot.register_next_step_handler(msg, process_step)
    if message.text == 'Время глаголов':
        bot.send_photo(message.chat.id, UZ_VERB_FORMS_PNG)
        msg = bot.send_message(chat_id=message.chat.id, text='Презапустить бот: /start', reply_markup=markup)
        bot.register_next_step_handler(msg, process_step)
    if message.text == 'Некоторые глаголы':
        bot.send_photo(message.chat.id, SOME_VERBS)
        msg = bot.send_message(chat_id=message.chat.id, text='Презапустить бот: /start', reply_markup=markup)
        bot.register_next_step_handler(msg, process_step)
    if message.text == 'Падежи / Kelishiklar':
        bot.send_photo(message.chat.id, CASES_PNG)
        bot.next_step_backend()
    if message.text == 'Родит. падеж / Qaratqich kelishikgi':
        bot.send_photo(message.chat.id, CASE_GENITIVE_PNG)
        msg = bot.send_message(chat_id=message.chat.id, text='Презапустить бот: /start', reply_markup=markup)
        bot.register_next_step_handler(msg, process_step)
    if message.text == 'Местоимения / Olmoshlar':
        bot.send_photo(message.chat.id, PRONOUN_PNG)
        msg = bot.send_message(chat_id=message.chat.id, text='Презапустить бот: /start', reply_markup=markup)
        bot.register_next_step_handler(msg, process_step)


bot.polling(none_stop=True, interval=0)
