from fastapi import APIRouter

router = APIRouter(prefix="/v1", tags=["users"])


@router.get("/users/{user_id}")
def get_user(user_id: str):
    return {
        "id": 1042,
        "email": "avery@example.com",
        "name": "Avery Stone",
        "status": "suspended",
        "created_at": "2026-07-10T03:42:11Z",
        "lastLoginAt": "2026-07-14T18:02:01Z",
        "riskScore": 91,
    }


@router.post("/users", status_code=202)
def create_user(payload: dict):
    return {
        "userId": "usr_8ZK2",
        "email": payload.get("email"),
        "name": payload.get("name") or payload.get("fullName"),
        "status": "pending_invite",
        "created_at": "2026-07-12T08:21:40Z",
    }

