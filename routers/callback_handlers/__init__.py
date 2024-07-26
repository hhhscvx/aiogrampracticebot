__all__ = ("router",)

from aiogram import Router

from .inline_callback_handlers import router as inline_router

router = Router()

router.include_router(inline_router)
