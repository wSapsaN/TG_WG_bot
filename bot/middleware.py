from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from typing import Any, Callable, Dict, Awaitable

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