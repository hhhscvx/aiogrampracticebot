from aiogram.fsm.state import StatesGroup, State


class Survey(StatesGroup):
    name = State()
    evm_wallet = State()
    crypto_sphere = State()
