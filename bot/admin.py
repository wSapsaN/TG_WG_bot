from aiogram.filters.command import Command, CommandStart
from aiogram import Router, F, types

from filter.chat_types import ChatTypesFilter, IsAdmin

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from database.models import User
from database.orm_admin import (
  outAllUsers, get_nameClinet, get_lastIPClinet
)

from genarate_wg import create_config

admin_route = Router()
admin_route.message.filter(ChatTypesFilter(['private']), IsAdmin())

@admin_route.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer("Hello Admin")

@admin_route.message(Command("msg"))
async def test_msg(message: types.Message, session: AsyncSession):
    await message.answer()

@admin_route.callback_query(F.data == 'posistiv')
async def result(callback: types.CallbackQuery, session: AsyncSession):
  await callback.answer("Доступ разрешён")

  user_id = int(callback.message.text.split()[3])
  last_ip = await get_lastIPClinet(session=session, id_telegram=user_id)
  name_client = await get_nameClinet(session=session, id_telegram=user_id)

  # await callback.bot.send_message(user_id, str(res))

  if last_ip <= 250:
    create_config(ip=last_ip+1, user_name=name_client)

  # TODO:
  # file = types.FSInputFile("PATH")
  # await callback.bot.send_document(user_id, file)
  # await callback.bot.send_message(user_id, "Инструкция по подключению.......") # надо добавить кнопки
  # инструкции типа Windows, Linux, Android, ios, MacOS

@admin_route.callback_query(F.data == 'negative')
async def result(callback_query: types.CallbackQuery):
  await callback_query.answer(f"Доступ запрещён")

  user_id = int(callback_query.message.text.split()[3])
  await callback_query.bot.send_message(user_id, 'Доступ запрещён')

@admin_route.message(Command("count"))
async def count_use(message: types.Message, session: AsyncSession):
  res = await outAllUsers(session=session)
  await message.answer(str(res))