from aiogram.filters.command import Command, CommandStart
from aiogram import Router, F, types

from filter.chat_types import ChatTypesFilter, IsAdmin

from sqlalchemy.ext.asyncio import AsyncSession

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

  # query = select(User.ip_client).where(User.id_telegram == user_id)
  # res = await session.execute(query)
  # s = res.scalar()

  await callback.bot.send_message(user_id, f'""')
  # await callback_query.bot.send_message(user_id, f'{type(s)} {s}')

@admin_route.callback_query(F.data == 'negative')
async def result(callback_query: types.CallbackQuery, q: str):
  await callback_query.answer(f"Доступ запрещён {q}")

  user_id = int(callback_query.message.text.split()[3])
  await callback_query.bot.send_message(user_id, 'Доступ запрещён')

