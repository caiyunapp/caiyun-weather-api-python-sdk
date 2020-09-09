from dataclasses import dataclass

from cy_weather_api.models.alert import cyWeatherAPIResponseAlertStruct
from cy_weather_api.models.daily import cyWeatherAPIResponseDailyStruct
from cy_weather_api.models.hourly import cyWeatherAPIResponseHourlyStruct
from cy_weather_api.models.minutely import cyWeatherAPIResponseMinutelyStruct
from cy_weather_api.models.realtime import cyWeatherAPIResponseRealtimeStruct


@dataclass
class cyWeatherAPIResponseResultStruct:
    primary: int
    forecast_keypoint: str = None
    realtime: cyWeatherAPIResponseRealtimeStruct = None
    minutely: cyWeatherAPIResponseMinutelyStruct = None
    hourly: cyWeatherAPIResponseHourlyStruct = None
    daily: cyWeatherAPIResponseDailyStruct = None
    alert: cyWeatherAPIResponseAlertStruct = None
