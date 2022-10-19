# from crypt import methods
# import cv2 as cv
# from PIL import Image
# import os
# from werkzeug.utils import secure_filename

import math
from flask import Flask, request, jsonify
import numpy as np

app = Flask(__name__)

app.secret_key = "My-BuraphaInformatics"


@app.route('/')
def main():
    return 'formalinapp_api works !'

@app.route('/hello')
def hello_world():
    return 'We love . .....'

myarea = []
@app.route('/radius', methods=["POST", "GET"])
def calradius():
    if request.method == 'POST':
        body = request.get_json()
        radius = body['radius']
        area = (22/7)*(radius**2)
        myarea.append(area)
        return {'Message': 'Radius already add into database', 'area': myarea}, 201
        
    elif request.method == 'GET':
        return {'radius': myarea}, 200

books = []
@app.route('/book', methods=['POST', 'GET', 'PUT', 'DELETE'])
def book():

    if request.method == 'POST':
        body = request.get_json()
        books.append(body)
        return {'Message': "Book already add to database", 'body': body}, 201

    elif request.method == 'GET':
        return {'books': books}, 200

    elif request.method == 'PUT':
        body = request.get_json()
        for i, book in enumerate(books):
            if book[i]['id'] == body[i]['index']:
                books[i] = body
        return {"message": "Book has been replace", "body": body}, 200

    elif request.method == 'DELETE':
        body = request.get_json()
        books[0].pop(body['index'])
        return {"message": "Book is deleted",
                'book': body['index'],
                'books': books[0]}, 200


if __name__ == '__main__':
    app.run(debug=True)
