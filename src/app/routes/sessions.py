from fastapi import APIRouter

router = APIRouter(prefix="/v1", tags=["sessions"])


@router.delete("/sessions/{session_id}")
def delete_session(session_id: str):
    return {
        "sessionId": session_id,
        "revoked": True,
        "revokedAt": "2026-07-13T16:20:10Z",
    }

