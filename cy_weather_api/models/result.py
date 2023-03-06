from dataclasses import dataclass
from typing import Optional

from cy_weather_api.models.alert import cyWeatherAPIResponseAlertStruct
from cy_weather_api.models.daily import cyWeatherAPIResponseDailyStruct
from cy_weather_api.models.hourly import cyWeatherAPIResponseHourlyStruct
from cy_weather_api.models.minutely import cyWeatherAPIResponseMinutelyStruct
from cy_weather_api.models.realtime import cyWeatherAPIResponseRealtimeStruct


@dataclass
class cyWeatherAPIResponseResultStruct:
    primary: int
    forecast_keypoint: Optional[str] = None
    realtime: Optional[cyWeatherAPIResponseRealtimeStruct] = None
    minutely: Optional[cyWeatherAPIResponseMinutelyStruct] = None
    hourly: Optional[cyWeatherAPIResponseHourlyStruct] = None
    daily: Optional[cyWeatherAPIResponseDailyStruct] = None
    alert: Optional[cyWeatherAPIResponseAlertStruct] = None
