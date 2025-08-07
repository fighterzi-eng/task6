

import random


f =open("words.txt","r")
words=[]


for line in f:


    words.append(line)

def word_selector():
    x=random.choice(words)
    return x

    




