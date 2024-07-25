from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from aiogram import Router



router = Router(name=__name__)   


@router.message(CommandStart())
async def message_start_handler(message: Message):
    username = message.from_user.username
    await message.answer(f'welcome to genious bot, {username}❗')


@router.message(Command('help'))
async def message_help_handler(message: Message):
    text = '<b>25 серия берсерка</b> смотреть онлайн'

    chat_id = message.chat.id
    await message.bot.send_sticker(chat_id, 'CAACAgIAAxkBAAOCZqCVrds_MNo8ocNbFc6cc_uxNssAAlsPAAKjCxBJyDVnHqF8mHI1BA')
    await message.answer(text=text)