import os
from flask import Flask, request
from flask_cors import CORS, cross_origin
from server.model import Model
import json
import time
import operator

app = Flask(__name__)
cors = CORS(app, resources={r"/foo": {"origins": "http://localhost:8080"}})
app.config['CORS_HEADERS'] = 'Content-Type'
model = None


def get_label(index):
    return 'Positivo' if index == 0 else (
        'Neutro' if index == 1 else 'Negativo')


def get_index(label):
    return 1 if label == 'Positivo' else (0 if label == 'Neutro' else -1)

@app.route('/hello')
@cross_origin()
def hello():
    return 'Hello from Enzo Lizama, Rodrigo Guadalupe and Camilo Silva!'


@app.route('/sentiment-analysis', methods=['POST'])
@cross_origin()
def predict():
    post_data = request.data.decode("utf-8")
    data = json.loads(post_data)
    ntweets = int(data['number_tweets'])
    model.get_data(ntweets)
    predictions = model.get_predictions()

    global_values = {'Positivo': 0, 'Negativo': 0, 'Neutro': 0}

    details = []

    for index, text in enumerate(model.raw_texts):
        dic = {}
        values = list(predictions[index])
        label = get_label(values.index(max(values)))
        dic['text'] = text
        dic['accuracy'] = str(round(max(values) * 100, 2)) + "%"
        dic['result'] = label

        global_values[label] += 1

        details.append(dic)

    max_label = max(global_values.items(), key=operator.itemgetter(1))[0]
    mean = get_index(max_label)

    res = {"mean_text": max_label, "mean": mean, "details": details}

    # number_tweets
    return res
    '''
     {
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
    '''


if __name__ == "__main__":
    model = Model()
    app.run(host='localhost')