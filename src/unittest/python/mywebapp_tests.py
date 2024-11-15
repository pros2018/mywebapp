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
    def test_get_data_route(self):
        response = self.app.get('/api/data')
        self.assertEqual(response.status_code, 200)
        self.assertIn('message', response.get_json())

    def test_post_data_route(self):
        response = self.app.post('/api/data', json={'name': 'Alice'})
        self.assertEqual(response.status_code, 201)
        self.assertIn('message', response.get_json())

    def test_post_data_invalid(self):
        response = self.app.post('/api/data', json={})
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.get_json())
if __name__ == '__main__':
    unittest.main()
