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
    mainmenu = types.InlineKeyboardMarkup()
    conversation = types.InlineKeyboardButton(text='Общение', callback_data='conversation')
    food = types.InlineKeyboardButton(text='Еда / Ovqat', callback_data='food')
    grammar = types.InlineKeyboardButton(text='Грамматика', callback_data='grammar')
    help = types.InlineKeyboardButton(text='Об этом боте', callback_data='help')
    # mainmenu.add(conversation, food, grammar, help)
    mainmenu.add(conversation)
    mainmenu.add(food)
    mainmenu.add(grammar)
    mainmenu.add(help)
    heading = 'Русско-Узбекский разговорник'
    bot.send_message(chat_id=message.chat.id, text=heading, reply_markup=mainmenu)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
# MAIN MENU
    if call.data == "mainmenu":
        mainmenu = types.InlineKeyboardMarkup()
        conversation = types.InlineKeyboardButton(text='Общение', callback_data='conversation')
        food = types.InlineKeyboardButton(text='Еда / Ovqat', callback_data='food')
        grammar = types.InlineKeyboardButton(text='Грамматика', callback_data='grammar')
        help = types.InlineKeyboardButton(text='Об этом боте', callback_data='help')
        mainmenu.add(conversation)
        mainmenu.add(food)
        mainmenu.add(grammar)
        mainmenu.add(help)
        bot.send_message(chat_id=call.message.chat.id, text='Главное меню', reply_markup=mainmenu)
# CONVERSATION
    elif call.data == "conversation":
        next_menu = types.InlineKeyboardMarkup()
        greetings = types.InlineKeyboardButton(text='Приветствие / Greeting', callback_data='greetings')
        how_are_you = types.InlineKeyboardButton(text='Как ваши дела? / How are you?', callback_data='how_are_you')
        by = types.InlineKeyboardButton(text='До свидания / Goodby', callback_data='by')
        back = types.InlineKeyboardButton(text='В главное меню', callback_data='mainmenu')
        next_menu.add(greetings, how_are_you, by)
        next_menu.add(back)
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
        back = types.InlineKeyboardButton(text='В главное меню', callback_data='mainmenu')
        next_menu.add(vegetables, fruits, berries)
        next_menu.add(meat, spice, milk)
        next_menu.add(baked_goods, beverages, groats)
        next_menu.add(meal, misc)
        next_menu.add(back)
        bot.edit_message_text('Тема: Еда / Oqat', call.message.chat.id, call.message.message_id, reply_markup=next_menu)
# GRAMMAR
    elif call.data == "grammar":
        next_menu = types.InlineKeyboardMarkup()
        time_verbs = types.InlineKeyboardButton(text='Время глаголов / Verbs tenses', callback_data='time_verbs')
        cases = types.InlineKeyboardButton(text='Падежи / Cases', callback_data='cases')
        case_genitive = types.InlineKeyboardButton(text='Родительный падеж / Case genitive', callback_data='case_genitive')
        back = types.InlineKeyboardButton(text='В главное меню', callback_data='mainmenu')
        next_menu.add(time_verbs, cases, case_genitive)
        next_menu.add(back)
        bot.edit_message_text('Тема: Грамматика', call.message.chat.id, call.message.message_id, reply_markup=next_menu)
# CONVERSATION
    if call.data == "greetings":
        txt = Path('dictionaries/greetings').read_text()
        bot.send_message(call.message.chat.id, txt)
    if call.data == "how_are_you":
        txt = Path('dictionaries/how_are_you').read_text()
        bot.send_message(call.message.chat.id, txt)
    if call.data == "by":
        txt = Path('dictionaries/by').read_text()
        bot.send_message(call.message.chat.id, txt)
# HELP
    if call.data == "help":
        txt = Path('dictionaries/help').read_text()
        bot.send_message(call.message.chat.id, txt)
# GRAMMAR
    if call.data == "time_verbs":
        bot.send_photo(call.message.chat.id, 'https://github.com/antonovmike/ruuz_bot_python/blob/test/pictures/uz_verb_forms.png?raw=true')
        bot.send_message(call.message.chat.id, "Restart bot: /start")
    if call.data == "cases":
        bot.send_photo(call.message.chat.id, 'https://github.com/antonovmike/ruuz_bot_python/blob/test/pictures/cases.png?raw=true')
        bot.send_message(call.message.chat.id, "Restart bot: /start")
    if call.data == "case_genitive":
        bot.send_photo(call.message.chat.id, 'https://github.com/antonovmike/ruuz_bot_python/blob/test/pictures/case_genitive.png?raw=true')
        bot.send_message(call.message.chat.id, "Restart bot: /start")
# FOOD
    if call.data == "vegetables":
        txt = Path('dictionaries/food_vegetables').read_text()
        bot.send_message(call.message.chat.id, txt)
    if call.data == "fruits":
        txt = Path('dictionaries/food_fruits').read_text()
        bot.send_message(call.message.chat.id, txt)
    if call.data == "berries":
        txt = Path('dictionaries/food_berries').read_text()
        bot.send_message(call.message.chat.id, txt)
    if call.data == "meat":
        txt = Path('dictionaries/food_meat').read_text()
        bot.send_message(call.message.chat.id, txt)
    if call.data == "baked_goods":
        txt = Path('dictionaries/food_baked_goods').read_text()
        bot.send_message(call.message.chat.id, txt)
    if call.data == "misc":
        txt = Path('dictionaries/food_misc').read_text()
        bot.send_message(call.message.chat.id, txt)
    if call.data == "beverages":
        txt = Path('dictionaries/food_beverages').read_text()
        bot.send_message(call.message.chat.id, txt)
    if call.data == "groats":
        txt = Path('dictionaries/food_groats').read_text()
        bot.send_message(call.message.chat.id, txt)
    if call.data == "meal":
        txt = Path('dictionaries/food_meal').read_text()
        bot.send_message(call.message.chat.id, txt)
    if call.data == "milk":
        txt = Path('dictionaries/food_milk').read_text()
        bot.send_message(call.message.chat.id, txt)
    if call.data == "spice":
        txt = Path('dictionaries/food_spice').read_text()
        bot.send_message(call.message.chat.id, txt)


bot.polling(none_stop=True, interval=0)
