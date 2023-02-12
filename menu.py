from telebot import types

class MainMenu:
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