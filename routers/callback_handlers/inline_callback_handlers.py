import io
from aiogram import F, Router
from aiogram.types import (CallbackQuery, BufferedInputFile,
                           ReplyKeyboardRemove)
from aiogram.enums import ChatAction

import uuid

from .info_kb import ProxyCountries, ProxyPayment
from routers.callback_handlers.info_kb import payment_markup


router = Router()


@router.callback_query(F.data == ProxyCountries.BELGIUM)
async def handle_proxy_belgium(callback_query: CallbackQuery):
    await callback_query.answer()
    await callback_query.message.edit_caption(caption="Choose your proxy country🌍")
    await callback_query.message.answer(text=f"🌍 <i>Your choice</i>: {ProxyCountries.BELGIUM[-2:]}\n\n"
                                        f"💰 <b>Total price:</b> 0.5$", reply_markup=payment_markup())


@router.callback_query(F.data == ProxyCountries.CZECHIA)
async def handle_proxy_czechia(callback_query: CallbackQuery):
    await callback_query.answer()
    await callback_query.message.edit_caption(caption="Choose your proxy country🌍")
    await callback_query.message.answer(text=f"🌍 <i>Your choice</i>: {ProxyCountries.CZECHIA[-2:]}\n\n"
                                        f"💰 <b>Total price:</b> 0.5$", reply_markup=payment_markup())


@router.callback_query(F.data == ProxyCountries.GERMANY)
async def handle_proxy_germany(callback_query: CallbackQuery):
    await callback_query.answer()
    await callback_query.message.edit_caption(caption="Choose your proxy country🌍")
    await callback_query.message.answer(text=f"🌍 <i>Your choice</i>: {ProxyCountries.GERMANY[-2:]}\n\n"
                                        f"💰 <b>Total price:</b> 0.5$", reply_markup=payment_markup())


@router.callback_query(F.data == ProxyCountries.ITALY)
async def handle_proxy_italy(callback_query: CallbackQuery):
    await callback_query.answer()
    await callback_query.message.edit_caption(caption="Choose your proxy country🌍")
    await callback_query.message.answer(text=f"🌍 <i>Your choice</i>: {ProxyCountries.ITALY[-2:]}\n\n"
                                        f"💰 <b>Total price:</b> 0.5$", reply_markup=payment_markup())


@router.callback_query(F.data == ProxyPayment.payment_callback)
async def handle_proxy_italy(callback_query: CallbackQuery):
    await callback_query.answer("Оплачено.")
    old_text = callback_query.message.text
    await callback_query.message.edit_text(text=f"{old_text}\n\n<b>Успешная оплата!</b>")
    await callback_query.bot.send_chat_action(chat_id=callback_query.message.chat.id,
                                              action=ChatAction.UPLOAD_DOCUMENT)
    file = io.StringIO()
    file.write("Мы тебя наебали, будешь мультить без прокси🤡")
    await callback_query.message.answer_document(document=BufferedInputFile(
        file=file.getvalue().encode("utf-8"),
        filename=f"proxies_{str(uuid.uuid4().fields[-1])[:10]}"
    ), caption="✨ <b>Your proxies are ready!</b>")


@router.callback_query(F.data == ProxyPayment.main_menu_callback)
async def handle_proxy_italy(callback_query: CallbackQuery):
    await callback_query.answer()
    await callback_query.message.delete()
