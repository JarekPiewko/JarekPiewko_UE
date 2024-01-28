from flask import Flask
from flask_restful import Resource, Api
import cv2
import numpy as np
from urllib.request import urlopen
import imghdr

app = Flask(__name__)
api = Api(app)

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
image_path = r"C:\Users\jarek\OneDrive\Pulpit\fotka.jpg"
class PeopleCounter(Resource):
    def get(self):
        img = cv2.imread(image_path)
        boxes, weights = hog.detectMultiScale(img, winStride=(1, 1))

        return {'count': len(boxes)}

class PeopleCounterOnline(Resource):
    def get(self):
        online_image_url = 'https://rzeszow-news.pl/wp-content/uploads/sites/1/nggallery/prezentacja-dworzec-pks-pazdziernik-2021/pks-03-wiz-1920x1080.jpg'
        response = urlopen(online_image_url)
        image_array = np.asarray(bytearray(response.read()), dtype=np.uint8)
        img = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
        if img is not None:
            boxes, weights = hog.detectMultiScale(img, winStride=(1, 1))
            return {'count': len(boxes)}
        else:
            return {'error': 'Failed to decode image'}, 500

class PeopleCounterPost(Resource):

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


api.add_resource(PeopleCounter, '/')
api.add_resource(HelloWorld, '/test')
api.add_resource(PeopleCounterOnline, '/test2')
api.add_resource(PeopleCounterPost, '/test3')

if __name__ == '__main__':
    app.run(debug=True)