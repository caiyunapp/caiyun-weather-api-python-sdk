from dataclasses import dataclass
from typing import Any, List, Union


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
    value: str


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
    precipitation: List[cyWeatherAPIResponseDailyMaxMinAvgItemStruct]
    temperature: List[cyWeatherAPIResponseDailyMaxMinAvgItemStruct]
    humidity: List[cyWeatherAPIResponseDailyMaxMinAvgItemStruct]
    cloudrate: List[cyWeatherAPIResponseDailyMaxMinAvgItemStruct]
    pressure: List[cyWeatherAPIResponseDailyMaxMinAvgItemStruct]
    visibility: List[cyWeatherAPIResponseDailyMaxMinAvgItemStruct]
    dswrf: List[cyWeatherAPIResponseDailyMaxMinAvgItemStruct]
    wind: List[cyWeatherAPIResponseDailyWindItemStruct]
    skycon: List[cyWeatherAPIResponseDailySkyconItemStruct]
    skycon_08h_20h: List[cyWeatherAPIResponseDailySkyconItemStruct]
    skycon_20h_32h: List[cyWeatherAPIResponseDailySkyconItemStruct]
    life_index: cyWeatherAPIResponseDailyLifeIndexItemStruct
