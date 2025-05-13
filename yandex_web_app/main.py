from aiogram import Bot, Dispatcher
import logging
from handlers import router
import asyncio
from config import API

bot = Bot(token=API)
dp = Dispatcher(bot=bot)


async def main():
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())

