"""Dataclass for Caiyun Weather API.

Below dataclasses arr based on Caiyun Weather API v2.5, the offical API docs:

    zh_CN: https://open.caiyunapp.com/通用预报接口/v2.5
    en_US: https://open.caiyunapp.com/General_weather_interface/v2.5

We encourage use Golang's coding style:

    1. Use black as format tool.
    2. Use Camel-Case.
    3. Avoid complex oop tricks.
"""

import json
from dataclasses import asdict, dataclass, is_dataclass
from typing import Dict, List

import orjson
from dacite import from_dict

from cy_weather_api.models.result import cyWeatherAPIResponseResultStruct


class EnhancedJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if is_dataclass(o):
            return asdict(o)
        return super().default(o)


@dataclass
class CyWeatherAPIResponseHandler:
    status: str
    api_version: str
    api_status: str
    lang: str
    unit: str
    tzshift: int
    timezone: str
    server_time: int
    location: List[float]
    result: cyWeatherAPIResponseResultStruct

    def __post_init__(self):
        pass

    def dumps(self, ensure_text=True) -> bytes:
        """Fast dumps via orjson.

        Check orjson docs for details: https://github.com/ijl/orjson#dataclass
        """
        if ensure_text:
            return orjson.dumps(self).decode("utf-8")
        else:
            return orjson.dumps(self)

    def dumps_pretty(self, **kwargs) -> str:
        """Dumps JSON with indent.

        Note: please do not change `cls` option if you don't know it.
        """
        return json.dumps(self, cls=EnhancedJSONEncoder, **kwargs)


def initFromDict(data: Dict) -> CyWeatherAPIResponseHandler:
    return from_dict(data_class=CyWeatherAPIResponseHandler, data=data)


if __name__ == "__main__":
    import requests

    # NOTE: Test token, no one can ensure its availability.
    TOKEN = "TAkhjf8d1nlSlspN"
    LNG, LAT = 116.3883, 39.9289
    URL = "http://api.caiyunapp.com/v2.5/{TOKEN}/{LNG},{LAT}/weather".format(
        TOKEN=TOKEN, LNG=LNG, LAT=LAT
    )

    apiResponseDataclass = from_dict(
        data_class=CyWeatherAPIResponseHandler, data=requests.get(URL).json()
    )
    print(apiResponseDataclass.dumps())
