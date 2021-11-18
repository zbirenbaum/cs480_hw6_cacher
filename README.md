#How To Use
Download w_loader.py and place this code somewhere in your hw6.py
```
def get_W():
    from words import build_W, word_loader, word_writer
    try:
        W = word_loader()
    except: 
        W = build_W()
        word_writer(W)
    return W
```   
