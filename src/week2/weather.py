from __future__ import annotations

from pathlib import Path
from typing import Any

import requests

DATA_DIR = Path(__file__).resolve().parent.parent.parent / "data"


def get_coords(city: str) -> tuple[float, float]:
    resp = requests.get(
        "https://geocoding-api.open-meteo.com/v1/search",
        params={"name": city, "count": 1, "language": "zh", "format": "json"},
    )
    resp.raise_for_status()
    r = resp.json()["results"][0]
    return r["latitude"], r["longitude"]


def get_weather(lat: float, lon: float) -> dict[str, Any]:
    resp = requests.get(
        "https://api.open-meteo.com/v1/forecast",
        params={"latitude": lat, "longitude": lon, "current_weather": True},
    )
    resp.raise_for_status()
    return resp.json()  # type: ignore[no-any-return]


def main() -> None:
    city = input("Enter city name: ")
    lat, lon = get_coords(city)
    w = get_weather(lat, lon)["current_weather"]
    print(f"{city}:{w['temperature']}°C,风速 {w['windspeed']} km/h")


if __name__ == "__main__":
    main()
