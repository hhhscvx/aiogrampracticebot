from aiogram import F, Router
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext

from ..states import Survey
from ..keyboard import CryptoSphere

router = Router()


@router.message(Survey.crypto_sphere, lambda message: message.text in CryptoSphere.SPHERES)
async def handle_degen_sphere(message: Message, state: FSMContext):
    await message.answer(f"<i>Sphere <b>{message.text}</b> successfully selected!</i>\n",
                         reply_markup=ReplyKeyboardRemove())
    if message.text == "Both":
        data = await state.update_data(crypto_sphere="Retro ⨯ NFT")
    else:
        data = await state.update_data(crypto_sphere=message.text)
    await state.clear()
    from ..handlers import send_survey_results
    await send_survey_results(message, data)


@router.message(Survey.crypto_sphere)
async def handle_degen_sphere_invalid(message: Message, state: FSMContext):
    await message.answer(f"This variable is invalid. Please select one in your keyboard below")
