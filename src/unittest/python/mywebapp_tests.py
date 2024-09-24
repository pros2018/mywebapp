import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../main/python')))
from mywebapp import app

class TestMyWebApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_hello_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'Hello, welcome to my simple web application')
    # Negative test case for a non-existent route
    def test_404(self):
        # Simulate a request to a non-existent URL
        response = self.app.get('/non-existent-route')
        # Assert that the response status code is 404 (Not Found)
        self.assertEqual(response.status_code, 404)

    # Negative test case for a wrong HTTP method
    def test_invalid_method(self):
        # Simulate a POST request to the root URL (which only accepts GET)
        response = self.app.post('/')
        # Assert that the response status code is 405 (Method Not Allowed)
        self.assertEqual(response.status_code, 405)

if __name__ == '__main__':
    unittest.main()
