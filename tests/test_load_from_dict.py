import json
import unittest
from unittest import TestCase

from cy_weather_api import CyWeatherResponse


class TestSDK(TestCase):
    def test_init_from_dict(self):
        with open("tests/data/sample1.json") as f:
            data = json.loads(f.read())
        item = CyWeatherResponse.from_dict(data)
        self.assertEqual(item.status, "ok")


if __name__ == "__main__":
    unittest.main()
