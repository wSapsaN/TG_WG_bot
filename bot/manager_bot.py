import asyncio
from aiogram import Bot, Dispatcher

from admin import admin_route
from client import client_route
from middleware import SomeMidleware

from config import TOKEN

bot = Bot(token=TOKEN)
bot.admin_list = [667066036]

async def main():
    dp = Dispatcher()
    dp.include_router(admin_route)
    dp.include_router(client_route)

    admin_route.message.middleware(SomeMidleware())

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())