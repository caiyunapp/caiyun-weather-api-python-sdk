from dataclasses import dataclass
from typing import Optional, Literal

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

        resp = self.http_client.get(url)
        resp_status = resp.status_code

        if resp_status == 200:
            return CyWeatherResponse.from_dict(resp.json())

        raise ValueError(
            (
                f"Calling API failed(HTTP {resp_status})`, please check token status\n\n"
                f"- url: {url}\n"
                f"- raw: {resp.text}\n"
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
