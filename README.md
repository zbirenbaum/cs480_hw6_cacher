# How To Use

## 1: Download word_cacher.py

### cd to the directory which contains your HW6 in a terminal (or powershell for Windows) and then run the following code in your shell:
```
curl -o word_cacher.py https://raw.githubusercontent.com/zbirenbaum/cs480_hw6_cacher/main/word_cacher.py
```
### Alternatively, skip the cd step and just run curl with this format
```
curl -o /path/to/hw6_dir/word_cacher.py https://raw.githubusercontent.com/zbirenbaum/cs480_hw6_cacher/main/word_cacher.py
```

## 2: Integrate in your code

### 1: Delete the Following Code 
```
nlp = spacy.load("en_core_web_lg")
W = []
words = []
strings = set([w.lower().strip() for w in nlp.vocab.strings])
for word in strings:
  vector = nlp.vocab[word].vector
  if np.fabs(vector).sum() > 0:
    words.append(word)
    W.append(vector)
```
### 2: Replace the Deleted Code with the Following:
```

def get_words():
    from word_cacher import build_W, word_loader, word_writer
    try:
        words = word_loader("words.dat")
        W = word_loader("W.dat")
        nlp = spacy.load("en_core_web_lg")
    except: 
        W, words, nlp = build_W()
        word_writer(words, model="words.dat")
        word_writer(W, model="W.dat")
    return W, words, nlp
```   
The first time the code runs it will likely take a very long time and you will not notice any change. Once it runs once, the cache will be generated, and all subsequent runs you can enjoy your sub second runtimes.

## Before & After
<img src="https://github.com/zbirenbaum/cs480_hw6_cacher/blob/main/comparison.png">
