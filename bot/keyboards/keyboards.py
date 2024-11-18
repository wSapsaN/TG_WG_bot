from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboard_list = [
    [KeyboardButton(text='VPN')],
    [KeyboardButton(text='Инструкция')],
]


keyboard_client = ReplyKeyboardMarkup(keyboard=keyboard_list, resize_keyboard=True, one_time_keyboard=True)