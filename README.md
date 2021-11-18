# How To Use
## Optional:
Importing Spacy can cause >1 second delays between runs as it initializes CUDA. I am not sure if this is true on all systems but it is for mine.
As this is the case, unless you utilize methods or classes from spacy in your implementation OUTSIDE of importing the model which is done here, I strongly recommend taking out your spacy import statement at the top of your code. The file contained here imports spacy only when creating the cache, not loading it, resulting in a >50% speedup. (1.4 second full run (with caching) vs .6 second full run)
If you do use spacy elsewhere, feel free to disregard this

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
def get_W():
    from word_cacher import build_W, word_loader, word_writer
    try:
        W = word_loader()
    except: 
        W = build_W()
        word_writer(W)
    return W
W=get_W()
```   
The first time the code runs it will likely take a very long time and you will not notice any change. Once it runs once, the cache will be generated, and all subsequent runs you can enjoy your sub second runtimes.

## Before & After
<img src="https://github.com/zbirenbaum/cs480_hw6_cacher/blob/main/comparison.png">
