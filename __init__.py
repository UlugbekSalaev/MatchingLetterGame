# yumshatish va ayirish belsini chiqarib tashlanadi
# 27 ta harf
from nltk import ngrams
from itertools import combinations
from itertools import permutations
import operator

letters = ['a', 'b', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'ō', 'p', 'q', 'r', 's', 'c', 't',
           'u', 'v', 'x', 'y', 'z', 'ḡ']  # 'ş', 'ç'
print(len(letters))
cubics = []
for i in combinations(letters, 6):
    cubics.append(i)
print("cubics count = " + str(len(cubics)))

for i in combinations(cubics, 8):
    print(i)
    break

words = []
letter_frq = {}
with open("words", encoding="utf8") as file:
    lines = file.readlines()
words = [line.rstrip() for line in lines]

bi_freq = {}
for word in words:
    for c in word:
        if c in letter_frq:
            letter_frq[c] += 1
        else:
            letter_frq[c] = 1

    bigrams = ngrams(word, 2)
    for grams in bigrams: # grams = ('z', 'u')
        key = grams[0]+grams[1]
        if key in bi_freq:
            bi_freq[key] += 1
        else:
            bi_freq[key] = 1

letter_frq = dict(sorted(letter_frq.items(), key=operator.itemgetter(1), reverse=True))
bi_freq = dict( sorted(bi_freq.items(), key=operator.itemgetter(1), reverse=True))
print(letter_frq)
print(bi_freq)
for i in letter_frq:
    if i not in letters:
        print("Errors by mismatch between word letter and letters letter" + i)

cubics = []
with open("cubics", encoding="utf8") as file: # one row is cubic's letter
    lines = file.readlines()
    cubics = [line.rstrip().split() for line in lines]

card_words = {}
card_words_cnt = {}

def is_exist(word:str, n:int, cubic: tuple):
    for i in range(n):
        if word[i] not in cubic[i]:
            return False
    return True

for word in words:
    #shu kubiklarga nicha suz yasash mumkinligni hisobla chiq,
    #keyin yana boshqa yul bn kubik yasa, hisobla
    n = len(word)  # word's length
    for i in permutations(cubics, n):
        if is_exist(word, n, i):
            if word in card_words_cnt:
                card_words_cnt[word] += 1
            else:
                card_words_cnt[word] = 1
                card_words[word] = i

card_words_cnt = dict(sorted(card_words_cnt.items(), key=operator.itemgetter(1), reverse=True))
ss = 0
with open("card_words", "w", encoding="utf8") as file:
    for i in card_words_cnt:
        file.writelines(i + "," + str(card_words_cnt[i]) + "\n")
        ss += card_words_cnt[i]
print(ss)