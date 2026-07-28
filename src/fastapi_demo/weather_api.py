from fastapi import FastAPI
from httpx import AsyncClient

app = FastAPI()
@app.get("/weather")
async def get_weather(city:str)->dict:
    async with AsyncClient() as client:
        resp = await client.get(
            "https://api.open-meteo.com/v1/forecast",
            params={"latitude": 39.9, "longitude": 116.4, "current_weather": True},
        )
        resp.raise_for_status()
        return resp.json()