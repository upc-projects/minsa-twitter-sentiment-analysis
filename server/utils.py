import re
import unidecode

def preprocess_text(sen):
    '''
    Method to delete not necessary characters and words
    '''
    #Remove @ words
    sen = ' '.join(word for word in sen.split(' ') if not word.startswith('@'))
    
    # Removing html tags
    sentence = remove_tags(sen)

    # Remove punctuations and numbers
    sentence = re.sub('[^a-zA-Záéíóúñ]', ' ', sentence)

    # Single character removal
    sentence = re.sub(r"\s+[a-zA-Z]\s+", ' ', sentence)

    # Removing multiple spaces
    sentence = re.sub(r'\s+', ' ', sentence)

    return sentence


TAG_RE = re.compile(r'<[^>]+>')

def remove_tags(text):
    '''
    Method to remove all html tags
    '''
    return TAG_RE.sub('', text)

def remove_stopwords(tokens, stoplist): 
    '''
    Remove all the stopwords from tokens using a stopwords list
    '''
    return [word for word in tokens if word not in stoplist]

def lower_token(tokens): 
    '''
    Put all tokens into lowercase
    '''
    return [w.lower() for w in tokens]  