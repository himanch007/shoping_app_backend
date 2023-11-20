from fastapi import APIRouter

from .controllers.add_to_cart import router as add_to_cart_router
from .controllers.view_cart import router as view_cart_router
from .controllers.wishlist import router as wishlist_router
from .controllers.view_wishlist import router as view_wishlist_router
from .controllers.checkout import router as checkout_router


api_router = APIRouter()

api_router.include_router(add_to_cart_router, prefix='/add-to-cart', tags=['add-to-cart'])
api_router.include_router(view_cart_router, prefix='/view-cart', tags=['view-cart'])
api_router.include_router(wishlist_router, prefix='/add-to-wishlist', tags=['add-to-wishlist'])
api_router.include_router(view_wishlist_router, prefix='/view-wishlist', tags=['view-wishlist'])
api_router.include_router(checkout_router, prefix='/checkout', tags=['checkout'])
