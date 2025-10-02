from aiogram.types import (
    ReplyKeyboardMarkup, 
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

share_phone_kb = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="Поделиться номером", request_contact=True)]],
    resize_keyboard=True,
    one_time_keyboard=True
)

my_data_kb = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text="Мои данные", callback_data="my_data")]]
)

back_kb = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text="Назад", callback_data="back_to_menu")]]
)
