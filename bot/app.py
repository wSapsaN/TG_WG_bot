import asyncio
from aiogram import Bot, Dispatcher

from admin import admin_route
from client import client_route
from middleware import DataBaseMD

from config import TOKEN

from database.engine import create_db, drop_db, session_maker

bot = Bot(token=TOKEN)
bot.admin_list = [667066036]

async def start_up_bot():
    print('\tConnection DataBase\t')
    
    await create_db()

async def main():
    
    dp = Dispatcher()

    dp.update.middleware(DataBaseMD(session_pool=session_maker))

    dp.include_router(admin_route)
    dp.include_router(client_route)
    
    dp.startup.register(start_up_bot)

    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())

if __name__ == "__main__":
    asyncio.run(main())