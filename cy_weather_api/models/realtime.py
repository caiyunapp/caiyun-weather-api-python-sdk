from dataclasses import dataclass
from typing import Union


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
    nearest: cyWeatherAPIResponseRealtimePrecipitationItemNearestStruct = None


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
    pm25: float = None
    pm10: float = None
    o3: float = None
    so2: float = None
    no2: float = None
    co: float = None


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
    skycon: str
    visibility: float
    dswrf: float
    wind: cyWeatherAPIResponseRealtimeWindStruct
    pressure: float
    apparent_temperature: float
    precipitation: cyWeatherAPIResponseRealtimePrecipitationStruct
    air_quality: cyWeatherAPIResponseRealtimeAirQualityStruct
    life_index: cyWeatherAPIResponseRealtimeLifeIndexStruct
