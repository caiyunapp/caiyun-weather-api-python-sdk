"""Dataclasses for Caiyun Weather API.

Below dataclasses arr based on Caiyun Weather API v2.6, the offical API docs:
https://docs.caiyunapp.com/docs/intro
"""

import json
from dataclasses import asdict, dataclass, is_dataclass
from typing import Dict, List, Union

import orjson
from dacite import Config, from_dict

from cy_weather_api.models.result import cyWeatherAPIResponseResultStruct
from cy_weather_api.models.skycon import CySkyCon


class EnhancedJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if is_dataclass(o):
            return asdict(o)
        return super().default(o)


@dataclass
class CyWeatherResponse:
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

    def dumps(self, ensure_text=True) -> Union[bytes, str]:
        """Fast dumps via orjson.

        Check orjson docs for details: https://github.com/ijl/orjson#dataclass
        """
        v = orjson.dumps(self)
        if ensure_text:
            v = v.decode("utf-8")
        return v

    def dumps_pretty(self, **kwargs) -> str:
        """Dumps JSON with indent.

        Note: please do not change `cls` option if you don't know it.
        """
        return json.dumps(self, cls=EnhancedJSONEncoder, **kwargs)

    @classmethod
    def from_dict(cls, data: Dict) -> "CyWeatherResponse":
        return from_dict(data_class=cls, data=data, config=Config(cast=[CySkyCon]))


if __name__ == "__main__":
    import httpx

    # NOTE: Test token, no one can ensure its availability.
    token = "TAkhjf8d1nlSlspN"
    lng, lat = 116.3883, 39.9289
    url = f"https://api.caiyunapp.com/v2.6/{token}/{lng},{lat}/weather?alert=true"

    resp = CyWeatherResponse.from_dict(httpx.get(url).json())
    print(resp.dumps_pretty(indent=4, ensure_ascii=False))
