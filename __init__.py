# yumshatish va ayirish belsini chiqarib tashlanadi
# 27 ta harf
from nltk import ngrams
from itertools import combinations
import operator

letters = ['a', 'b', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'ō', 'p', 'q', 'r', 's', 'c', 't',
           'u', 'v', 'x', 'y', 'z', 'ḡ']  # 'ş', 'ç'

soft = ['a', 'i', 'o', 'u', 'e', 'ō',]
hard = ['r', 'l', 's', 't', 'n', 'm', 'q', 'k', 'y', 'h', 'b', 'd', 'z', 'v', 'p', 'f', 'g', 'j', 'ḡ', 'x', 'c']


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
           'u', 'v', 'w', 'x', 'y', 'z']  #  english
soft = ['a', 'i', 'o', 'u', 'e']
hard = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't',
           'v', 'w', 'x', 'y', 'z']

cc = 8  # cubic count
lc = len(letters) # length of alphabet
print("Len of the alphabet="+str(len(letters)))
cubics = []
for i in combinations(letters, 6):
    cubics.append(i)
print("Count of all available cubics generated from letters = " + str(len(cubics)))
#print(cubics[0])
# print("-------Print one combination for game's "+str(cc)+" cubics-------")
# for i in combinations(cubics, cc):
#     print(i)
#     break

words = []
with open("words_eng", encoding="utf8") as file:
    lines = file.readlines()
words = [line.rstrip() for line in lines]

letter_frq = {}
bi_freq = {}
tri_freq= {}
for word in words:
    # if len(word)>4:
    #     continue
    # calculating letter frq
    for c in word:
        if c in letter_frq:
            letter_frq[c] += 1
        else:
            letter_frq[c] = 1

    # calculating bigram frq
    bigrams = ngrams(word, 2)
    trigrams = ngrams(word, 3)
    for grams in bigrams: # grams = ('z', 'u')
        key = grams[0]+grams[1]
        if key in bi_freq:
            bi_freq[key] += 1
        else:
            bi_freq[key] = 1

    for grams in trigrams: # grams = ('z', 'u', 'k')
        key = grams[0]+grams[1]+grams[2]
        if key in tri_freq:
            tri_freq[key] += 1
        else:
            tri_freq[key] = 1

letter_frq = dict(sorted(letter_frq.items(), key=operator.itemgetter(1), reverse=True))
bi_freq = dict(sorted(bi_freq.items(), key=operator.itemgetter(1), reverse=True))
tri_freq = dict(sorted(tri_freq.items(), key=operator.itemgetter(1), reverse=True))
print(letter_frq)

my_letters = letters.copy()
last_bi = ""
last_bi_ind = 0
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
    last_bi_ind += 1
last_bi_ind += 1 # after break must add 1
print(last_bi)
print(last_bi_ind)

new_bi_freq = dict(list(bi_freq.items())[0:last_bi_ind])
print(new_bi_freq)
# print(tri_freq)

cubletter = ""
dubl = []
if cc*6 - lc > 0:
    if cc*6 - lc <= len(soft):
        dubl = soft[:cc*6-lc]
    else:
        dubl = soft + list(hard)[:cc*6-lc-len(soft)]
    # dubl = list(letter_frq)[:cc*6-lc]
print("dubl="+",".join(dubl))
# dubl = []
new_bi_freq = dict(list(bi_freq.items())[0:last_bi_ind])
new_dbl = [] # sorted by bigram order

for i in new_bi_freq:
    if i[0] not in cubletter:
        cubletter += i[0]
        if i[0] in dubl:
            # cubletter += i[0]
            dubl.remove(i[0])
            new_dbl.append(i[0])
    if i[1] not in cubletter:
        cubletter += i[1]
        if i[1] in dubl:
            # cubletter += i[1]
            dubl.remove(i[1])
            new_dbl.append(i[1])
print(cubletter)
print(new_dbl)

# for i in range(cc):
#     for j in range(6):
#         print(cubletter[j*cc+i], end='\t')
#     print()

cubes =[]
cubes = [[] for i in range(cc)]
cnt=0
for j in range(6):
    for i in range(cc):
        if len(cubletter)>cnt:
            cubes[i].append(cubletter[cnt])
            cnt += 1

cnt1 = 0
di = 0
for i in range(6):
    for j in range(cc):
        if cnt1 >= cnt:
            # if cubletter[cnt1] in cubes[j]
            cubes[j].append(new_dbl[di])
            di += 1
        cnt1 += 1

for i in range(cc):
    for j in range(6):
        print(cubes[i][j], end='\t')
    print()

# checking errors in words' letter
for i in letter_frq:
    if i not in letters:
        print("Errors by mismatch between word letter and letters letter " + i)