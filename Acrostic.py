import nltk
import markovify
import json
import syllables
import re
import spacy


def poem():

  nlp = spacy.load("en")

  text = "" 
  with open("Turing.txt", "r", encoding="utf-8") as f:
    read = f.read().splitlines()
    for row in read:
        text+=row

  text_model = markovify.Text(text)


  a, c, d, f = 'x', 'x', 'x', 'x'
  while(a != "B"):
    one = text_model.make_short_sentence(50)
    if one != None:
      a = list(one)[0]
  while(c[0] != "I"):
    two = text_model.make_short_sentence(50)
    if two != None:
      c = list(two)[0]
  while(d!= "T"):
    three = text_model.make_short_sentence(50)
    if three != None:
      d = list(three)[0]
  while(f != "S"):
    four = text_model.make_short_sentence(50)
    if four !=None:
      f = list(four)[0]

  one = list(one)
  one.insert(2, " ")
  one = "".join(one)
  try:
    print(one.replace(".", "").replace("?","").replace("!", ""))
    print(two.replace(".", "").replace("?","").replace("!", ""))
    print(three.replace(".", "").replace("?","").replace("!", ""))
    print(four.replace(".", "").replace("?","").replace("!", ""))
    print(five.replace(".", "").replace("?","").replace("!", ""))

  except:
    pass



