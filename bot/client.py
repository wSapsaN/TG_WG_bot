from aiogram.filters.command import Command, CommandStart
from aiogram import Router, F, types

client_route = Router()

@client_route.message(CommandStart())
async def cmd_st(message: types.Message):
  await message.answer("Hello client")
  await message.answer(text=str(message.from_user.id))