from itertools import permutations
import operator
soft = ['a', 'i', 'o', 'u', 'e', 'ō']
cc = 8
cubics = []
words = []
with open("words_eng", encoding="utf8") as file:
    lines = file.readlines()
words = [line.rstrip() for line in lines]

with open("cubics"+str(cc), encoding="utf8") as file: # one row is cubic's letter
    lines = file.readlines()
    cubics = [line.rstrip().split() for line in lines]

# checking restrictions
for i in cubics:
    ss = set(i)
    if len(ss) != len(i):
        print("there is dublicate in cubic", i)
    sc = 0
    for j in i:
        if i in soft:
            sc += 1
    if sc>2:
        print("There is more vovel in cubic:", i)

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

# exit()
# calculate information
t3 = 518
t4 = 1165
t5 = 2875

t3 = 1026
t4 = 2499
t5 = 2499

print('#', '\t', t3+t4+t5, '\t', t3, '\t', t4, '\t', t5, '\t')
for ind in range(4,9):
    with open("card_words"+str(ind), encoding="utf8") as file: #
        lines = file.readlines()
        words_c = [line.rstrip().split(',')[0] for line in lines]

    cnt3=0
    cnt4=0
    cnt5=0
    for i in words_c:
        if len(i) == 3:
            cnt3 += 1
        if len(i) == 4:
            cnt4 += 1
        if len(i) == 5:
            cnt5 += 1
    print(ind, '\t', len(words_c), '\t', cnt3, '\t', cnt4, '\t', cnt5, '\t')
    print(ind, '\t', round(len(words_c)/(t3+t4+t5),3), '\t', round(cnt3/t3,3), '\t', round(cnt4/t4,3), '\t', round(cnt5/t5,3), '\t')
