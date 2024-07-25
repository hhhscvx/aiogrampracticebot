__all__ = ("router", )

from aiogram import Router

from .commands import router as commands_router
from .common import router as common_router

router = Router(name=__name__)

router.include_router(commands_router)

# this router must be included last
router.include_router(common_router)
