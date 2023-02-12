from telebot import types
from constants import *

class MainMenu:
    def main_menu(self):
        mainmenu = types.InlineKeyboardMarkup()
        conversation = types.InlineKeyboardButton(text=CONVERSATION_HDNG, callback_data='conversation')
        food = types.InlineKeyboardButton(text=FOOD_HEADING, callback_data='food')
        travel = types.InlineKeyboardButton(text=TRAVEL_HEADING, callback_data='travel')
        grammar = types.InlineKeyboardButton(text=GRAMMAR_HEADING, callback_data='grammar')
        help = types.InlineKeyboardButton(text=ABOUT_HEADING, callback_data='help')
        # Horizontal menu
        # mainmenu.add(conversation, food, grammar, help)
        # Vertical menu
        mainmenu.add(conversation)
        mainmenu.add(food)
        mainmenu.add(travel)
        mainmenu.add(grammar)
        mainmenu.add(help)
        return mainmenu


class BackToMainMenu:
    def back_to_main_menu(self):
        back_to_mainmenu = types.InlineKeyboardMarkup()
        go_back = types.InlineKeyboardButton(text='Жмяк!', callback_data='mainmenu')
        back_to_mainmenu.add(go_back)
        return back_to_mainmenu


# class SubMenu(list):
#     def sub_menu_creator(self, list_menu: []):
#         sub_menu = types.InlineKeyboardMarkup()
#         for i in list_menu:
#             sub_menu.add(i-1)
#         return sub_menu