from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from sqlalchemy import inspect, text
from app.core.config import get_settings
from app.core.database import engine, Base
from app.api.analyze import router as analyze_router
from app.api.auth import router as auth_router
from app.api.history import router as history_router
from app.api.weather import router as weather_router
from app.api.dashboard import router as dashboard_router
from app.models.user import User
from app.models.scan import Scan
from app.api.reminders import router as reminders_router
from app.models.reminder import Reminder

settings = get_settings()

Base.metadata.create_all(bind=engine)


def ensure_scan_image_columns() -> None:
    inspector = inspect(engine)
    if "scans" not in inspector.get_table_names():
        return

    cols = {c["name"] for c in inspector.get_columns("scans")}
    with engine.begin() as conn:
        if "image_data" not in cols:
            conn.execute(text("ALTER TABLE scans ADD COLUMN image_data TEXT"))
        if "image_mime_type" not in cols:
            conn.execute(text("ALTER TABLE scans ADD COLUMN image_mime_type VARCHAR(100)"))


ensure_scan_image_columns()

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="API Agronova — Intelligence artificielle pour l'agriculture",
)

app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router, prefix="/api/auth", tags=["Authentification"])
app.include_router(analyze_router, prefix="/api", tags=["Analyse"])
app.include_router(history_router, prefix="/api", tags=["Historique"])
app.include_router(weather_router, prefix="/api", tags=["Météo"])
app.include_router(dashboard_router, prefix="/api", tags=["Dashboard"])
app.include_router(reminders_router, prefix="/api", tags=["Rappels"])
@app.get("/")
async def root():
    return {
        "app": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "status": "running",
        "message": "Bienvenue sur l'API Agronova 🌱",
    }


@app.get("/health")
async def health_check():
    return {"status": "healthy"}