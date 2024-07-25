from aiogram import Router
from aiogram.types import Message


router = Router(name=__name__)

@router.message()
async def message_echo_handler(message: Message):
    await message.reply(text=message.text)