# Caiyun Weather API Python SDK

> **NOTE**: This project is not officially supported by ColorfulClouds
> Technology.
>
> It's open sourced under MIT License and designed as a debug tool for our
> internal systems instead of online services, or third party technology
> support.

## Install

Python 3.8.1+ is required.

```sh
pip install cy-weather-api
```

## Usage

### Request Caiyun API

**NOTE: `TAkhjf8d1nlSlspN` is test token, no one can ensure its availability.**

```python
from cy_weather_api import CyWeatherAPIClient

client = CyWeatherAPIClient(token="TAkhjf8d1nlSlspN")

api_result = client.fetch(lng=101.8551, lat=26.6832, lang="zh_CN", alert=True)
print(api_result.result.hourly.description)

api_result = client.fetch(lng=-0.2008, lat=51.5024, lang="en_GB")
print(api_result.result.hourly.description)

api_result = client.fetch(lng=73.9808, lat=40.7648, lang="en_US")
print(api_result.result.hourly.description)
```

Output sample:

```
晴，今天晚间20点钟后转小雨，其后多云
clear weather over the next 24 hours
clear weather, overcast after 20 o'clock this afternoon, followed by cloudy
```

### Use our dataclass models

The default HTTP client is httpx, you can use other HTTP client to request API,
and pass the response dict to our models (based on `dataclass`):

```py
from cy_weather_api import CyWeatherResponse

data = {
    "status": "ok",
    "api_version": "v2.6",
    "api_status": "active",
    "lang": "en_US",
    "unit": "metric",
    "tzshift": 28800,
    "timezone": "Asia/Shanghai",
    "server_time": 1589125757,
    "location": [39.888888, 116.674501],
    "result": {"forecast_keypoint": "test forecast_keypoint", "primary": 0},
}
result = CyWeatherResponse.from_dict(data)
```
