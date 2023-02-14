from telebot import types
from constants import *

class MainMenu:
    def main_menu(self, names):
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        for i in names: markup.add(i)
        return markup


# class SubMenu(list):
#     def sub_menu_creator(self, list_menu: []):
#         sub_menu = types.InlineKeyboardMarkup()
#         for i in list_menu:
#             sub_menu.add(i-1)
#         return sub_menu