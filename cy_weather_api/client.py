from dataclasses import dataclass

import requests

from cy_weather_api.models import CyWeatherAPIResponseHandler, initFromDict

API_BASE = (
    "http://api.caiyunapp.com/v2.5/{token}/{lng},{lat}/weather.json?"
    "&lang={lang}"
    "&unit={unit}"
    "&dailysteps={dailysteps}"
    "&hourlysteps={hourlysteps}"
)
VALID_UNIT_OPTIONS = ["metric", "metric:v1", "metric:v2", "imperial", "SI"]
VALID_GRANU_OPTIONS = ["realtime", "minutely", "hourly", "daily", "weather"]


@dataclass
class CyWeatherAPIClient:
    token: str = "TAkhjf8d1nlSlspN"
    session = requests.Session()

    def fetch(
        self,
        lng: float,
        lat: float,
        lang: str = "en_US",
        begin: int = None,
        alert: bool = False,
        granu: str = None,
        unit: str = "metric",
        dailysteps: int = 5,
        hourlysteps: int = 48,
    ) -> CyWeatherAPIResponseHandler:

        if unit and unit not in VALID_UNIT_OPTIONS:
            raise ValueError(
                "Invaliad unit, got  {}, expect one from {}".format(
                    unit, VALID_UNIT_OPTIONS
                )
            )

        if granu and granu not in VALID_GRANU_OPTIONS:
            raise ValueError(
                "Invaliad granu, got  {}, expect one from {}".format(
                    unit, VALID_GRANU_OPTIONS
                )
            )

        if dailysteps < 1 or dailysteps > 15:
            raise ValueError("dailysteps in range [1, 15]")

        if hourlysteps < 1 or hourlysteps > 360:
            raise ValueError("hourlysteps in range [1, 360]")

        url = API_BASE.format(
            token=self.token,
            lng=lng,
            lat=lat,
            lang=lang,
            unit=unit,
            hourlysteps=hourlysteps,
            dailysteps=dailysteps,
        )

        if granu:
            url += "&granu={}".format(granu)

        if begin is not None:
            try:
                int(begin)
                url += "&begin={}".format(begin)
            except Exception:
                raise ValueError("Invalid begin")

        _data = self.session.get(url).json()
        if _data["status"] != "ok":
            _mess = (
                "Calling Caiyun API Errored with {error_mess}, please check token status\n"
                "url: {url}\n"
                "data: {api_data}\n"
            )
            mess = _mess.format(url=url, api_data=_data, error_mess=_data.get("error"))
            raise ValueError(mess)
        return initFromDict(_data)


if __name__ == "__main__":
    client = CyWeatherAPIClient(token="TAkhjf8d1nlSlspN")
    apiResult = client.fetch(lng=101.8551, lat=26.6832, lang="zh_CN", alert=True)
    print(apiResult.result.hourly.description)
    apiResult = client.fetch(lng=-0.2008, lat=51.5024, lang="en_GB")
    print(apiResult.result.hourly.description)
    apiResult = client.fetch(lng=73.9808, lat=40.7648, lang="en_US")
    print(apiResult.result.hourly.description)
