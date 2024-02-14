import unittest
from flask import Flask
from app import app 
import io
from werkzeug.datastructures import FileStorage

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app
        self.client = self.app.test_client()

    def test_upload_file(self):
        #read file from  tst_data/alb_id.jpg
        file = FileStorage(
            stream=open("test_data/alb_id.jpg", "rb"),
            filename="alb_id.jpg",
            content_type="image/jpg",
        )
        data = {
            'image': file
        }

        response = self.client.post('/upload', data=data, content_type='multipart/form-data')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'alb_id')

if __name__ == '__main__':
    unittest.main()