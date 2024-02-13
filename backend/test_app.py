import unittest
from flask import Flask
from app import app 
import io

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app
        self.client = self.app.test_client()

    def test_upload_file(self):
        data = {
            'image': (io.BytesIO(b"this is a test"), 'alb_id.jpg')
        }
        response = self.client.post('/upload', data=data, content_type='multipart/form-data')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'alb_id.jpg')

if __name__ == '__main__':
    unittest.main()