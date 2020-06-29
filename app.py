import os
from flask import Flask, request
from flask_cors import CORS, cross_origin
import json

app = Flask(__name__)
cors = CORS(app, resources={r"/foo": {"origins": "http://localhost:8080"}})
app.config['CORS_HEADERS'] = 'Content-Type'
model = None


@app.route('/hello')
@cross_origin()
def hello():
    return 'Hello from Enzo Lizama, Rodrigo Guadalupe and Camilo Silva!'


@app.route('/sentiment-analysis', methods=['POST'])
@cross_origin()
def predict():
    return {"data": "Gmi2 puto"}


if __name__ == "__main__":
    app.run(host='localhost')