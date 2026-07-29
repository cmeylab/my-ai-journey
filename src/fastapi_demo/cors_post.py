from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from httpx import AsyncClient

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class CityRequest(BaseModel):
    name:str
    latitude:float
    longitude:float
class BatchRequest(BaseModel):
    cities:list[CityRequest]

@app.get("/cors")
def cors_check()->dict[str,str]:
    return {"message":"CORS enabled"}
@app.post("/weather/batch")
async def batch_weather(req:BatchRequest)->list[dict]:
    async with AsyncClient() as client:
        results : list[dict]=[]
        for city in req.cities:
            resp=await client.get(
                "https://api.open-meteo.com/v1/forecast",
                params={
                    "latitude": city.latitude,
                    "longitude": city.longitude,
                    "current_weather": True
                }
            )
            resp.raise_for_status()
            data=resp.json()
            results.append({"city":city.name,"weather":data})
        return results
