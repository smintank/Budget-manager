from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.utils.markdown import hbold

from bot.bot import dp


@dp.massage(CommandStart())
async def command_start_handler(message: Message):
    await message.answer(text=f'Привет 👋, '
                              f'{hbold(message.from_user.full_name)}!'
                              f' Я помогу тебе вести бюджет.')
