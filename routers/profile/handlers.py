from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state

from .states import Survey

from .survey.name import router as name_router
from .survey.evm_wallet import router as wallet_router
from .survey.crypto_sphere import router as sphere_router


router = Router(name=__name__)

router.include_router(name_router)
router.include_router(wallet_router)
router.include_router(sphere_router)


@router.message(Command("degen"), default_state)
@router.message(F.text == "DEGEN🤑", default_state)
async def handle_degen_message(message: Message, state: FSMContext):
    await state.set_state(Survey.name)
    await message.answer(
        "Welcome to our degen survey! What`s your name/nickname?"
    )


async def send_survey_results(message: Message, data: dict):
    text = (f"<i><b>👀 Your survey results:</b></i>\n\n"
            f"Name: <b>{data['name']}</b>\n"
            f"EVM-Wallet: <code>{data['evm_wallet']}</code>\n"
            f"Preference:: <b>{data['crypto_sphere']}</b>\n\n"
            f"<i><b>Thank you for participating!</b></i>")
    await message.answer(text=text)
