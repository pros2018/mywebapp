import unittest
from mywebapp import app

class TestMyWebApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_hello_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'Hello, welcome to my simple web application!')

if __name__ == '__main__':
    unittest.main()
