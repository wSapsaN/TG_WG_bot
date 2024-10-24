from aiogram.filters.command import Command, CommandStart
from aiogram import Router, F, types
from aiogram import Bot

from keyboards import keyboard_client
from inline_keyboards import inline

client_route = Router()

@client_route.message(CommandStart())
async def cmd_st(message: types.Message):
  await message.answer("Привет. Тебе нужен доступ до VPN?", reply_markup=keyboard_client)

@client_route.message(F.text == 'VPN')
async def vpn(message: types.Message, bot: Bot):
  await message.answer("Запрос на получение VPN отправлен. Ожидайте ответа")
  await bot.send_message(
    bot.admin_list[0],
    f"Пользователь {message.from_user.full_name} @{message.from_user.username} {message.from_user.id} запрашивает доступ для VPN",
    reply_markup=inline,
  )

@client_route.message(F.text == 'Инструкция')
async def vpn(message: types.Message):
  await message.answer("Что бы получить доступ до VPN, надо скачать такое-то приложение.")

@client_route.callback_query(F.data == 'posistiv')
async def result(callback_query: types.CallbackQuery):
  await callback_query.answer("Доступ разрешён")

  user_id = int(callback_query.message.text.split()[3])
  await callback_query.bot.send_message(user_id, 'Доступ разрешён')

@client_route.callback_query(F.data == 'negative')
async def result(callback_query: types.CallbackQuery):
  await callback_query.answer("Доступ запрещён")

  user_id = int(callback_query.message.text.split()[3])
  await callback_query.bot.send_message(user_id, 'Доступ запрещён')

@client_route.message(Command('help'))
async def helper(message: types.Message):
  await message.answer("Здесь должна быть помощь")