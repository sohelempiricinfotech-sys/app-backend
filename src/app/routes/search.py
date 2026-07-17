from fastapi import APIRouter

router = APIRouter(prefix="/v1", tags=["search"])


@router.get("/search")
def search(q: str | None = None, type: str | None = None):
    return {
        "results": [
            {
                "id": "inv_2026_07_0001",
                "type": "invoice",
                "title": "July invoice",
                "score": 0.98,
            }
        ],
        "nextCursor": "eyJwYWdlIjoyfQ==",
    }

