from itertools import permutations
import operator

cc = 8
cubics = []
words = []
with open("words", encoding="utf8") as file:
    lines = file.readlines()
words = [line.rstrip() for line in lines]

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
