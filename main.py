import telebot
from telebot import types
from pathlib import Path

# TELEGRAM TOKEN
file = open('./test.env')
env = file.readlines()[0]
file.close()
index = len(env) - 1
bot = telebot.TeleBot(env[:index])


class MainMenu:
    # def __init__(self):
    #     self. =
    def main_menu(self):
        mainmenu = types.InlineKeyboardMarkup()
        conversation = types.InlineKeyboardButton(text='Общение', callback_data='conversation')
        food = types.InlineKeyboardButton(text='Еда / Ovqat', callback_data='food')
        grammar = types.InlineKeyboardButton(text='Грамматика', callback_data='grammar')
        help = types.InlineKeyboardButton(text='Об этом боте', callback_data='help')
        # Horizontal menu
        # mainmenu.add(conversation, food, grammar, help)
        # Vertical menu
        mainmenu.add(conversation)
        mainmenu.add(food)
        mainmenu.add(grammar)
        mainmenu.add(help)
        return mainmenu


class BackToMainMenu:
    def back_to_main_menu(self):
        back_to_mainmenu = types.InlineKeyboardMarkup()
        go_back = types.InlineKeyboardButton(text='Жмяк!', callback_data='mainmenu')
        back_to_mainmenu.add(go_back)
        return back_to_mainmenu


menu_heading = 'Вернуться в главное меню'
heading = 'Русско-Узбекский разговорник'

@bot.message_handler(content_types=['text'])
def start(message):
    mainmenu = MainMenu()
    bot.send_message(chat_id=message.chat.id, text=heading, reply_markup=mainmenu.main_menu())


class SubMenu(list):
    def sub_menu_creator(self, list_menu: []):
        sub_menu = types.InlineKeyboardMarkup()
        for i in list_menu:
            sub_menu.add(i-1)
        return sub_menu


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
# MAIN MENU
    if call.data == "mainmenu":
        mainmenu = MainMenu()
        bot.edit_message_text(heading, call.message.chat.id, call.message.message_id, reply_markup=mainmenu.main_menu())
# CONVERSATION
    elif call.data == "conversation":
        next_menu = types.InlineKeyboardMarkup()
        greetings = types.InlineKeyboardButton(text='Приветствие / Greeting', callback_data='greetings')
        how_are_you = types.InlineKeyboardButton(text='Как ваши дела? / How are you?', callback_data='how_are_you')
        by = types.InlineKeyboardButton(text='До свидания / Goodby', callback_data='by')
        back = types.InlineKeyboardButton(text=menu_heading, callback_data='mainmenu')
        next_menu.add(greetings)
        next_menu.add(how_are_you)
        next_menu.add(by)
        next_menu.add(back)
        bot.edit_message_text('Тема: Общение', call.message.chat.id, call.message.message_id, reply_markup=next_menu) #, parse_mode='MarkdownV2'
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
        back = types.InlineKeyboardButton(text='В главное меню', callback_data='mainmenu')
        next_menu.add(vegetables, fruits, berries)
        next_menu.add(meat, spice)
        next_menu.add(milk, baked_goods)
        next_menu.add(beverages, groats)
        next_menu.add(meal, misc)
        next_menu.add(back)
        bot.edit_message_text('Тема: Еда / Oqat', call.message.chat.id, call.message.message_id, reply_markup=next_menu)
# GRAMMAR
    elif call.data == "grammar":
        next_menu = types.InlineKeyboardMarkup()
        time_verbs = types.InlineKeyboardButton(text='Время глаголов / Verbs tenses', callback_data='time_verbs')
        cases = types.InlineKeyboardButton(text='Падежи / Cases', callback_data='cases')
        case_genitive = types.InlineKeyboardButton(text='Родительный падеж / Case genitive', callback_data='case_genitive')
        pronoun = types.InlineKeyboardButton(text='Местоимения / Pronoun / Olmoshlar', callback_data='pronoun')
        back = types.InlineKeyboardButton(text=menu_heading, callback_data='mainmenu')
        next_menu.add(time_verbs)
        next_menu.add(pronoun)
        next_menu.add(cases)
        next_menu.add(case_genitive)
        next_menu.add(back)
        bot.edit_message_text('Тема: Грамматика', call.message.chat.id, call.message.message_id, reply_markup=next_menu)
# CONVERSATION
    if call.data == "greetings":
        txt = Path('dictionaries/greetings').read_text()
        bot.send_message(call.message.chat.id, txt)
        back = BackToMainMenu().back_to_main_menu()
        bot.send_message(chat_id=call.message.chat.id, text=menu_heading, reply_markup=back)
    if call.data == "how_are_you":
        txt = Path('dictionaries/how_are_you').read_text()
        bot.send_message(call.message.chat.id, txt)
        back = BackToMainMenu().back_to_main_menu()
        bot.send_message(chat_id=call.message.chat.id, text=menu_heading, reply_markup=back)
    if call.data == "by":
        txt = Path('dictionaries/by').read_text()
        bot.send_message(call.message.chat.id, txt)
        back = BackToMainMenu().back_to_main_menu()
        bot.send_message(chat_id=call.message.chat.id, text=menu_heading, reply_markup=back)
# HELP
    if call.data == "help":
        txt = Path('dictionaries/help').read_text()
        bot.send_message(call.message.chat.id, txt)
        back = BackToMainMenu().back_to_main_menu()
        bot.send_message(chat_id=call.message.chat.id, text=menu_heading, reply_markup=back)
# GRAMMAR
    if call.data == "time_verbs":
        bot.send_photo(call.message.chat.id, 'https://github.com/antonovmike/ruuz_bot_python/blob/test/pictures/uz_verb_forms.png?raw=true')
        back = BackToMainMenu().back_to_main_menu()
        bot.send_message(chat_id=call.message.chat.id, text=menu_heading, reply_markup=back)
    if call.data == "pronoun":
        bot.send_photo(call.message.chat.id, 'https://github.com/antonovmike/ruuz_bot_python/blob/test/pictures/pronoun.png?raw=true')
        back = BackToMainMenu().back_to_main_menu()
        bot.send_message(chat_id=call.message.chat.id, text=menu_heading, reply_markup=back)
    if call.data == "cases":
        bot.send_photo(call.message.chat.id, 'https://github.com/antonovmike/ruuz_bot_python/blob/test/pictures/cases.png?raw=true')
        back = BackToMainMenu().back_to_main_menu()
        bot.send_message(chat_id=call.message.chat.id, text=menu_heading, reply_markup=back)
    if call.data == "case_genitive":
        bot.send_photo(call.message.chat.id, 'https://github.com/antonovmike/ruuz_bot_python/blob/test/pictures/case_genitive.png?raw=true')
        back = BackToMainMenu().back_to_main_menu()
        bot.send_message(chat_id=call.message.chat.id, text=menu_heading, reply_markup=back)
# FOOD
    if call.data == "vegetables":
        txt = Path('dictionaries/food_vegetables').read_text()
        bot.send_message(call.message.chat.id, txt)
        back = BackToMainMenu().back_to_main_menu()
        bot.send_message(chat_id=call.message.chat.id, text=menu_heading, reply_markup=back)
    if call.data == "fruits":
        txt = Path('dictionaries/food_fruits').read_text()
        bot.send_message(call.message.chat.id, txt)
        back = BackToMainMenu().back_to_main_menu()
        bot.send_message(chat_id=call.message.chat.id, text=menu_heading, reply_markup=back)
    if call.data == "berries":
        txt = Path('dictionaries/food_berries').read_text()
        bot.send_message(call.message.chat.id, txt)
        back = BackToMainMenu().back_to_main_menu()
        bot.send_message(chat_id=call.message.chat.id, text=menu_heading, reply_markup=back)
    if call.data == "meat":
        txt = Path('dictionaries/food_meat').read_text()
        bot.send_message(call.message.chat.id, txt)
        back = BackToMainMenu().back_to_main_menu()
        bot.send_message(chat_id=call.message.chat.id, text=menu_heading, reply_markup=back)
    if call.data == "baked_goods":
        txt = Path('dictionaries/food_baked_goods').read_text()
        bot.send_message(call.message.chat.id, txt)
        back = BackToMainMenu().back_to_main_menu()
        bot.send_message(chat_id=call.message.chat.id, text=menu_heading, reply_markup=back, parse_mode='MarkdownV2')
    if call.data == "misc":
        txt = Path('dictionaries/food_misc').read_text()
        bot.send_message(call.message.chat.id, txt)
        back = BackToMainMenu().back_to_main_menu()
        bot.send_message(chat_id=call.message.chat.id, text=menu_heading, reply_markup=back)
    if call.data == "beverages":
        txt = Path('dictionaries/food_beverages').read_text()
        bot.send_message(call.message.chat.id, txt)
        back = BackToMainMenu().back_to_main_menu()
        bot.send_message(chat_id=call.message.chat.id, text=menu_heading, reply_markup=back)
    if call.data == "groats":
        txt = Path('dictionaries/food_groats').read_text()
        bot.send_message(call.message.chat.id, txt)
        back = BackToMainMenu().back_to_main_menu()
        bot.send_message(chat_id=call.message.chat.id, text=menu_heading, reply_markup=back)
    if call.data == "meal":
        txt = Path('dictionaries/food_meal').read_text()
        bot.send_message(call.message.chat.id, txt)
        back = BackToMainMenu().back_to_main_menu()
        bot.send_message(chat_id=call.message.chat.id, text=menu_heading, reply_markup=back)
    if call.data == "milk":
        txt = Path('dictionaries/food_milk').read_text()
        bot.send_message(call.message.chat.id, txt)
        back = BackToMainMenu().back_to_main_menu()
        bot.send_message(chat_id=call.message.chat.id, text=menu_heading, reply_markup=back)
    if call.data == "spice":
        txt = Path('dictionaries/food_spice').read_text()
        bot.send_message(call.message.chat.id, txt)
        back = BackToMainMenu().back_to_main_menu()
        bot.send_message(chat_id=call.message.chat.id, text=menu_heading, reply_markup=back)


bot.polling(none_stop=True, interval=0)
