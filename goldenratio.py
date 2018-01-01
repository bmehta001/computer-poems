
goldpart1 = "1."
goldpart2 = "618033988749894848204586834365638117720309179805762862135448622705260462818902449707207204189391137"

gold1 = [goldpart1[i:i+1] for i in range(0, len(goldpart1))]
gold2 = [goldpart2[i:i+1] for i in range(0, len(goldpart2))]


dicty = {"0": "time", "1": "perfect", ".": "? ", "2": "love", "3": "life", "5": "art", "6": "beauty", "8": "long", "9": "i"}

for i in gold1:
  print(dicty[i], end = "")

print(" ")

for i in gold2:
  if i!= "7" and i!="4":
    print(dicty[i] + " ", end="")
  else:
    print(" ")
