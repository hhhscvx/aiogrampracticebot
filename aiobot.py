import os
from dotenv import load_dotenv
import logging
import asyncio

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode

from routers import router as main_router


dp = Dispatcher()
dp.include_router(main_router)


async def main():
    logging.basicConfig(level=logging.DEBUG)
    await dp.start_polling(bot)


if __name__ == "__main__":
    load_dotenv()
    TOKEN = os.getenv('AIOGRAM_TOKEN')
    bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
    asyncio.run(main())
