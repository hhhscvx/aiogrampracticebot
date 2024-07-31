from aiogram import F, Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from ..states import Survey

router = Router()


@router.message(Survey.name, F.text)
async def handle_degen_name(message: Message, state: FSMContext):
    await message.answer(f"Hello <b>{message.text}</b>\n\n"
                         f"Now please, share your EVM-wallet for future airdrop!")
    await state.update_data(name=message.text)
    await state.set_state(Survey.evm_wallet)


@router.message(Survey.name)
async def handle_degen_name_invalid(message: Message, state: FSMContext):
    await message.answer(f"Sorry, this type of message is unavailable. Please, enter your name")
