import numpy as np
import tensorflow as tf
from tensorflow import keras
from utils import preprocess_text
from keras.preprocessing.sequence import pad_sequences
import pickle

#Import model from saved model
#The model folder should be in root
model = keras.models.load_model('cnn_model1')

#Set max sequence length
MAX_SEQUENCE_LENGTH = 50

#Get the tokenizer from saved pickle file
with open('tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

#Set text to try the model predictions
text = [
    "Partido complicado pero no perdido. Saldremos de esta 💪 Que la fe sea lo ultimo que se pierda 🙌",
    "@manuval68 @Minsa_Peru @Agencia_Andina @noticias_tvperu @RadioNacionalFM @DiarioElPeruano ASI ES!!!!!!!!!!!!!!!!!!!! MALDITAS FUJUIRRAATAAAAAASSSS!!!!!!!!!!!!!!!! #FujimoristasEnemigosDelPeru!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!",
    "@Minsa_Peru @Agencia_Andina @noticias_tvperu @RadioNacionalFM @DiarioElPeruano Cuidence por favor !!!!!!!!! distanciamiento fisico ! ❤️❤️❤️❤️🙏🤍💪 tomen distancia 🥺",
    "@rparrawong @Minsa_Peru Tienen el numero de contagios de hoy y fallecidos por regiones please?? 🙁",
    "Partido complicado pero no perdido. Saldremos de esta 💪 Que la fe sea lo ultimo que se pierda 🙌",
    "El chino es un buen puto, me cae bien",
    "@pcmperu @nlcr5_ @presidenciaperu @PeruPaisDigital @MTC_GobPeru @Minsa_Peru @EsSaludPeru @elcomercio_peru @larepublica_pe @RPPNoticias @canalN_ @exitosape Otra cojudez de este gobierno incompetente"
]

#Process the model
text = [preprocess_text(t) for t in text]
print(text)
text = tokenizer.texts_to_sequences(text)
text = pad_sequences(text, maxlen=MAX_SEQUENCE_LENGTH)

predictions = model.predict(text)
for p in predictions:
    p = [round(num,5) for num in p]
    print(p)