from aiogram import F, Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from ..states import Survey
from ..keyboard import choose_sphere_keyboard

router = Router()


@router.message(Survey.evm_wallet, F.text)
async def handle_degen_evm_wallet(message: Message, state: FSMContext):
    await message.answer(f"✨ Wallet succesfully connected!\n"
                         f"<code>{message.text}</code>")
    await message.answer(f"Please select which cryptocurrency area you are interested in:",
                         reply_markup=choose_sphere_keyboard())
    await state.update_data(evm_wallet=message.text)
    await state.set_state(Survey.crypto_sphere)


@router.message(Survey.evm_wallet)
async def handle_degen_evm_wallet_invalid(message: Message, state: FSMContext):
    await message.answer(f"Sorry, this type of message is unavailable. Please, enter your evm-wallet")
