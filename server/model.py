import numpy as np
import tensorflow as tf
from tensorflow import keras
from server.get_twitter_data import get_tweets
from server.utils import preprocess_text
from keras.preprocessing.sequence import pad_sequences
import pickle
import pandas as pd

class Model:

    def __init__(self):

        #Import model from saved model
        #The model folder should be in root
        self.model = keras.models.load_model('cnn_model3')

        #Set max sequence length
        self.MAX_SEQUENCE_LENGTH = 50

        #Get the tokenizer from saved pickle file
        with open('tokenizer3.pickle', 'rb') as handle:
            tokenizer = pickle.load(handle)

        self.tokenizer = tokenizer
        self.raw_texts = None
        self.texts = None

    def get_data(self, amount):
        get_tweets(amount)
        dataframe = pd.read_csv('data.csv', encoding='utf-8')

        dataframe['text'] = dataframe['text'].apply(lambda x: str(x))
        self.raw_texts = dataframe['text'].tolist()

        dataframe['text'] = dataframe['text'].apply(lambda x: preprocess_text(x))
        self.texts = dataframe['text'].tolist()

    def get_predictions(self):

        data = self.tokenizer.texts_to_sequences(self.texts)
        data = pad_sequences(data, maxlen=self.MAX_SEQUENCE_LENGTH)

        predictions = self.model.predict(data)
        for index, p in enumerate(predictions):
            predictions[index] = [round(num,3) for num in p]
        
        return predictions

        
