from word_ladder import WordLadder

w1 = WordLadder('vocabulary.txt')
w2 = w1.find_path('FELL', 'HOPE')

try:
    for i in w2:
        print (i.lower())
except:
    pass
