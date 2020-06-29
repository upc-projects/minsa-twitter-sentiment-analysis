import os
from flask import Flask, request
from flask_cors import CORS, cross_origin
import json
import time

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
    post_data = request.data.decode("utf-8")
    data = json.loads(post_data)
    time.sleep(5)
    # number_tweets
    return {
        "mean_text":
        "Negativo",
        "mean":
        -1,
        "details": [{
            "text": "Gmi2 puto",
            "accuracy": 52.1,
            "result": "negativo",
        }, {
            "text": "Andrecito cagon",
            "accuracy": 82.1,
            "result": "negativo"
        }, {
            "text": "Miguleito xd",
            "accuracy": 92.1,
            "result": "neutro"
        }]
    }


if __name__ == "__main__":
    app.run(host='localhost')