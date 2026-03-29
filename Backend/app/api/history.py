from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import get_current_user
from app.models.user import User
from app.models.scan import Scan
from app.schemas.scan import ScanResponse
from app.schemas.auth import MessageResponse

router = APIRouter()


@router.get(
    "/history",
    response_model=list[ScanResponse],
    summary="Historique des scans",
)
async def get_history(
    disease_only: bool = Query(False, description="Retourner uniquement les scans avec maladie détectée"),
    plant_name: str | None = Query(None, description="Filtrer par nom de plante"),
    skip: int = Query(0, ge=0, description="Nombre d'éléments à ignorer"),
    limit: int = Query(20, ge=1, le=100, description="Nombre maximum d'éléments à retourner"),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    query = db.query(Scan).filter(Scan.user_id == current_user.id)

    if disease_only:
        query = query.filter(Scan.disease_detected.is_(True))

    if plant_name:
        query = query.filter(Scan.plant_name.ilike(f"%{plant_name}%"))

    scans = (
        query
        .order_by(Scan.created_at.desc())
        .offset(skip)
        .limit(limit)
        .all()
    )

    return [ScanResponse.model_validate(scan) for scan in scans]


@router.get(
    "/history/{scan_id}",
    response_model=ScanResponse,
    summary="Détail d'un scan",
)
async def get_scan_by_id(
    scan_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    scan = (
        db.query(Scan)
        .filter(Scan.id == scan_id, Scan.user_id == current_user.id)
        .first()
    )

    if not scan:
        raise HTTPException(status_code=404, detail="Scan introuvable.")

    return ScanResponse.model_validate(scan)


@router.delete(
    "/history/{scan_id}",
    response_model=MessageResponse,
    summary="Supprimer un scan",
)
async def delete_scan(
    scan_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    scan = (
        db.query(Scan)
        .filter(Scan.id == scan_id, Scan.user_id == current_user.id)
        .first()
    )

    if not scan:
        raise HTTPException(status_code=404, detail="Scan introuvable.")

    db.delete(scan)
    db.commit()

    return MessageResponse(message="Scan supprimé avec succès.")