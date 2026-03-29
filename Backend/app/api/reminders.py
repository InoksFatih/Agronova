from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import get_current_user
from app.models.user import User
from app.models.reminder import Reminder
from app.schemas.reminder import ReminderCreate, ReminderUpdate, ReminderResponse
from app.schemas.auth import MessageResponse

router = APIRouter()


@router.post(
    "/reminders",
    response_model=ReminderResponse,
    summary="Créer un rappel",
)
async def create_reminder(
    payload: ReminderCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    reminder = Reminder(
        user_id=current_user.id,
        title=payload.title,
        description=payload.description,
        due_date=payload.due_date,
        completed=False,
    )

    db.add(reminder)
    db.commit()
    db.refresh(reminder)

    return ReminderResponse.model_validate(reminder)


@router.get(
    "/reminders",
    response_model=list[ReminderResponse],
    summary="Lister mes rappels",
)
async def get_reminders(
    completed: bool | None = Query(None, description="Filtrer par statut terminé/non terminé"),
    skip: int = Query(0, ge=0),
    limit: int = Query(20, ge=1, le=100),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    query = db.query(Reminder).filter(Reminder.user_id == current_user.id)

    if completed is not None:
        query = query.filter(Reminder.completed == completed)

    reminders = (
        query
        .order_by(Reminder.due_date.asc())
        .offset(skip)
        .limit(limit)
        .all()
    )

    return [ReminderResponse.model_validate(reminder) for reminder in reminders]


@router.get(
    "/reminders/{reminder_id}",
    response_model=ReminderResponse,
    summary="Détail d'un rappel",
)
async def get_reminder_by_id(
    reminder_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    reminder = (
        db.query(Reminder)
        .filter(Reminder.id == reminder_id, Reminder.user_id == current_user.id)
        .first()
    )

    if not reminder:
        raise HTTPException(status_code=404, detail="Rappel introuvable.")

    return ReminderResponse.model_validate(reminder)


@router.put(
    "/reminders/{reminder_id}",
    response_model=ReminderResponse,
    summary="Modifier un rappel",
)
async def update_reminder(
    reminder_id: int,
    payload: ReminderUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    reminder = (
        db.query(Reminder)
        .filter(Reminder.id == reminder_id, Reminder.user_id == current_user.id)
        .first()
    )

    if not reminder:
        raise HTTPException(status_code=404, detail="Rappel introuvable.")

    if payload.title is not None:
        reminder.title = payload.title

    if payload.description is not None:
        reminder.description = payload.description

    if payload.due_date is not None:
        reminder.due_date = payload.due_date

    if payload.completed is not None:
        reminder.completed = payload.completed

    db.commit()
    db.refresh(reminder)

    return ReminderResponse.model_validate(reminder)


@router.delete(
    "/reminders/{reminder_id}",
    response_model=MessageResponse,
    summary="Supprimer un rappel",
)
async def delete_reminder(
    reminder_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    reminder = (
        db.query(Reminder)
        .filter(Reminder.id == reminder_id, Reminder.user_id == current_user.id)
        .first()
    )

    if not reminder:
        raise HTTPException(status_code=404, detail="Rappel introuvable.")

    db.delete(reminder)
    db.commit()

    return MessageResponse(message="Rappel supprimé avec succès.")