import unittest
from domain.control_api import ControlAPI
from domain.request import Request
from infrastructure.database.redis_client import RedisClient

# TODO: Improve test coverage
class TestControlAPI(unittest.TestCase):

    def mock_set(self, key, value, ex=None):
        self.data[key] = value
        self.data[ex] = ex

    def mock_get(self, key):
        return self.data.get(key, None)

    def setUp(self):
        self.data = {}
        self.redis = RedisClient()
        self.control_api = ControlAPI(self.redis)
        self.request = Request(method='POST', body=[{'id': '123', 'name': 'mesa'}])

    def test_request_is_denied(self):
        self.redis.get = self.mock_get
        self.redis.set = self.mock_set

        self.assertEqual(self.control_api.request_is_denied(self.request), False)
        self.assertEqual(self.control_api.request_is_denied(self.request), True)
        self.assertEqual(self.control_api.request_is_denied(self.request), True)

if __name__ == '__main__':
    unittest.main()
