# yumshatish va ayirish belsini chiqarib tashlanadi
# 27 ta harf
from nltk import ngrams
from itertools import combinations
import operator

letters = ['а', 'b', 'd', 'е', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'о', 'p', 'q', 'r', 's', 't',
           'u', 'v', 'x', 'y', 'ḡ', 'ō', 'c']  # 'ş', 'ç'

cubics = []
for i in combinations(letters, 6):
    cubics.append(i)
print(len(cubics))

k = 0
for i in combinations(cubics, 8):
    print(i)
    k += 1
    if k == 1:
        break;
print(k)
freq = {}
words = []
with open("words", encoding="utf8") as file:
    lines = file.readlines()
words = [line.rstrip() for line in lines]

for word in words:
    bigrams = ngrams(word, 2)

    for grams in bigrams:
        print(grams[0]+grams[1])
        key = grams[0]+grams[1]
        if key in freq:
            freq[key] += 1
        else:
            freq[key] = 1
s_freq = dict( sorted(freq.items(), key=operator.itemgetter(1), reverse=True))
print(s_freq)

cubics = []
with open("cubics", encoding="utf8") as file:
    lines = file.readlines()
    cubics = [line.rstrip().split() for line in lines]

for word in words:
    shu kubiklarga nicha suz yasash mumkinligni hisobla chiq,
    keyin yana boshqa yul bn kubik yasa, hisobla
