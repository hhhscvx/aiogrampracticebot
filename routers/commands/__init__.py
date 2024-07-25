__all__ = ("router", )  # отсюда импортим только router (интересно🤔)

from aiogram import Router

from .base_commands import router as base_commands_router
from .user_commands import router as user_commands_router

router = Router()

router.include_routers(base_commands_router,
                       user_commands_router)
