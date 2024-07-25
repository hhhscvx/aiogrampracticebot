from aiogram.types import Message
from aiogram import Router
from aiogram.filters import Command

router = Router(name=__name__)


@router.message(Command('dinahu'))
async def message_dinahu_handler(message: Message):
    chat_id = message.chat.id
    await message.bot.send_sticker(chat_id, 'CAACAgIAAxkBAAOBZqCU48R6Kq5GX_hqL6FQz0bBQCQAAklRAALasiFJF49ZlX6movs1BA')