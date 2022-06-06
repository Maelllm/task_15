from unittest import TestCase
from unittest.mock import patch, MagicMock

from task_15.task.stas_task_1_hw_15 import city_weather


class TestWeather(TestCase):

    @patch("task_15.task.stas_task_1_hw_15.requests")  # Decorate our test to mock it
    def test_city_weather(self, mock_requests):  # Mock object must be passed as an argument
        requests_responce_mock = MagicMock()  # Init mock object for method

        requests_responce_mock.json.return_value = {'coord': {'lon': -0.1257, 'lat': 51.5085},
                                                    'weather': [
                                                        {'id': 803, 'main': 'Clouds', 'description': 'broken clouds',
                                                         'icon': '04d'}], 'base': 'stations',
                                                    'main': {'temp': 287.41, 'feels_like': 289.15, 'temp_min': 287.64,
                                                             'temp_max': 290.37, 'pressure': 1015,
                                                             'humidity': 79}, 'visibility': 10000,
                                                    'wind': {'speed': 4.12, 'deg': 240}, 'clouds': {'all': 75},
                                                    'dt': 1654540876,
                                                    'sys': {'type': 2, 'id': 2019646, 'country': 'GB',
                                                            'sunrise': 1654487151, 'sunset': 1654546365},
                                                    'timezone': 3600, 'id': 2643743, 'name': 'London', 'cod': 200}
        # Setup a predicted value from responce by changing result of responce.json, was used London weather as example
        mock_requests.get.return_value = requests_responce_mock  # Setup result from reguests.get with our mock object
        assert city_weather(city_name='Kiev') == ('14', '1015')  # And here real weather of city doesn't matter


if __name__ == '__main__':
    main()
