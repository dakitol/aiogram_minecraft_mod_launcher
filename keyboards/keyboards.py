from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

def create_game_icons_markup():
    game_icons = ["🎲Рандомный мод!"]
    game_icons_builder = ReplyKeyboardBuilder()
    game_icons_builder.row(*[KeyboardButton(text=icon) for icon in game_icons], width=3)
    
    return game_icons_builder.as_markup(resize_keyboard=True, one_time_keyboard=True)