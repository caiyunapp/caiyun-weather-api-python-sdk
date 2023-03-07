from dataclasses import dataclass
from typing import Any, List, Union


@dataclass
class cyWeatherAPIResponseHourlyPrecipitationItemStruct:
    datetime: str
    value: float
    probability: float

@dataclass
class cyWeatherAPIResponseHourlyWindStruct:
    datetime: str
    speed: Union[float, int]
    direction: Union[float, int]


@dataclass
class cyWeatherAPIResponseHourlyAirQualityItemValue:
    chn: float
    usa: float


@dataclass
class cyWeatherAPIResponseHourlyAirQualityItem:
    datetime: str
    value: cyWeatherAPIResponseHourlyAirQualityItemValue


@dataclass
class cyWeatherAPIResponseHourlyAirQualityPM25Item:
    datetime: str
    value: float


@dataclass
class cyWeatherAPIResponseHourlyAirQuality:
    aqi: List[cyWeatherAPIResponseHourlyAirQualityItem]
    pm25: List[cyWeatherAPIResponseHourlyAirQualityPM25Item]


@dataclass
class cyWeatherAPIResponseHourlySimpleDatetimeValuePair:
    datetime: str
    value: Any


@dataclass
class cyWeatherAPIResponseHourlyStruct:
    status: str
    description: str
    precipitation: List[cyWeatherAPIResponseHourlyPrecipitationItemStruct]
    temperature: List[cyWeatherAPIResponseHourlySimpleDatetimeValuePair]
    apparent_temperature: List[cyWeatherAPIResponseHourlySimpleDatetimeValuePair]
    humidity: List[cyWeatherAPIResponseHourlySimpleDatetimeValuePair]
    cloudrate: List[cyWeatherAPIResponseHourlySimpleDatetimeValuePair]
    skycon: List[cyWeatherAPIResponseHourlySimpleDatetimeValuePair]
    pressure: List[cyWeatherAPIResponseHourlySimpleDatetimeValuePair]
    visibility: List[cyWeatherAPIResponseHourlySimpleDatetimeValuePair]
    dswrf: List[cyWeatherAPIResponseHourlySimpleDatetimeValuePair]
    wind: List[cyWeatherAPIResponseHourlyWindStruct]
    air_quality: cyWeatherAPIResponseHourlyAirQuality
