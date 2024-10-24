from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

success_access = InlineKeyboardButton(text="Yes", callback_data="posistiv")
denide_access = InlineKeyboardButton(text="Nope", callback_data="negative")

key_inline = [
    [success_access],
    [denide_access],
]

inline = InlineKeyboardMarkup(inline_keyboard=key_inline)