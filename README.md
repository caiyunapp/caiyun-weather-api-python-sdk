# Caiyun Weather API Python SDK

## Install

Python 3.6+ is required.

```sh
pip install cy-weather-api
```

## Usage

### Request Caiyun API

```py
from cy_weather_api import CyWeatherAPIClient

client = CyWeatherAPIClient(token="TAkhjf8d1nlSlspN")
apiResult = client.fetch(lng=101.8551, lat=26.6832, lang="zh_CN", alert=True)
print(apiResult.result.hourly.description)
apiResult = client.fetch(lng=-0.2008, lat=51.5024, lang="en_GB")
print(apiResult.result.hourly.description)
apiResult = client.fetch(lng=73.9808, lat=40.7648, lang="en_US")
print(apiResult.result.hourly.description)
```

Output sample:

```
晴，今天晚间20点钟后转小雨，其后多云
clear weather over the next 24 hours
clear weather, overcast after 20 o'clock this afternoon, followed by cloudy
```

### Use our dataclass models

The default HTTP client is requests, you can other HTTP cient to request API,
and pass the response dict to our models (based on `dataclasss`):

```py
from cy_weather_api import initFromDict

data = {
    "status": "ok",
    "api_version": "v2.5",
    "api_status": "active",
    "lang": "en_US",
    "unit": "metric",
    "tzshift": 28800,
    "timezone": "Asia/Shanghai",
    "server_time": 1589125757,
    "location": [39.888888, 116.674501],
    "result": {"forecast_keypoint": "test forecast_keypoint", "primary": 0},
}
apiResult = initFromDict(data)
```
