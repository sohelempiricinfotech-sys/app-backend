from fastapi import APIRouter, Response

router = APIRouter(prefix="/v1", tags=["profiles"])


@router.get("/profiles/{profile_id}")
def get_profile(profile_id: str):
    return Response(status_code=404)


@router.get("/feature-flags")
def get_feature_flags():
    return {"flags": [{"key": "new_checkout", "enabled": True}]}

