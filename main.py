import telebot
from menu import *
from constants import *
from token_env import token


bot = telebot.TeleBot(token)


@bot.message_handler(content_types=['text'])
def start(message):
    mainmenu = MainMenu()
    bot.send_message(chat_id=message.chat.id, text=HEADING, reply_markup=mainmenu.main_menu())


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    sub_menu = types.InlineKeyboardMarkup()
    back_1 = types.InlineKeyboardButton(text=MENU_HEADING, callback_data='mainmenu')

# MAIN MENU
    if call.data == "mainmenu":
        mainmenu = MainMenu()
        bot.edit_message_text(HEADING, call.message.chat.id, call.message.message_id, reply_markup=mainmenu.main_menu())
# CONVERSATION
    elif call.data == "conversation":
        greetings = types.InlineKeyboardButton(text='Приветствие / Greeting / Salomlashish', callback_data='greetings')
        how_are_you = types.InlineKeyboardButton(text='Как ваши дела? / How are you? / Yaxshimi siz?', callback_data='how_are_you')
        by = types.InlineKeyboardButton(text='До свидания / Goodby / Ko’rishkuncha', callback_data='by')
        list_of_buttons = [greetings, how_are_you, by]
        for i in list_of_buttons: sub_menu.add(i)
        sub_menu.add(back_1)
        bot.edit_message_text(CONVERSATION_HDNG, call.message.chat.id, call.message.message_id, reply_markup=sub_menu)
# FOOD
    elif call.data == "food":
        vegetables = types.InlineKeyboardButton(text='Овощи / Vegetables / Sabzavotlar', callback_data='vegetables')
        fruits = types.InlineKeyboardButton(text='Фрукты / Fruits / Mevalar', callback_data='fruits')
        berries = types.InlineKeyboardButton(text='Ягоды / Berries / Rezavorlar', callback_data='berries')
        meat = types.InlineKeyboardButton(text='Мясо / Meat / Go’sh', callback_data='meat')
        beverages = types.InlineKeyboardButton(text='Напитки / Beverages', callback_data='beverages')
        meal = types.InlineKeyboardButton(text='Приём пищи / Meal', callback_data='meal')
        baked_goods = types.InlineKeyboardButton(text='Выпечка / Bake / Novoy hona', callback_data='baked_goods')
        misc = types.InlineKeyboardButton(text='Разное / Miscellaneous', callback_data='misc')
        groats = types.InlineKeyboardButton(text='Крупа / Groats', callback_data='groats')
        milk = types.InlineKeyboardButton(text='Молочная продукция / Milk products', callback_data='milk')
        spice = types.InlineKeyboardButton(text='Специи / Spice / Ziravorlar', callback_data='spice')
        sub_menu.add(vegetables)
        sub_menu.add(fruits, berries)
        sub_menu.add(meat, spice)
        sub_menu.add(milk)
        sub_menu.add(baked_goods)
        sub_menu.add(beverages, groats)
        sub_menu.add(meal, misc)
        sub_menu.add(back_1)
        bot.edit_message_text(FOOD_HEADING, call.message.chat.id, call.message.message_id, reply_markup=sub_menu)
# TRAVEL
    elif call.data == "travel":
        sub_menu.add(back_1)
        bot.edit_message_text(TRAVEL_HEADING, call.message.chat.id, call.message.message_id, reply_markup=sub_menu)
# GRAMMAR
    elif call.data == "grammar":
        sub_menu = types.InlineKeyboardMarkup()
        time_verbs = types.InlineKeyboardButton(text='Время глаголов / Verbs tenses', callback_data='time_verbs')
        some_verbs = types.InlineKeyboardButton(text='Некоторые глаголы / Some verbs', callback_data='some_verbs')
        cases = types.InlineKeyboardButton(text='Падежи / Cases / Kelishiklar', callback_data='cases')
        case_genitive = types.InlineKeyboardButton(text='Родительный падеж / Case genitive / Qaratqich kelishikgi', callback_data='case_genitive')
        pronoun = types.InlineKeyboardButton(text='Местоимения / Pronoun / Olmoshlar', callback_data='pronoun')
        list_of_buttons = [time_verbs, some_verbs, cases, case_genitive, pronoun]
        for i in list_of_buttons: sub_menu.add(i)
        sub_menu.add(back_1)
        bot.edit_message_text(GRAMMAR_HEADING, call.message.chat.id, call.message.message_id, reply_markup=sub_menu)

    back_2 = BackToMainMenu().back_to_main_menu()

# CONVERSATION
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
    if call.data == "some_verbs":
        bot.send_photo(call.message.chat.id, SOME_VERBS)
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
