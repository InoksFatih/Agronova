import base64
import json
from openai import OpenAI
from app.core.config import get_settings

settings = get_settings()
client = OpenAI(api_key=settings.OPENAI_API_KEY)

SYSTEM_PROMPT = """Tu es un expert agronome spécialisé dans l'identification des plantes et la détection des maladies végétales.

Quand on te montre une photo de plante, tu dois répondre UNIQUEMENT en JSON valide avec cette structure exacte :

{
    "plant_name": "Nom commun de la plante",
    "scientific_name": "Nom scientifique",
    "disease_detected": true,
    "disease_name": "Nom de la maladie ou null",
    "confidence": 0.0,
    "severity": "faible" ou "moyen" ou "élevé" ou "critique" ou null,
    "description": "Brève description de ce que tu observes",
    "treatment": {
        "curative": ["Liste des traitements curatifs"],
        "preventive": ["Liste des mesures préventives"],
        "care_tips": ["Conseils d'entretien"]
    }
}

Règles :
- Réponds UNIQUEMENT en JSON, sans texte avant ou après
- Si tu ne détectes pas de maladie, disease_name et severity sont null
- Le niveau de confiance doit être entre 0.0 et 1.0
- Les conseils doivent être pratiques et adaptés au contexte agricole
- Réponds en français
"""


def get_confidence_label(confidence: float) -> str:
    if confidence >= 0.85:
        return "Très fiable"
    if confidence >= 0.60:
        return "Fiable"
    return "Incertain"


async def analyze_plant_image(image_bytes: bytes, content_type: str) -> dict:
    """Analyze a plant image using OpenAI Vision and return a validated diagnosis dict."""

    base64_image = base64.b64encode(image_bytes).decode("utf-8")

    allowed_types = ["image/jpeg", "image/png", "image/webp", "image/gif"]
    media_type = content_type if content_type in allowed_types else "image/jpeg"

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Analyse cette photo de plante. Identifie la plante et détecte toute maladie présente. Réponds uniquement en JSON valide.",
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:{media_type};base64,{base64_image}"
                        },
                    },
                ],
            },
        ],
        max_tokens=1000,
        temperature=0.2,
    )

    result_text = response.choices[0].message.content.strip()

    if result_text.startswith("```"):
        result_text = result_text.split("\n", 1)[1]
        result_text = result_text.rsplit("```", 1)[0].strip()

    try:
        result = json.loads(result_text)
    except json.JSONDecodeError:
        raise ValueError("La réponse du modèle n'est pas un JSON valide.")

    result.setdefault("plant_name", "Inconnue")
    result.setdefault("scientific_name", None)
    result.setdefault("disease_detected", False)
    result.setdefault("disease_name", None)
    result.setdefault("confidence", 0.0)
    result.setdefault("severity", None)
    result.setdefault("description", "Aucune description.")
    result.setdefault(
        "treatment",
        {
            "curative": [],
            "preventive": [],
            "care_tips": [],
        },
    )

    if not isinstance(result["treatment"], dict):
        result["treatment"] = {
            "curative": [],
            "preventive": [],
            "care_tips": [],
        }

    result["treatment"].setdefault("curative", [])
    result["treatment"].setdefault("preventive", [])
    result["treatment"].setdefault("care_tips", [])

    try:
        result["confidence"] = float(result["confidence"])
    except (TypeError, ValueError):
        result["confidence"] = 0.0

    if result["confidence"] < 0.0:
        result["confidence"] = 0.0
    if result["confidence"] > 1.0:
        result["confidence"] = 1.0

    result["confidence_label"] = get_confidence_label(result["confidence"])

    allowed_severities = ["faible", "moyen", "élevé", "critique", None]
    if result["severity"] not in allowed_severities:
        result["severity"] = None

    if not result["disease_detected"]:
        result["disease_name"] = None
        result["severity"] = None

    return result
