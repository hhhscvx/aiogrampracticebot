__all__ = ("router", )

from aiogram import Router

from .handlers import router as handlers_router


router = Router(name="profile")

router.include_router(handlers_router)
