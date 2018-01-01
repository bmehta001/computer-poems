import pronouncing
import random


animals = ["cat", "dog", "alligator", "babboon", "cow", "rabbit", "pig", "horse", "ant", "deer", "fox", "goat", "sheep", "bear"]
animals = set(animals)
actions = ["watch", "read", "write", "draw", "cry", "laugh", "sleep", "eat", "knit", "whine", "talk", "run", "cook", "bite"]
actions = set(actions)

try:
  word1 = str(random.sample(animals,1)).replace("[", "").replace("]", "").replace("'", "").replace("'", "")
  word2 = str(random.sample(actions,1)).replace("[", "").replace("]", "").replace("'", "").replace("'", "")
  word3 = str(random.sample(pronouncing.rhymes(word1), 1)).replace("'", "").replace("'", "").replace("[", "").replace("]", "")
  word4 = str(random.sample(pronouncing.rhymes(word2), 1)).replace("'", "").replace("'", "").replace("[", "").replace("]", "")
  print("If I were a "   + word1 + ", I would love to " + word2 + ".")
  print("Look, there's a " + word3 + ", let us " + word4 + ".")
except:
  pass
