from flask import Flask, request
from flask_cors import CORS, cross_origin
import logging

logging.basicConfig(filename='backend.log', level=logging.INFO)

from keras.preprocessing.image import img_to_array
from keras.models import load_model
import cv2
import numpy as np
import uuid
import csv
import os


app = Flask(__name__)
CORS(app, support_credentials=True)


model = load_model('model/id-classification.h5')


with open('model/class_names.csv', newline='') as csvfile:
    classes = list(csv.reader(csvfile))

def classify_image(img_path):
    app.logger.debug('\n\nprocessing new image')
    image = cv2.imread(img_path)
    image = cv2.resize(image, (256, 256))
    image = image.astype("float") / 255.0
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    res = model.predict(image)[0]
    
    for i in range(0, len(res)):
        app.logger.debug(f'{classes[i]}: {res[0]}')

    app.logger.debug(f'res_argmax: {res.argmax(axis=-1)}')
    pred_index = res.argmax(axis=-1)
    
    return classes[pred_index][0]

@app.route('/upload', methods=['POST'])
@cross_origin(supports_credentials=True)
def upload_file():
    print('request.files:', request.files)
    if 'image' not in request.files:
        app.logger.error('No image part in the request')
        return 'No image part in the request', 400

    file = request.files['image']
    file_name = f'{uuid.uuid4()}.jpg'
    file.save(f'{file_name}')

    image_class = classify_image(f'{file_name}')

    # remove the file after classification
    os.remove(file_name)
    return image_class, 200

if __name__ == '__main__':
    app.run()