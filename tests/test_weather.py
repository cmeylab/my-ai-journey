from src.weather import *
import pytest

def test_get_coords()->None:
    lat,lon=get_coords("北京")
    assert isinstance(lat,float)
    assert isinstance(lon,float)
def test_get_weather()->None:
    lat,lon=get_coords("上海")
    data=get_weather(lat,lon)
    assert "current_weather" in data
def test_unknown_city()->None:
    try:
        get_coords("这个城市不存在")
        assert False,"应该抛出异常"
    except Exception:
        pass