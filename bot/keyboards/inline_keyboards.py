from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def req_vpn()-> InlineKeyboardMarkup:
    success_access = InlineKeyboardButton(text="Yes", callback_data="posistiv")
    denide_access = InlineKeyboardButton(text="Nope", callback_data="negative")

    key_inline = [
        [success_access],
        [denide_access],
    ]

    return InlineKeyboardMarkup(inline_keyboard=key_inline)

async def instruction()-> InlineKeyboardMarkup:
    ios = InlineKeyboardButton(text="iOS🍎", callback_data="ios")
    android = InlineKeyboardButton(text="Android📱", callback_data="android")
    windows = InlineKeyboardButton(text="Windows💻", callback_data="windows")
    linux = InlineKeyboardButton(text="Linux🐧", callback_data="linux")

    key_inline = [
        [ios, android],
        [windows, linux],
    ]

    return InlineKeyboardMarkup(inline_keyboard=key_inline)
