import string
import nltk
from bs4 import BeautifulSoup
import urllib.request
import spacy
import random

nlp = spacy.load('en')
paragraph = []
resp = urllib.request.urlopen("http://www.sacred-texts.com/hin/av/av10010.htm")
soup = BeautifulSoup(resp,"html.parser")
for text in soup.find_all('span'):
  paragraph.append(text.next_sibling)


word1 = []
word2 = []
word3 = []
word4 = []
word5 = []
word6 = []
word7 = []

for i in range(len(paragraph)):
    doc = nlp(str(paragraph[i]))
    nsubj = [str(tok).replace("[", "").replace("]", "") for tok in doc if (tok.dep_ == "nsubj")]
    root = [str(tok).replace("[", "").replace("]", "") for tok in doc if (tok.dep_ == "ROOT")]
    det = [str(tok).replace("[", "").replace("]", "") for tok in doc if (tok.dep_ == "det")]
    dobj = [str(tok).replace("[", "").replace("]", "") for tok in doc if (tok.dep_ == "dobj")]
    prep = [str(tok).replace("[", "").replace("]", "") for tok in doc if (tok.dep_ == "prep")]
    pobj = [str(tok).replace("[", "").replace("]", "") for tok in doc if (tok.dep_ == "pobj")]
    punct = [str(tok).replace("[", "").replace("]", "") for tok in doc if (tok.dep_ == "punct")]
    word1.extend(nsubj)
    word2.extend(root)
    word3.extend(det)
    word4.extend(dobj)
    word5.extend(prep)
    word6.extend(pobj)
    word7.extend(punct)

word1= set(word1)
word2 = set(word2)
word3 = set(word3)
word4 = set(word4)
word5 = set(word5)
word6 = set(word6)
word7 = set(word7)

poem1 = random.sample(word1,1)
poem1 = str(poem1).replace("'", "").replace("'", "").replace("[", "").replace("]", "") + " "

poem2 = random.sample(word2,1)
poem2 = str(poem2).replace("'", "").replace("'", "").replace("[", "").replace("]", "") + " "

poem3 = random.sample(word3,1)
poem3 = str(poem3).replace("'", "").replace("'", "").replace("[", "").replace("]", "") + " "

poem4 = random.sample(word4,1)
poem4 = str(poem4).replace("'", "").replace("'", "").replace("[", "").replace("]", "")+ " "

poem5 = random.sample(word5,1)
poem5 = str(poem5).replace("'", "").replace("'", "").replace("[", "").replace("]", "")+ " "

poem6 = random.sample(word6,1)
poem6 = str(poem6).replace("'", "").replace("'", "").replace("[", "").replace("]", "")

poem7 = random.sample(word7,1)
poem7 = str(poem7).replace("'", "").replace("'", "").replace("[", "").replace("]", "")+ " "

print(poem1, poem2, poem3, poem4, poem5, poem6, poem7, poem3, poem4, poem5, poem6, poem7, poem1, poem2)


