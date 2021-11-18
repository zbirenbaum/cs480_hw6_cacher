import pickle
import numpy as np
import os

def load_model(model="lg"):
    import spacy
    nlp = spacy.load("en_core_web_"+model)
    return nlp    

def build_W(model="lg"):
    nlp = load_model(model)
    W = []
    words = []
    strings = set([w.lower().strip() for w in nlp.vocab.strings])
    for word in strings:
        vector = nlp.vocab[word].vector
        if np.fabs(vector).sum() > 0: #type: ignore
            words.append(word)
            W.append(vector)
    return W

def word_loader(model="lg", cachedir="./cache/"):
    cache = cachedir+model
    with open(cache, "rb") as fp:
        W = pickle.load(fp)
    return W

def word_writer(W, model="lg", cachedir="./cache/"):
    if not os.path.isdir(cachedir):
        os.mkdir(cachedir)
    cache = cachedir+model
    with open(cache, "wb") as fp:
        pickle.dump(W, fp, protocol=-1)
    return

