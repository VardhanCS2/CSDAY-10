from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)


from sqlalchemy.orm import Session


from app.database.database import get_db


from app.models.user import User


from app.schemas.order import OrderResponse


from app.api.deps import get_current_user


from app.services.order_service import (
    place_order,
    get_orders,
    get_order,
    cancel_order
)


from app.utils.response import success_response



router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)



@router.post("/")
def create_order(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    order = place_order(
        db,
        current_user.id
    )


    return success_response(
        data=order,
        message="Order placed successfully"
    )



@router.get("/")
def read_orders(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    orders = get_orders(
        db,
        current_user.id
    )


    return success_response(
        data=orders,
        message="Orders fetched successfully"
    )



@router.get("/{order_id}")
def read_order(
    order_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    order = get_order(
        db,
        order_id,
        current_user.id
    )


    if not order:

        raise HTTPException(
            status_code=404,
            detail="Order not found"
        )


    return success_response(
        data=order,
        message="Order fetched successfully"
    )



@router.patch("/{order_id}/cancel")
def cancel_user_order(
    order_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Cancel a Pending order. Stock is automatically restored.
    Orders with status other than 'Pending' cannot be cancelled.
    """

    order, error = cancel_order(
        db,
        order_id,
        current_user.id
    )


    if error:
        status_code = 404 if "not found" in error.lower() else 400
        raise HTTPException(
            status_code=status_code,
            detail=error
        )


    return success_response(
        data=order,
        message="Order cancelled successfully"
    )