from aiogram.types import (Message, ReplyKeyboardMarkup,
                           KeyboardButton, ReplyKeyboardRemove)
from aiogram.filters import Command, CommandStart
from aiogram import F, Router


router = Router(name=__name__)


def start_msg_keyboard():
    btn1 = KeyboardButton(text="H3lp?")
    btn2 = KeyboardButton(text="DINAHU")
    btn3 = KeyboardButton(text="GOEV")
    btn4 = KeyboardButton(text="DEGEN🤑")
    btn_proxy = KeyboardButton(text="Proxy🪓")
    buttons_first_row = [btn1, btn2, btn3]
    buttons_second_row = [btn4]
    buttons_third_row = [btn_proxy]
    markup = ReplyKeyboardMarkup(keyboard=[buttons_first_row,
                                           buttons_second_row,
                                           buttons_third_row],
                                 resize_keyboard=True, one_time_keyboard=True)
    return markup


@router.message(CommandStart())
async def message_start_handler(message: Message):
    username = message.from_user.username
    await message.answer(text=f'welcome to genious bot, {username}❗',
                         reply_markup=start_msg_keyboard())


@router.message(Command('help'))
@router.message(F.text == 'H3lp?')
async def message_help_handler(message: Message):
    text = '<b>25 серия берсерка</b> <a href="https://google.com/">смотреть онлайн</a>'
    sticker = 'CAACAgIAAxkBAAOCZqCVrds_MNo8ocNbFc6cc_uxNssAAlsPAAKjCxBJyDVnHqF8mHI1BA'

    chat_id = message.chat.id
    await message.bot.send_sticker(chat_id=chat_id, sticker=sticker,
                                   reply_markup=ReplyKeyboardRemove())
    await message.answer(text=text)
    with open("proxy.txt") as file:
        file.__del__()
