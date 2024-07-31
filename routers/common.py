from aiogram import Router, F
from aiogram.types import Message, LabeledPrice
from aiogram.utils.chat_action import ChatActionSender
from aiogram.types import Message

import asyncio
import os


router = Router(name=__name__)
SBER_TOKEN = os.getenv('SBER_TOKEN')
print(f"SBER_TOKEN: {SBER_TOKEN}")


@router.message(F.photo)
async def message_images_handler(message: Message):  # photo=url
    # await message.bot.send_chat_action(chat_id=message.chat.id, action=ChatAction.UPLOAD_PHOTO)
    async with ChatActionSender.upload_photo(
        chat_id=message.chat.id,
        bot=message.bot
    ):
        await asyncio.sleep(delay=1)
        await message.reply_photo(photo=message.photo[-1].file_id)


@router.message(F.text == 'qwe')
async def message_f_test_handler(message: Message):
    text = 'daiki'
    await message.answer(text=text)


@router.message(F.text == 'buy')
async def message_payment_handler(message: Message):
    labeled_price = LabeledPrice(label='Покупка нашего курса', amount=500)
    await message.bot.send_invoice(
        chat_id=message.chat.id,
        title="Покупка товара",
        description="Заплатить (Клик)",
        payload="payload",
        provider_token=SBER_TOKEN,
        currency='USD',
        prices=[labeled_price]
    )


@router.message()
async def message_echo_handler(message: Message):
    await message.reply(text=message.text)
