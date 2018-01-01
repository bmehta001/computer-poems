import string
import nltk
from bs4 import BeautifulSoup
import urllib.request
import spacy
from random import *
import re
import enchant
import random

englishwords = enchant.Dict("en_US")

titlelist = []
bagofwords = set()
resp = urllib.request.urlopen("http://www.imdb.com/chart/top")
soup = BeautifulSoup(resp,"html.parser")
for heading in soup.findAll("td", {"class": "titleColumn"}):
  title = str(heading).split()
  words = title[12].replace("</a>", "").replace("<span>", "").replace(">", "")
  if englishwords.check(words):
    bagofwords.add(words)
  words = title[11].replace("</a>", "").replace("<span>", "").replace(">", "")
  if englishwords.check(words):
    bagofwords.add(words)
  words = title[13].replace("</a>", "").replace("<span>", "").replace(">", "")
  if englishwords.check(words):
    bagofwords.add(words)  

for j in range(6):
    poem = random.sample(bagofwords,1)
    print(str(poem).replace("['", "").replace("']", "") + " ", end="")


