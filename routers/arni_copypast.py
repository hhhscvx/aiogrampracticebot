from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message
from routers.callback_handlers.info_kb import proxy_keyboard_markup

router = Router(name=__name__)


@router.message(Command("proxy"))
@router.message(F.text == "Proxy🪓")
async def message_proxy_handler(message: Message):
    chat_id = message.chat.id
    photo = 'https://i.pinimg.com/564x/a0/89/15/a08915d3191bba4f436e9bb742b55590.jpg'
    await message.bot.send_photo(chat_id=chat_id, photo=photo,
                                 caption="Choose your proxy country🌍",
                                 reply_markup=proxy_keyboard_markup())
