from dataclasses import dataclass
from typing import List


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

    def __post__init(self):
        self.lng = self.latlon[-1]
        self.lat = self.latlon[0]


@dataclass
class cyWeatherAPIResponseAlertStruct:
    status: str = None
    content: List[cyWeatherAPIResponseAlertContentItemStruct] = None
