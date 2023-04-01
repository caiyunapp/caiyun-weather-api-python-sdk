from dataclasses import dataclass
from typing import Any, List, Union

from cy_weather_api.models.skycon import CySkyCon


@dataclass
class cyWeatherAPIResponseDailyAstroItemTimeStruct:
    time: str


@dataclass
class cyWeatherAPIResponseDailyAstroItemStruct:
    date: str
    sunrise: cyWeatherAPIResponseDailyAstroItemTimeStruct
    sunset: cyWeatherAPIResponseDailyAstroItemTimeStruct


@dataclass
class cyWeatherAPIResponseDailyMaxMinAvgItemStruct:
    date: str
    max: float
    min: float
    avg: float


@dataclass
class cyWeatherAPIResponseDailyPrecipitationItemStruct:
    date: str
    max: float
    min: float
    avg: float
    probability: float


@dataclass
class cyWeatherAPIResponseDailyWindItemPropertyStruct:
    speed: Union[float, int]
    direction: Union[float, int]


@dataclass
class cyWeatherAPIResponseDailyWindItemStruct:
    date: str
    max: cyWeatherAPIResponseDailyWindItemPropertyStruct
    min: cyWeatherAPIResponseDailyWindItemPropertyStruct
    avg: cyWeatherAPIResponseDailyWindItemPropertyStruct


@dataclass
class cyWeatherAPIResponseDailyAirQualityItemAQITypeStruct:
    chn: float
    usa: float


@dataclass
class cyWeatherAPIResponseDailyAirQualityItemAQIStruct:
    date: str
    max: cyWeatherAPIResponseDailyAirQualityItemAQITypeStruct
    min: cyWeatherAPIResponseDailyAirQualityItemAQITypeStruct
    avg: cyWeatherAPIResponseDailyAirQualityItemAQITypeStruct


@dataclass
class cyWeatherAPIResponseDailyAirQualityItemStruct:
    aqi: List[cyWeatherAPIResponseDailyAirQualityItemAQIStruct]
    pm25: List[cyWeatherAPIResponseDailyMaxMinAvgItemStruct]


@dataclass
class cyWeatherAPIResponseDailySkyconItemStruct:
    date: str
    value: CySkyCon


@dataclass
class cyWeatherAPIResponseDailyDateIndexDescItemStruct:
    date: str
    index: Any
    desc: str


@dataclass
class cyWeatherAPIResponseDailyLifeIndexItemStruct:
    ultraviolet: List[cyWeatherAPIResponseDailyDateIndexDescItemStruct]
    carWashing: List[cyWeatherAPIResponseDailyDateIndexDescItemStruct]
    dressing: List[cyWeatherAPIResponseDailyDateIndexDescItemStruct]
    comfort: List[cyWeatherAPIResponseDailyDateIndexDescItemStruct]
    coldRisk: List[cyWeatherAPIResponseDailyDateIndexDescItemStruct]


@dataclass
class cyWeatherAPIResponseDailyStruct:
    status: str
    astro: List[cyWeatherAPIResponseDailyAstroItemStruct]
    precipitation: List[cyWeatherAPIResponseDailyPrecipitationItemStruct]
    precipitation_08h_20h: List[cyWeatherAPIResponseDailyPrecipitationItemStruct]
    precipitation_20h_32h: List[cyWeatherAPIResponseDailyPrecipitationItemStruct]
    temperature: List[cyWeatherAPIResponseDailyMaxMinAvgItemStruct]
    temperature_08h_20h: List[cyWeatherAPIResponseDailyMaxMinAvgItemStruct]
    temperature_20h_32h: List[cyWeatherAPIResponseDailyMaxMinAvgItemStruct]
    humidity: List[cyWeatherAPIResponseDailyMaxMinAvgItemStruct]
    cloudrate: List[cyWeatherAPIResponseDailyMaxMinAvgItemStruct]
    pressure: List[cyWeatherAPIResponseDailyMaxMinAvgItemStruct]
    visibility: List[cyWeatherAPIResponseDailyMaxMinAvgItemStruct]
    dswrf: List[cyWeatherAPIResponseDailyMaxMinAvgItemStruct]
    wind: List[cyWeatherAPIResponseDailyWindItemStruct]
    wind_08h_20h: List[cyWeatherAPIResponseDailyWindItemStruct]
    wind_20h_32h: List[cyWeatherAPIResponseDailyWindItemStruct]
    skycon: List[cyWeatherAPIResponseDailySkyconItemStruct]
    skycon_08h_20h: List[cyWeatherAPIResponseDailySkyconItemStruct]
    skycon_20h_32h: List[cyWeatherAPIResponseDailySkyconItemStruct]
    life_index: cyWeatherAPIResponseDailyLifeIndexItemStruct
    air_quality: cyWeatherAPIResponseDailyAirQualityItemStruct
