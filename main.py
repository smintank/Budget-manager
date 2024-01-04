import asyncio
import logging
import sys
from os import getenv

from aiogram import Dispatcher, Bot
from aiogram.enums import ParseMode
from dotenv import load_dotenv


logging.basicConfig(level=logging.INFO, stream=sys.stdout)
logger = logging.getLogger(__name__)

TOKEN = getenv('TG_BOT_TOKEN')

dp = Dispatcher()


async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
