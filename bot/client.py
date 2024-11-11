from aiogram.filters.command import Command, CommandStart
from aiogram import Router, F, types
from aiogram import Bot

from keyboards import keyboard_client
from inline_keyboards import inline
from database.orm_clinet import add_client

from sqlalchemy.ext.asyncio import AsyncSession

# from genarate_wg import create_config

client_route = Router()

@client_route.message(CommandStart())
async def cmd_st(message: types.Message):
  await message.answer("Привет. Тебе нужен доступ до VPN?", reply_markup=keyboard_client)

@client_route.message(F.text == 'VPN')
async def vpn(message: types.Message, bot: Bot, session: AsyncSession):
  await message.answer("Запрос на получение VPN отправлен. Ожидайте ответа")
  await bot.send_message(
    bot.admin_list[0],
    f"Пользователь {message.from_user.full_name} @{message.from_user.username} {message.from_user.id} запрашивает доступ для VPN",
    reply_markup=inline,
  )

  await add_client(
    session=session, 
    id_telegram=message.from_user.id, 
    nik_name=message.from_user.username,
  )

# TODO: 
# @client_route.message(F.text == 'Инструкция')
# async def vpn(message: types.Message):
#   await message.answer("Что бы получить доступ до VPN, надо скачать такое-то приложение.")

@client_route.message(Command('help'))
async def helper(message: types.Message):
  await message.answer("Здесь должна быть помощь")