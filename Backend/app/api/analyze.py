import os
import uuid
import base64
from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from openai import APIConnectionError, APITimeoutError, AuthenticationError, RateLimitError
from sqlalchemy.orm import Session

from app.schemas.analysis import AnalysisResponse, ErrorResponse
from app.services.analysis import analyze_plant_image
from app.core.database import get_db
from app.core.security import get_current_user
from app.models.user import User
from app.models.scan import Scan

router = APIRouter()

UPLOAD_DIR = "uploads/scans"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post(
    "/analyze",
    response_model=AnalysisResponse,
    responses={
        400: {"model": ErrorResponse},
        500: {"model": ErrorResponse},
    },
    summary="Analyser une photo de plante",
    description="Envoie une photo de plante pour recevoir un diagnostic IA.",
)
async def analyze_plant(
    file: UploadFile = File(
        ..., description="Photo de la plante (JPEG, PNG, WebP, GIF)"
    ),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    allowed_types = ["image/jpeg", "image/png", "image/webp", "image/gif"]

    if file.content_type not in allowed_types:
        raise HTTPException(
            status_code=400,
            detail=f"Type de fichier non supporté : {file.content_type}. Utilisez JPEG, PNG, WebP ou GIF.",
        )

    contents = await file.read()

    if len(contents) > 10 * 1024 * 1024:
        raise HTTPException(
            status_code=400,
            detail="Image trop volumineuse. Taille maximum : 10 Mo.",
        )

    extension_map = {
        "image/jpeg": ".jpg",
        "image/png": ".png",
        "image/webp": ".webp",
        "image/gif": ".gif",
    }

    file_ext = extension_map.get(file.content_type, ".jpg")
    filename = f"{uuid.uuid4()}{file_ext}"
    file_path = os.path.join(UPLOAD_DIR, filename).replace("\\", "/")

    try:
        with open(file_path, "wb") as f:
            f.write(contents)

        result = await analyze_plant_image(contents, file.content_type)

        scan = Scan(
            user_id=current_user.id,
            image_path=file_path,
            image_data=base64.b64encode(contents).decode("ascii"),
            image_mime_type=file.content_type,
            plant_name=result["plant_name"],
            scientific_name=result.get("scientific_name"),
            disease_detected=result["disease_detected"],
            disease_name=result.get("disease_name"),
            confidence=result["confidence"],
            confidence_label=result.get("confidence_label"),
            severity=result.get("severity"),
            description=result.get("description"),
            treatment_json=result.get("treatment", {}),
        )

        db.add(scan)
        db.commit()
        db.refresh(scan)

        return AnalysisResponse(**result)

    except ValueError as e:
        db.rollback()

        if os.path.exists(file_path):
            os.remove(file_path)

        raise HTTPException(
            status_code=400,
            detail=str(e),
        )

    except APIConnectionError:
        db.rollback()

        if os.path.exists(file_path):
            os.remove(file_path)

        raise HTTPException(
            status_code=503,
            detail=(
                "Le serveur n’a pas pu joindre l’API OpenAI (erreur réseau). "
                "Sur la machine où tourne le backend, vérifiez la connexion Internet, "
                "le pare-feu / antivirus (autoriser HTTPS vers api.openai.com) et tout proxy ou VPN."
            ),
        )

    except APITimeoutError:
        db.rollback()

        if os.path.exists(file_path):
            os.remove(file_path)

        raise HTTPException(
            status_code=504,
            detail="L’API OpenAI n’a pas répondu à temps. Réessayez dans un instant.",
        )

    except AuthenticationError:
        db.rollback()

        if os.path.exists(file_path):
            os.remove(file_path)

        raise HTTPException(
            status_code=502,
            detail="Clé API OpenAI refusée. Vérifiez OPENAI_API_KEY dans le fichier .env du backend.",
        )

    except RateLimitError:
        db.rollback()

        if os.path.exists(file_path):
            os.remove(file_path)

        raise HTTPException(
            status_code=429,
            detail="Limite de requêtes OpenAI atteinte. Réessayez plus tard.",
        )

    except Exception as e:
        db.rollback()

        if os.path.exists(file_path):
            os.remove(file_path)

        raise HTTPException(
            status_code=500,
            detail=f"Erreur lors de l'analyse : {str(e)}",
        )
