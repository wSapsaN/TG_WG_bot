from aiogram.filters.command import Command, CommandStart
from aiogram import Router, F, types
from aiogram import Bot

from keyboards.keyboards import keyboard_client
from keyboards.inline_keyboards import req_vpn, instruction
from database.orm_clinet import add_client, status_useVPN, up_request

from sqlalchemy.ext.asyncio import AsyncSession

# from genarate_wg import create_config

client_route = Router()

@client_route.message(CommandStart())
async def cmd_st(message: types.Message):
  await message.answer("Привет. Тебе нужен доступ до VPN?", reply_markup=keyboard_client)

@client_route.message(F.text == 'VPN')
async def vpn(message: types.Message, bot: Bot, session: AsyncSession):
  await add_client(
    session=session, 
    id_telegram=message.from_user.id, 
    nik_name=message.from_user.username,
  )

  if await status_useVPN(session=session, id_telegram=message.from_user.id):
    await message.answer("Вы уже отправили запрос, ожидайте ответа.")

    return

  await up_request(session=session, id_telegram=message.from_user.id)

  await message.answer("Запрос на получение VPN отправлен. Ожидайте ответа")
  await bot.send_message(
    bot.admin_list[0],
    f"Пользователь {message.from_user.full_name} @{message.from_user.username} {message.from_user.id} запрашивает доступ для VPN",
    reply_markup=await req_vpn(),
  )

# TODO: 
# @client_route.message(F.text == 'Инструкция')
# async def vpn(message: types.Message):
#   await message.answer("Что бы получить доступ до VPN, надо скачать такое-то приложение.")

@client_route.message(Command('help'))
async def helper(message: types.Message):
  await message.answer("Здесь должна быть помощь", reply_markup=await instruction())

@client_route.callback_query(F.data == 'windows')
async def windows_instruction(callback: types.CallbackQuery):
  await callback.answer('WINDOWS')
  await callback.message.edit_text("Windows инструкция")

@client_route.callback_query(F.data == 'android')
async def android_instruction(callback: types.CallbackQuery):
  await callback.answer('ANDROID')
  await callback.message.edit_text("Android инструкция")


@client_route.callback_query(F.data == 'ios')
async def ios_instruction(callback: types.CallbackQuery):
  await callback.answer('IOS')
  await callback.message.edit_text(
    """1. Скачайте приложение [WireGuard](https://apps.apple.com/ru/app/wireguard/id1441195209).
2. *Нажмите на файл для просмотра*, который я отправил вам выше с расширением conf, нажмите на иконку для просмотра в правом нижнем углу, далее отправки из приложения в правом вехем углу телефона.
3. Найдите приложение *WireGuard* и откройте его.
4. В приложение *WireGuard* появиться строка с названием файла и кнопка для подключения к VPN'у.

Приятного использования."""
  )

@client_route.callback_query(F.data == 'linux')
async def linux_instruction(callback: types.CallbackQuery):
  await callback.answer('LINUX')
  await callback.message.edit_text("Linux инструкция")
