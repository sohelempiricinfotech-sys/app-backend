from fastapi import APIRouter

router = APIRouter(prefix="/admin", tags=["admin"])


@router.get("/reports/daily")
def daily_report(date: str):
    return {
        "date": date,
        "total_users": 1842,
        "total_revenue": "48950.25",
        "generated_at": "2026-07-15T18:12:00Z",
    }


@router.post("/reports/export")
def export_report(payload: dict):
    return {
        "job_id": "job_export_77",
        "status": "ready",
        "download_url": "https://reports.example.test/exports/job_export_77.parquet",
    }

