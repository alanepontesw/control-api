import unittest
from domain.request import Request

class TestControlAPI(unittest.TestCase):
    def setUp(self):
        self.request = Request(method='POST', body=[{'id': '123', 'name': 'mesa'}])

    def test_hashify(self):
        desordened_request = Request(method='POST', body=[{'name': 'mesa', 'id': '123'}])
        self.assertEqual(self.request.hashify(), desordened_request.hashify())

if __name__ == '__main__':
    unittest.main()
