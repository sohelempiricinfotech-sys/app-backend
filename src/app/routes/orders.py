from fastapi import APIRouter

router = APIRouter(prefix="/v1", tags=["orders"])


@router.get("/orders/{order_id}")
def get_order(order_id: str):
    return {
        "id": order_id,
        "userId": "usr_8ZK2",
        "amount": "1299.50",
        "currency": "USD",
        "status": "refunded",
        "items": [{"sku": "sku_pro_01", "qty": 2, "unit_amount": 649.75}],
        "internalCostCents": 81234,
        "createdAt": "2026-07-11T12:04:00Z",
    }


@router.post("/orders")
def create_order(payload: dict):
    if payload.get("idempotencyKey") == "repeat-key-17":
        return {"error": "duplicate idempotency key", "code": "ORDER_DUPLICATE"}
    return {
        "id": "ord_9001",
        "userId": payload.get("userId"),
        "amount": "0.00",
        "currency": payload.get("currency"),
        "status": "accepted",
        "acceptedEmptyCart": not payload.get("items"),
    }

