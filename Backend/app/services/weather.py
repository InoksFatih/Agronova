import httpx
from datetime import datetime
from app.schemas.weather import WeatherForecastResponse, WeatherDaily

OPEN_METEO_URL = "https://api.open-meteo.com/v1/forecast"

async def fetch_forecast(lat: float, lon: float) -> WeatherForecastResponse:
    params = {
        "latitude": lat,
        "longitude": lon,
        "timezone": "auto",
        "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum,precipitation_hours,windspeed_10m_max,uv_index_max",
        "forecast_days": 7,
    }

    async with httpx.AsyncClient(timeout=15) as client:
        r = await client.get(OPEN_METEO_URL, params=params)
        r.raise_for_status()
        data = r.json()

    daily = []
    d = data["daily"]
    for i in range(len(d["time"])):
        daily.append(
            WeatherDaily(
                date=d["time"][i],
                temp_max=float(d["temperature_2m_max"][i]),
                temp_min=float(d["temperature_2m_min"][i]),
                precipitation_mm=float(d["precipitation_sum"][i]),
                precipitation_hours=float(d["precipitation_hours"][i]),
                wind_max_kmh=float(d["windspeed_10m_max"][i]),
                uv_max=float(d["uv_index_max"][i]) if d.get("uv_index_max") else None,
            )
        )

    return WeatherForecastResponse(
        latitude=float(data["latitude"]),
        longitude=float(data["longitude"]),
        timezone=str(data["timezone"]),
        daily=daily,
    )