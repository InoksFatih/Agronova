from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.core.database import get_db
from app.core.security import get_current_user
from app.models.user import User
from app.models.scan import Scan
from app.schemas.dashboard import DashboardResponse, DashboardItem

router = APIRouter()


@router.get(
    "/dashboard",
    response_model=DashboardResponse,
    summary="Tableau de bord utilisateur",
)
async def get_dashboard(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    total_scans = (
        db.query(func.count(Scan.id))
        .filter(Scan.user_id == current_user.id)
        .scalar()
        or 0
    )

    diseased_scans = (
        db.query(func.count(Scan.id))
        .filter(Scan.user_id == current_user.id, Scan.disease_detected.is_(True))
        .scalar()
        or 0
    )

    healthy_scans = total_scans - diseased_scans

    avg_confidence = (
        db.query(func.avg(Scan.confidence))
        .filter(Scan.user_id == current_user.id)
        .scalar()
    )
    avg_confidence = float(avg_confidence) if avg_confidence is not None else 0.0

    last_scan_at = (
        db.query(func.max(Scan.created_at))
        .filter(Scan.user_id == current_user.id)
        .scalar()
    )

    top_plants_query = (
        db.query(Scan.plant_name, func.count(Scan.id).label("count"))
        .filter(Scan.user_id == current_user.id)
        .group_by(Scan.plant_name)
        .order_by(func.count(Scan.id).desc())
        .limit(5)
        .all()
    )

    top_diseases_query = (
        db.query(Scan.disease_name, func.count(Scan.id).label("count"))
        .filter(
            Scan.user_id == current_user.id,
            Scan.disease_detected.is_(True),
            Scan.disease_name.isnot(None),
        )
        .group_by(Scan.disease_name)
        .order_by(func.count(Scan.id).desc())
        .limit(5)
        .all()
    )

    top_plants = [
        DashboardItem(label=plant_name, count=count)
        for plant_name, count in top_plants_query
    ]

    top_diseases = [
        DashboardItem(label=disease_name, count=count)
        for disease_name, count in top_diseases_query
    ]

    return DashboardResponse(
        total_scans=total_scans,
        diseased_scans=diseased_scans,
        healthy_scans=healthy_scans,
        avg_confidence=round(avg_confidence, 2),
        last_scan_at=last_scan_at,
        top_plants=top_plants,
        top_diseases=top_diseases,
    )