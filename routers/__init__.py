__all__ = ("router", )

from aiogram import Router

from .commands import router as commands_router
from .common import router as common_router
from .arni_copypast import router as arni_router
from .callback_handlers import router as callback_router
from .profile import router as profile_router

router = Router(name=__name__)

router.include_routers(callback_router,
                       commands_router,
                       profile_router,
                       arni_router)

# this router must be included last
router.include_router(common_router)
