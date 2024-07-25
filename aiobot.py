import os
from dotenv import load_dotenv
import logging
import asyncio

from aiogram import Bot, Dispatcher, F, Router
from aiogram.types import Message, LabeledPrice
from aiogram.utils.chat_action import ChatActionSender
from aiogram.enums import ParseMode

from routers import router as main_router


dp = Dispatcher()
dp.include_router(main_router)


@dp.message(F.photo)
async def message_images_handler(message: Message):  # photo=url
    # await message.bot.send_chat_action(chat_id=message.chat.id, action=ChatAction.UPLOAD_PHOTO)
    async with ChatActionSender.upload_photo(
        chat_id=message.chat.id,
        bot=message.bot
    ):
        await asyncio.sleep(delay=3)
        await message.reply_photo(photo=message.photo[-1].file_id)


@dp.message(F.text == 'qwe')
async def message_f_test_handler(message: Message):
    text = 'daiki'
    await message.answer(text=text)


@dp.message(F.text == 'buy')
async def message_payment_handler(message: Message):
    labeled_price = LabeledPrice(label='Покупка нашего курса', amount=500)
    await bot.send_invoice(
        chat_id=message.chat.id,
        title="Покупка товара",
        description="Заплатить (Клик)",
        payload="payload",
        provider_token=SBER_TOKEN,
        currency='USD',
        prices=[labeled_price]
    )



async def main():
    logging.basicConfig(level=logging.DEBUG)
    await dp.start_polling(bot)


if __name__ == "__main__":
    load_dotenv()
    TOKEN = os.getenv('AIOGRAM_TOKEN')
    SBER_TOKEN = os.getenv('SBER_TOKEN')
    bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
    asyncio.run(main())
