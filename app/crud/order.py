from sqlalchemy.orm import Session

from app.models.order import Order
from app.models.order_item import OrderItem
from app.models.product import Product




def create_order(
    db: Session,
    user_id: int,
    total_amount: float,
    status: str = "Pending"
):

    order = Order(
        user_id=user_id,
        total_amount=total_amount,
        status=status
    )


    db.add(order)

    db.commit()

    db.refresh(order)


    return order



def create_order_item(
    db: Session,
    order_id: int,
    product_id: int,
    quantity: int,
    price: float
):

    item = OrderItem(

        order_id=order_id,

        product_id=product_id,

        quantity=quantity,

        price=price

    )


    db.add(item)

    db.commit()

    db.refresh(item)


    return item



def get_user_orders(
    db: Session,
    user_id: int
):

    return (
        db.query(Order)
        .filter(Order.user_id == user_id)
        .all()
    )



def get_order_by_id(
    db: Session,
    order_id: int,
    user_id: int
):

    return (
        db.query(Order)
        .filter(
            Order.id == order_id,
            Order.user_id == user_id
        )
        .first()
    )



def cancel_order_by_id(
    db: Session,
    order_id: int,
    user_id: int
):

    order = (
        db.query(Order)
        .filter(
            Order.id == order_id,
            Order.user_id == user_id
        )
        .first()
    )


    if not order:
        return None, "Order not found"


    if order.status != "Pending":
        return None, f"Cannot cancel an order with status '{order.status}'"


    # Restore stock for each item
    for item in order.items:
        product = (
            db.query(Product)
            .filter(Product.id == item.product_id)
            .first()
        )
        if product:
            product.stock += item.quantity

    order.status = "Cancelled"

    db.commit()

    db.refresh(order)

    return order, None
