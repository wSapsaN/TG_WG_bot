import os
import logging
import asyncio
from typing import Dict
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command, CommandStart

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from typing import Any, Callable, Dict, Awaitable

from aiogram import Router, F

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')

if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

TOKEN = os.environ.get('TOKEN')

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)

route = Router()

class SomeMidleware(BaseMiddleware):
    def __init__(self) -> None:
        self.msg = "message"

    async def __call__(self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any],
            ) -> Any:

        data["msg"] = self.msg
        return await handler(event, data)

@route.message(CommandStart())
async def cmd_start(message: types.message):
    await message.answer("Hello man")

@route.message(Command("msg"))
async def test_msg(message: types.Message, msg: str):
    await message.answer(msg)

async def main():
    dp = Dispatcher()
    # dp.update.outer_middleware(SomeMidleware())
    dp.include_router(route)

    route.message.middleware(SomeMidleware())

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())