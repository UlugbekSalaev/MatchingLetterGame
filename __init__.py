# yumshatish va ayirish belsini chiqarib tashlanadi
# 27 ta harf
from nltk import ngrams
from itertools import combinations
from itertools import permutations
import operator

letters = ['a', 'b', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'ō', 'p', 'q', 'r', 's', 'c', 't',
           'u', 'v', 'x', 'y', 'z', 'ḡ']  # 'ş', 'ç'
cc = 7  # cubic count
print(len(letters))
cubics = []
for i in combinations(letters, 6):
    cubics.append(i)
print("Count of all available cubics generated from letters = " + str(len(cubics)))
#print(cubics[0])
print("-------Print one combination for game's 8 cubics-------")
for i in combinations(cubics, cc):
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
bi_freq = dict(sorted(bi_freq.items(), key=operator.itemgetter(1), reverse=True))
print(letter_frq)
print(dict(list(bi_freq.items())[0:120]))

my_letters = letters.copy()
last_bi = ""
ind = 0
for i in bi_freq:
    if i[0] in my_letters:
        my_letters.remove(i[0])
        if not my_letters:
            last_bi = i
            break
    if i[1] in my_letters:
        my_letters.remove(i[1])
        if not my_letters:
            last_bi = i
            break
    ind += 1
print(last_bi)
print(ind)

cubletter = ""
dubl = ['a','i','o','r','l','s','u','t','n','m','k','q','b','h','y']
new_bi_freq = dict(list(bi_freq.items())[0:120])
for i in new_bi_freq:
    if i[0] not in cubletter:
        cubletter += i[0]
    else:
        if i[0] in dubl:
            cubletter += i[0]
            dubl.remove(i[0])
    if i[1] not in cubletter:
        cubletter += i[1]
    else:
        if i[1] in dubl:
            cubletter += i[1]
            dubl.remove(i[1])

for i in range(7):
    for j in range(7):
        print(cubletter[i*6+j], end='\t')
    print()

# checking errors in words' letter
for i in letter_frq:
    if i not in letters:
        print("Errors by mismatch between word letter and letters letter " + i)

cubics = []
with open("cubics"+str(cc), encoding="utf8") as file: # one row is cubic's letter
    lines = file.readlines()
    cubics = [line.rstrip().split() for line in lines]

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

card_words_cnt = dict(sorted(card_words_cnt.items(), key=operator.itemgetter(1), reverse=True))
with open("card_words"+str(cc), "w", encoding="utf8") as file:
    for i in card_words_cnt:
        file.writelines(i + "," + str(card_words_cnt[i]) + "\n")
