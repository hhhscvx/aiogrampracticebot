from aiogram.types import (Message, ReplyKeyboardRemove,
                           ReplyKeyboardMarkup, KeyboardButton)
from aiogram import F, Router
from aiogram.filters import Command

router = Router(name=__name__)

def proxy_keyboard_markup() -> ReplyKeyboardMarkup:
    btn1 = KeyboardButton(text="Belgium 🇧🇪")
    btn2 = KeyboardButton(text="Czechia 🇨🇿")
    btn3 = KeyboardButton(text="Germany 🇩🇪")
    btn4 = KeyboardButton(text="Italy 🇮🇹")

    keyboard = [[btn1], [btn2], [btn3], [btn4]]
    markup = ReplyKeyboardMarkup(keyboard=keyboard)

    return markup


@router.message(Command("proxy"))
@router.message(F.text == "Proxy🪓")
async def message_dinahu_handler(message: Message):
    chat_id = message.chat.id
    photo = 'https://i.pinimg.com/564x/a0/89/15/a08915d3191bba4f436e9bb742b55590.jpg'
    await message.bot.send_photo(chat_id=chat_id, photo=photo,
                                 caption="Choose your proxy country🌍",
                                 reply_markup=proxy_keyboard_markup())
    
REMOVE_KEYBOARD_MARKUP = ["Belgium 🇧🇪", "Czechia 🇨🇿", "Germany 🇩🇪", "Italy 🇮🇹"]

@router.message(lambda _: F.text in REMOVE_KEYBOARD_MARKUP)
async def message_dinahu_handler(message: Message):
    await message.reply(text="Your choise: " + message.text, reply_markup=ReplyKeyboardRemove())
