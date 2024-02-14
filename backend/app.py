from flask import Flask, request
from flask_cors import CORS, cross_origin

from keras.preprocessing.image import img_to_array
from keras.models import load_model
import cv2
import numpy as np
import uuid
import csv


app = Flask(__name__)
CORS(app, support_credentials=True)


model = load_model('model/id-classification.h5')


with open('model/class_names.csv', newline='') as csvfile:
    classes = list(csv.reader(csvfile))

def classify_image(img_path):

    image = cv2.imread(img_path)
    image = cv2.resize(image, (64, 64))
    image = image.astype("float") / 255.0
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    res = model.predict(image)

    pred_index = res.argmax(axis=-1)[0]
    return classes[pred_index]

@app.route('/upload', methods=['POST'])
@cross_origin(supports_credentials=True)
def upload_file():    
    print('request.files:', request.files)
    if 'image' not in request.files:
        return 'No image part in the request', 400

    file = request.files['image']
    file_name = f'{uuid.uuid4()}.jpg'
    file.save(f'{file_name}')

    image_class = classify_image(f'{file_name}')

    return image_class, 200

if __name__ == '__main__':
    app.run()