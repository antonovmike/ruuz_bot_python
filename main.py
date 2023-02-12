import telebot
from menu import *
from constants import *

# TELEGRAM TOKEN
file = open('./test.env')
env = file.readlines()[0]
file.close()
index = len(env) - 1
bot = telebot.TeleBot(env[:index])


@bot.message_handler(content_types=['text'])
def start(message):
    mainmenu = MainMenu()
    bot.send_message(chat_id=message.chat.id, text=HEADING, reply_markup=mainmenu.main_menu())


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
# MAIN MENU
    back_1 = types.InlineKeyboardButton(text=MENU_HEADING, callback_data='mainmenu')
    if call.data == "mainmenu":
        mainmenu = MainMenu()
        bot.edit_message_text(HEADING, call.message.chat.id, call.message.message_id, reply_markup=mainmenu.main_menu())
# CONVERSATION
    elif call.data == "conversation":
        next_menu = types.InlineKeyboardMarkup()
        greetings = types.InlineKeyboardButton(text='Приветствие / Greeting', callback_data='greetings')
        how_are_you = types.InlineKeyboardButton(text='Как ваши дела? / How are you?', callback_data='how_are_you')
        by = types.InlineKeyboardButton(text='До свидания / Goodby', callback_data='by')
        next_menu.add(greetings)
        next_menu.add(how_are_you)
        next_menu.add(by)
        next_menu.add(back_1)
        bot.edit_message_text('Тема: Общение', call.message.chat.id, call.message.message_id, reply_markup=next_menu)
# FOOD
    elif call.data == "food":
        next_menu = types.InlineKeyboardMarkup()
        vegetables = types.InlineKeyboardButton(text='Овощи / Sabzavotlar', callback_data='vegetables')
        fruits = types.InlineKeyboardButton(text='Фрукты / Mevalar', callback_data='fruits')
        berries = types.InlineKeyboardButton(text='Ягоды / Rezavorlar', callback_data='berries')
        meat = types.InlineKeyboardButton(text='Мясо / Go’sh', callback_data='meat')
        beverages = types.InlineKeyboardButton(text='Напитки', callback_data='beverages')
        meal = types.InlineKeyboardButton(text='Приём пищи', callback_data='meal')
        baked_goods = types.InlineKeyboardButton(text='Выпечка / Novoy hona', callback_data='baked_goods')
        misc = types.InlineKeyboardButton(text='Разное', callback_data='misc')
        groats = types.InlineKeyboardButton(text='Крупа', callback_data='groats')
        milk = types.InlineKeyboardButton(text='Молочная продукция', callback_data='milk')
        spice = types.InlineKeyboardButton(text='Специи', callback_data='spice')
        next_menu.add(vegetables, fruits, berries)
        next_menu.add(meat, spice)
        next_menu.add(milk, baked_goods)
        next_menu.add(beverages, groats)
        next_menu.add(meal, misc)
        next_menu.add(back_1)
        bot.edit_message_text('Тема: Еда / Oqat', call.message.chat.id, call.message.message_id, reply_markup=next_menu)
# GRAMMAR
    elif call.data == "grammar":
        next_menu = types.InlineKeyboardMarkup()
        time_verbs = types.InlineKeyboardButton(text='Время глаголов / Verbs tenses', callback_data='time_verbs')
        cases = types.InlineKeyboardButton(text='Падежи / Cases', callback_data='cases')
        case_genitive = types.InlineKeyboardButton(text='Родительный падеж / Case genitive', callback_data='case_genitive')
        pronoun = types.InlineKeyboardButton(text='Местоимения / Pronoun / Olmoshlar', callback_data='pronoun')
        next_menu.add(time_verbs)
        next_menu.add(pronoun)
        next_menu.add(cases)
        next_menu.add(case_genitive)
        next_menu.add(back_1)
        bot.edit_message_text('Тема: Грамматика', call.message.chat.id, call.message.message_id, reply_markup=next_menu)
# CONVERSATION
    back_2 = BackToMainMenu().back_to_main_menu()
    if call.data == "greetings":
        bot.send_message(call.message.chat.id, GREETINGS_TXT)
        bot.send_message(chat_id=call.message.chat.id, text=MENU_HEADING, reply_markup=back_2)
    if call.data == "how_are_you":
        bot.send_message(call.message.chat.id, HOW_ARE_YOU_TXT)
        bot.send_message(chat_id=call.message.chat.id, text=MENU_HEADING, reply_markup=back_2)
    if call.data == "by":
        bot.send_message(call.message.chat.id, BY_TXT)
        bot.send_message(chat_id=call.message.chat.id, text=MENU_HEADING, reply_markup=back_2)
# HELP OR ABOUT
    if call.data == "help":
        bot.send_message(call.message.chat.id, HELP_TXT)
        bot.send_message(chat_id=call.message.chat.id, text=MENU_HEADING, reply_markup=back_2)
# GRAMMAR
    if call.data == "time_verbs":
        bot.send_photo(call.message.chat.id, UZ_VERB_FORMS_PNG)
        bot.send_message(chat_id=call.message.chat.id, text=MENU_HEADING, reply_markup=back_2)
    if call.data == "pronoun":
        bot.send_photo(call.message.chat.id, PRONOUN_PNG)
        bot.send_message(chat_id=call.message.chat.id, text=MENU_HEADING, reply_markup=back_2)
    if call.data == "cases":
        bot.send_photo(call.message.chat.id, CASES_PNG)
        bot.send_message(chat_id=call.message.chat.id, text=MENU_HEADING, reply_markup=back_2)
    if call.data == "case_genitive":
        bot.send_photo(call.message.chat.id, CASE_GENITIVE_PNG)
        bot.send_message(chat_id=call.message.chat.id, text=MENU_HEADING, reply_markup=back_2)
# FOOD
    if call.data == "vegetables":
        bot.send_message(call.message.chat.id, VEGETABLES_TXT)
        bot.send_message(chat_id=call.message.chat.id, text=MENU_HEADING, reply_markup=back_2)
    if call.data == "fruits":
        bot.send_message(call.message.chat.id, FRUITS_TXT)
        bot.send_message(chat_id=call.message.chat.id, text=MENU_HEADING, reply_markup=back_2)
    if call.data == "berries":
        bot.send_message(call.message.chat.id, BERRIES_TXT)
        bot.send_message(chat_id=call.message.chat.id, text=MENU_HEADING, reply_markup=back_2)
    if call.data == "meat":
        bot.send_message(call.message.chat.id, MEAT_TXT)
        bot.send_message(chat_id=call.message.chat.id, text=MENU_HEADING, reply_markup=back_2)
    if call.data == "baked_goods":
        bot.send_message(call.message.chat.id, BAKED_GOODS_TXT)
        bot.send_message(chat_id=call.message.chat.id, text=MENU_HEADING, reply_markup=back_2)
    if call.data == "misc":
        bot.send_message(call.message.chat.id, MISC_TXT)
        bot.send_message(chat_id=call.message.chat.id, text=MENU_HEADING, reply_markup=back_2)
    if call.data == "beverages":
        bot.send_message(call.message.chat.id, BEVERAGES_TXT)
        bot.send_message(chat_id=call.message.chat.id, text=MENU_HEADING, reply_markup=back_2)
    if call.data == "groats":
        bot.send_message(call.message.chat.id, GROATS_TXT)
        bot.send_message(chat_id=call.message.chat.id, text=MENU_HEADING, reply_markup=back_2)
    if call.data == "meal":
        bot.send_message(call.message.chat.id, MEAL_TXT)
        bot.send_message(chat_id=call.message.chat.id, text=MENU_HEADING, reply_markup=back_2)
    if call.data == "milk":
        bot.send_message(call.message.chat.id, MILK_TXT)
        bot.send_message(chat_id=call.message.chat.id, text=MENU_HEADING, reply_markup=back_2)
    if call.data == "spice":
        bot.send_message(call.message.chat.id, SPICE_TXT)
        bot.send_message(chat_id=call.message.chat.id, text=MENU_HEADING, reply_markup=back_2)


bot.polling(none_stop=True, interval=0)
