import string
import nltk
from bs4 import BeautifulSoup
import urllib.request
import spacy
from random import *

nlp = spacy.load('en')
head = {}
titlelist = []
resp = urllib.request.urlopen("https://www.nytimes.com/")
soup = BeautifulSoup(resp,"html.parser")
for heading in soup.find_all("h3", class_= "story-heading"):
    title = heading.string.strip()
    titlelist.extend([title])


word1 = []
word2 = []
word3 = []
word4 = []
word5 = []
word6 = []

for i in range(len(titlelist)):
    doc = nlp(titlelist[i])
    nsubj = [tok for tok in doc if (tok.dep_ == "prep")]
    aux = [tok for tok in doc if (tok.pos_ == "NOUN")]
    root = [tok for tok in doc if (tok.pos_ == "ADJ")]
    prep = [tok for tok in doc if (tok.pos_ == "NOUN")]
    pcomp = [tok for tok in doc if (tok.pos_ == "ADV")]
    dobj = [tok for tok in doc if (tok.pos_ == "VERB")]
    word1.extend(nsubj)
    word2.extend(aux)
    word3.extend(root)
    word4.extend(prep)
    word5.extend(pcomp)
    word6.extend(dobj)




num1 = str(sample(word1,  1)).replace("[", "").replace("]", "")
num2 = str(sample(word2,  1)).replace("[", "").replace("]", "")
num3 = str(sample(word3,  1)).replace("[", "").replace("]", "")
num4 = str(sample(word4,  1)).replace("[", "").replace("]", "")
num5 = str(sample(word5,  1)).replace("[", "").replace("]", "")
num6 = str(sample(word6,  1)).replace("[", "").replace("]", "")

print(num1, num2, num3, num4, num5, num6)
