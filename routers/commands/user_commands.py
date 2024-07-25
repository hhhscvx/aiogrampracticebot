from aiogram.types import Message, ReplyKeyboardRemove
from aiogram import F, Router
from aiogram.filters import Command

router = Router(name=__name__)


@router.message(Command("dinahu"))
@router.message(F.text == "DINAHU")
async def message_dinahu_handler(message: Message):
    chat_id = message.chat.id
    sticker = 'CAACAgIAAxkBAAOBZqCU48R6Kq5GX_hqL6FQz0bBQCQAAklRAALasiFJF49ZlX6movs1BA'
    await message.bot.send_sticker(chat_id=chat_id, sticker=sticker,
                                   reply_markup=ReplyKeyboardRemove())
