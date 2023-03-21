import json
from dataclasses import dataclass
from typing import Literal, Optional

import httpx

from cy_weather_api.models import CyWeatherResponse

API_BASE = (
    "https://api.caiyunapp.com/v2.6/{token}/{lng},{lat}/weather.json?"
    "&lang={lang}"
    "&unit={unit}"
    "&dailysteps={dailysteps}"
    "&hourlysteps={hourlysteps}"
    "&alert={alert}"
)
VALID_UNIT_OPTIONS = Literal["metric", "metric:v1", "metric:v2", "imperial", "SI"]
VALID_GRANU_OPTIONS = Literal["realtime", "minutely", "hourly", "daily", "weather"]


@dataclass
class CyWeatherAPIClient:
    token: str = "TAkhjf8d1nlSlspN"
    http_client = httpx.Client()

    def _make_url(
        self,
        lng: float,
        lat: float,
        lang: Literal["zh_CN", "zh_TW", "ja", "en_GB", "en_US"] = "en_US",
        begin: Optional[int] = None,
        alert: bool = False,
        granu: VALID_GRANU_OPTIONS = None,
        unit: VALID_UNIT_OPTIONS = "metric",
        dailysteps: int = 5,
        hourlysteps: int = 48,
    ) -> str:
        if unit and unit not in VALID_UNIT_OPTIONS.__args__:
            raise ValueError(
                f"Invalid unit, got {unit}, expect one from {VALID_UNIT_OPTIONS.__args__}"
            )

        if granu and granu not in VALID_GRANU_OPTIONS.__args__:
            raise ValueError(
                f"Invalid granu, got {granu}, expect one from {VALID_GRANU_OPTIONS.__args__}"
            )

        if dailysteps < 1 or dailysteps > 15:
            raise ValueError(f"Invalid dailysteps={dailysteps} should in range [1, 15]")

        if hourlysteps < 1 or hourlysteps > 360:
            raise ValueError(
                "Invalid hourlysteps={hourlysteps} should in range [1, 360]"
            )

        url = API_BASE.format(
            token=self.token,
            lng=lng,
            lat=lat,
            lang=lang,
            unit=unit,
            hourlysteps=hourlysteps,
            dailysteps=dailysteps,
            alert=alert,
        )

        if granu:
            url += f"&granu={granu}"

        if begin:
            int(begin)
            url += f"&begin={begin}"

        return url

    def fetch(
        self,
        lng: float,
        lat: float,
        lang: Literal["zh_CN", "zh_TW", "ja", "en_GB", "en_US"] = "en_US",
        begin: Optional[int] = None,
        alert: bool = False,
        granu: VALID_GRANU_OPTIONS = None,
        unit: VALID_UNIT_OPTIONS = "metric",
        dailysteps: int = 5,
        hourlysteps: int = 48,
    ) -> CyWeatherResponse:
        url = self._make_url(
            lng,
            lat,
            lang=lang,
            begin=begin,
            alert=alert,
            granu=granu,
            unit=unit,
            dailysteps=dailysteps,
            hourlysteps=hourlysteps,
        )
        resp = self.http_client.get(url)
        status_code = resp.status_code

        if status_code == httpx.codes.OK:
            return CyWeatherResponse.from_dict(resp.json())

        http_name = httpx.codes(status_code).name
        headers = json.dumps(dict(resp.headers), indent=4)
        raise ValueError(
            (
                f"Calling API failed: HTTP {status_code} {http_name}\n\n"
                f"- url: {url}\n"
                f"- raw: {resp.text}\n"
                f"- header: {headers}\n"
            )
        )


if __name__ == "__main__":
    client = CyWeatherAPIClient(token="TAkhjf8d1nlSlspN")

    api_result = client.fetch(lng=101.8551, lat=26.6832, lang="zh_CN", alert=True)
    print(api_result.result.hourly.description)

    api_result = client.fetch(lng=-0.2008, lat=51.5024, lang="en_GB")
    print(api_result.result.hourly.description)

    api_result = client.fetch(lng=73.9808, lat=40.7648, lang="en_US")
    print(api_result.result.hourly.description)
