from dataclasses import dataclass
from typing import Optional, Union

from cy_weather_api.models.skycon import CySkyCon


@dataclass
class cyWeatherAPIResponseRealtimeWindStruct:
    speed: Union[float, int]
    direction: Union[float, int]


@dataclass
class cyWeatherAPIResponseRealtimePrecipitationItemLocalStruct:
    status: str
    datasource: str
    intensity: float


@dataclass
class cyWeatherAPIResponseRealtimePrecipitationItemNearestStruct:
    status: str
    distance: float
    intensity: float


@dataclass
class cyWeatherAPIResponseRealtimePrecipitationStruct:
    local: cyWeatherAPIResponseRealtimePrecipitationItemLocalStruct
    nearest: Optional[cyWeatherAPIResponseRealtimePrecipitationItemNearestStruct] = None


@dataclass
class cyWeatherAPIResponseRealtimeAirQualityAQIValueStruct:
    chn: float
    usa: float


@dataclass
class cyWeatherAPIResponseRealtimeAirQualityAQIDescStruct:
    chn: str
    usa: str


@dataclass
class cyWeatherAPIResponseRealtimeAirQualityStruct:
    aqi: cyWeatherAPIResponseRealtimeAirQualityAQIValueStruct
    description: cyWeatherAPIResponseRealtimeAirQualityAQIDescStruct
    pm25: Optional[float] = None
    pm10: Optional[float] = None
    o3: Optional[float] = None
    so2: Optional[float] = None
    no2: Optional[float] = None
    co: Optional[float] = None


@dataclass
class cyWeatherAPIResponseRealtimeLifeIndexItemStruct:
    index: float
    desc: str


@dataclass
class cyWeatherAPIResponseRealtimeLifeIndexStruct:
    ultraviolet: cyWeatherAPIResponseRealtimeLifeIndexItemStruct
    comfort: cyWeatherAPIResponseRealtimeLifeIndexItemStruct


@dataclass
class cyWeatherAPIResponseRealtimeStruct:
    status: str
    temperature: float
    humidity: float
    cloudrate: float
    skycon: CySkyCon
    visibility: float
    dswrf: float
    wind: cyWeatherAPIResponseRealtimeWindStruct
    pressure: float
    apparent_temperature: float
    precipitation: cyWeatherAPIResponseRealtimePrecipitationStruct
    air_quality: cyWeatherAPIResponseRealtimeAirQualityStruct
    life_index: cyWeatherAPIResponseRealtimeLifeIndexStruct
