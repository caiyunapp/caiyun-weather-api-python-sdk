from dataclasses import dataclass

from cyapi.models.alert import cyWeatherAPIResponseAlertStruct
from cyapi.models.hourly import cyWeatherAPIResponseHourlyStruct
from cyapi.models.minutely import cyWeatherAPIResponseMinutelyStruct
from cyapi.models.realtime import cyWeatherAPIResponseRealtimeStruct
from cyapi.models.daily import cyWeatherAPIResponseDailyStruct


@dataclass
class cyWeatherAPIResponseResultStruct:
    primary: int
    forecast_keypoint: str = None
    realtime: cyWeatherAPIResponseRealtimeStruct = None
    minutely: cyWeatherAPIResponseMinutelyStruct = None
    hourly: cyWeatherAPIResponseHourlyStruct = None
    daily: cyWeatherAPIResponseDailyStruct = None
    alert: cyWeatherAPIResponseAlertStruct = None
