from fastapi import APIRouter, Header, Request
from shoping_app.models.add_to_cart import AddToCart

router = APIRouter()


@router.get("", status_code=200)
async def view_cart(request: Request, auth_token: str = Header(alias="authorization")):


    user_data = request.user_data
    user_id = user_data.pop('_id')

    products_in_cart = await AddToCart.Model.objects.products_in_cart(user_id)
    
    return {
        "products": products_in_cart
    }
