from fastapi import APIRouter, Depends, Query
from app.core.security import get_current_user
from app.models.user import User
from app.services.weather import fetch_forecast
from app.services.crop_advice import advice_for_crops
from app.schemas.weather import WeatherForecastResponse, CropAdviceResponse

router = APIRouter()

@router.get("/weather/forecast", response_model=WeatherForecastResponse, summary="Prévisions météo 7 jours")
async def weather_forecast(
    lat: float = Query(...),
    lon: float = Query(...),
    current_user: User = Depends(get_current_user),
):
    return await fetch_forecast(lat, lon)

@router.get("/weather/advice", response_model=CropAdviceResponse, summary="Conseils cultures basés sur la météo")
async def weather_advice(
    lat: float = Query(...),
    lon: float = Query(...),
    crops: str = Query("tomato,potato"),
    current_user: User = Depends(get_current_user),
):
    forecast = await fetch_forecast(lat, lon)
    crop_list = [c.strip() for c in crops.split(",")]
    return advice_for_crops(forecast, crop_list)