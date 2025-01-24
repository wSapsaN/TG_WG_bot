import sys
import logging
import ssl

from aiohttp import web
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums.parse_mode import ParseMode
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from aiogram.types import FSInputFile

from admin import admin_route
from client import client_route
from middleware import DataBaseMD

from config import TOKEN, WEBHOOK_SSL_CERT, WEBHOOK_SSL_PRIV, ADMIN_LIST

from database.engine import create_db, drop_db, session_maker

bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN))
bot.admin_list = ADMIN_LIST

WEB_SERVER_HOST='127.0.0.1'
WEB_SERVER_PORT=5000

dp = Dispatcher()

async def start_up_bot(bot: Bot):
    print('\tConnection DataBase\t')

    dp.update.middleware(DataBaseMD(session_pool=session_maker))

    dp.include_router(admin_route)
    dp.include_router(client_route)
    
    await bot.set_webhook(
        f"https://86.102.60.62:88/",
        certificate=FSInputFile(WEBHOOK_SSL_CERT),
    )
    
    await create_db()

async def shutdown_bot(bot: Bot):
    await bot.delete_webhook()


def main():
    # TODO:
    # Logger: https://habr.com/ru/companies/otus/articles/773540/

    dp.shutdown.register(shutdown_bot)
    
    dp.startup.register(start_up_bot)
    
    app = web.Application()

    webhook_requests_handler = SimpleRequestHandler(
        dispatcher=dp,
        bot=bot,
    )

    # Register webhook handler on application
    webhook_requests_handler.register(app, path="")

    # Mount dispatcher startup and shutdown hooks to aiohttp application
    setup_application(app, dp, bot=bot)

    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    context.load_cert_chain(WEBHOOK_SSL_CERT, WEBHOOK_SSL_PRIV)    
    
    # web.run_app(app, host="127.0.0.1", port=5000)
    web.run_app(app, host=WEB_SERVER_HOST, port=WEB_SERVER_PORT, ssl_context=context)

    # await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    main()
