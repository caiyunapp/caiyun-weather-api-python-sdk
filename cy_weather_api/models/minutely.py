from dataclasses import dataclass
from typing import List


@dataclass
class cyWeatherAPIResponseMinutelyStruct:
    status: str
    datasource: str
    precipitation_2h: List[float]
    precipitation: List[float]
    probability: List[float]
    description: str
