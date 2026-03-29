from typing import List, Optional, Literal
from pydantic import BaseModel


class WeatherDaily(BaseModel):
    date: str
    temp_max: float
    temp_min: float
    precipitation_mm: float
    precipitation_hours: float
    wind_max_kmh: float
    uv_max: Optional[float] = None


class WeatherForecastResponse(BaseModel):
    latitude: float
    longitude: float
    timezone: str
    daily: List[WeatherDaily]


class CropAction(BaseModel):
    title: str
    reason: str
    when: str
    priority: Literal["low", "medium", "high", "critical"]


class CropAdviceResponse(BaseModel):
    crops: List[str]
    summary: str
    actions: List[CropAction]
    raw_forecast: WeatherForecastResponse