from aiogram.filters.command import Command, CommandStart
from aiogram import Router, F, types

from filter.chat_types import ChatTypesFilter, IsAdmin

admin_route = Router()
admin_route.message.filter(ChatTypesFilter(['private']), IsAdmin())

@admin_route.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer("Hello Admin")

@admin_route.message(Command("msg"))
async def test_msg(message: types.Message, msg: str):
    await message.answer(msg)
