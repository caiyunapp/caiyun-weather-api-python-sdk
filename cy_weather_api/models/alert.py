from dataclasses import dataclass
from typing import List, Optional


@dataclass
class cyWeatherAPIResponseAlertAdcodeItemStruct:
    adcode: int
    name: str


@dataclass
class cyWeatherAPIResponseAlertContentItemStruct:
    province: str
    status: str
    code: str
    description: str
    pubtimestamp: float
    city: str
    adcode: str
    regionId: str
    latlon: List[float]
    county: str
    alertId: str
    request_status: str
    source: str
    title: str
    location: str


@dataclass
class cyWeatherAPIResponseAlertStruct:
    status: Optional[str] = None
    content: Optional[List[cyWeatherAPIResponseAlertContentItemStruct]] = None
    adcodes: Optional[List[cyWeatherAPIResponseAlertAdcodeItemStruct]] = None
