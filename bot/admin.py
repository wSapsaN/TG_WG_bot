from aiogram.filters.command import Command, CommandStart
from aiogram import Router, F, types

from filter.chat_types import ChatTypesFilter, IsAdmin

from sqlalchemy.ext.asyncio import AsyncSession

from database.orm_admin import (
  outAllUsers, get_nameClinet, get_lastIPClinet
)
from database.orm_clinet import update_ip

# from genarate_wg import create_config
from create_accsess import create_accsess

from keyboards.inline_keyboards import instruction

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

  if last_ip <= 250:
    ip_clinet = f"10.10.10.{last_ip+1}"
    # file_name = await create_config(ip=ip_clinet, user_name=name_client)
    file_name = create_accsess(user_name=name_client, ip_addr=ip_clinet)

    file = types.FSInputFile(file_name)
    await callback.bot.send_document(user_id, file)
    await callback.bot.send_message(
      user_id, 
      "Выбирите подходящую инструкцию для подключения", 
      reply_markup=await instruction()
    )
    
    await update_ip(
      session=session, 
      id_telegram=user_id, 
      address=ip_clinet
    )

    return

  await callback.answer(f"Invalid ip address {ip_clinet}")
  await callback.message.bot(user_id, "На данный момент места на подключение ограничены, попробуйте запросить доступ позже. Извините за неудобства.")

@admin_route.callback_query(F.data == 'negative')
async def result(callback_query: types.CallbackQuery):
  await callback_query.answer(f"Доступ запрещён")

  user_id = int(callback_query.message.text.split()[3])
  await callback_query.bot.send_message(user_id, 'Доступ запрещён')

@admin_route.message(Command("count"))
async def count_use(message: types.Message, session: AsyncSession):
  res = await outAllUsers(session=session)
  await message.answer(str(res))