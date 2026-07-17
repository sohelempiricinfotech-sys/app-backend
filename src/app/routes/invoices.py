from fastapi import APIRouter

router = APIRouter(prefix="/v1", tags=["invoices"])


@router.get("/invoices/{invoice_id}")
def get_invoice(invoice_id: str):
    return {
        "id": invoice_id,
        "orderId": "ord_9001",
        "total": 1299.5,
        "currency": "USD",
        "status": "paid",
        "dueDate": None,
        "taxId": "GSTIN-29ABCDE1234F1Z5",
        "legacyDiscountCode": "JULY-LEGACY",
    }

