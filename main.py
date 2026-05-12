import os
import logging
import asyncio
from routers import start,admin
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from database import create_table_users

load_dotenv()


async def main():
    create_table_users()
    bot = Bot(token=os.getenv("BOT_API_TOKEN"))
    dp = Dispatcher()

    dp.include_routers(start.router,admin.router)

    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
