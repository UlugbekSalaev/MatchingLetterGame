# yumshatish va ayirish belsini chiqarib tashlanadi
# 27 ta harf
from nltk import ngrams
from itertools import combinations
import operator
import random

dataset = "ru"  # en, uz, ru
if dataset == "uz":
    letters = ['a', 'i', 'o', 'r', 'l', 's', 't', 'u', 'n', 'm', 'q', 'k', 'y', 'h', 'b', 'e', 'd', 'z', 'v', 'ō', 'p', 'f', 'g', 'j', 'ḡ', 'x', 'c']  # 'ş', 'ç'
    soft = ['a', 'i', 'o', 'u', 'e', 'ō']
    hard = ['r', 'l', 's', 't', 'n', 'm', 'q', 'k', 'y', 'h', 'b', 'd', 'z', 'v', 'p', 'f', 'g', 'j', 'ḡ', 'x', 'c']
if dataset == "en":
    letters = ['e', 'a', 's', 'o', 'r', 'l', 't', 'i', 'd', 'n', 'c', 'u', 'b', 'p', 'm', 'h', 'g', 'f', 'y', 'k', 'w', 'v', 'x', 'z', 'j', 'q']  #  english
    soft = ['e', 'a', 'o', 'i', 'u']
    hard = ['s', 'r', 'l', 't', 'd', 'n', 'c', 'b', 'p', 'm', 'h', 'g', 'f', 'y', 'k', 'w', 'v', 'x', 'z', 'j', 'q']
if dataset == "ru":
    letters = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я', 'ь', 'б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ']  #  russian
    soft = ['а', 'о', 'е', 'и', 'у', 'ь', 'ё', 'я', 'ы', 'ю', 'э']
    hard = ['б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ']

cc = 8  # cubic count
lc = len(letters) # length of alphabet
print("Len of the alphabet="+str(len(letters)))

# words = []
# with open("words_"+dataset, encoding="utf8") as file:
#     lines = file.readlines()
# words = [line.rstrip() for line in lines]
# letter_frq = {}
# obsh=0
# for word in words:
#     for c in word:
#         obsh+=1
#         if c in letter_frq:
#             letter_frq[c] += 1
#         else:
#             letter_frq[c] = 1
# print(letter_frq)
# print(obsh)
# exit()

# ## get datasets as training and test dataset
# random.shuffle(words)
# k = 5
# print(words)
#
train = [[],[],[],[],[]]
test = [[],[],[],[],[]]
# if dataset == "uz":
#     train[0] = words[:3648]
#     test[0]  = words[3648:]
#
#     train[1] = words[:2736] + words[3648:]
#     test[1]  = words[2736:3648]
#
#     train[2] = words[:1824] + words[2736:]
#     test[2]  = words[1824:2736]
#
#     train[3] = words[:912] + words[1824:]
#     test[3]  = words[912:1824]
#
#     train[4] = words[912:]
#     test[4]  = words[:912]
# else:
#     train[0] = words[:4816]
#     test[0]  = words[4816:]
#
#     train[1] = words[:3612] + words[4816:]
#     test[1]  = words[3612:4816]
#
#     train[2] = words[:2408] + words[3612:]
#     test[2]  = words[2408:3612]
#
#     train[3] = words[:1204] + words[2408:]
#     test[3]  = words[1204:2408]
#
#     train[4] = words[1204:]
#     test[4]  = words[:1204]
# if dataset == "ru":
#     train[0] = words[:2456]
#     test[0]  = words[2456:]
#
#     train[1] = words[:1842] + words[2456:]
#     test[1]  = words[1842:2456]
#
#     train[2] = words[:1228] + words[1842:]
#     test[2]  = words[1228:1842]
#
#     train[3] = words[:614] + words[1228:]
#     test[3]  = words[614:1228]
#
#     train[4] = words[567:]
#     test[4]  = words[:567]

for iteration in range(5):
    # with open("test" + str(iteration), "w", encoding="utf8") as file:
    #     for i in test[iteration]:
    #         file.writelines(i + "\n")
    # with open("train" + str(iteration), "w", encoding="utf8") as file:
    #     for i in train[iteration]:
    #         file.writelines(i + "\n")
    # continue
    with open("result/test_"+dataset + "/train" + str(iteration), encoding="utf8") as file:
        lines = file.readlines()
    train[iteration] = [line.rstrip() for line in lines]

for app in range(2):
    for iteration in range(5):

        letter_frq = {}
        bi_freq = {}
        for word in train[iteration]:
            for c in word:
                if c in letter_frq:
                    letter_frq[c] += 1
                else:
                    letter_frq[c] = 1

            # calculating bigram frq
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

        my_letters = letters.copy()
        last_bi = ""
        last_bi_ind = 0
        # for i in bi_freq:
        #     if i[0] in my_letters:
        #         my_letters.remove(i[0])
        #         if not my_letters:
        #             last_bi = i
        #             break
        #     if i[1] in my_letters:
        #         my_letters.remove(i[1])
        #         if not my_letters:
        #             last_bi = i
        #             break
        #     last_bi_ind += 1
        ml = set()
        for i in bi_freq:
            ml.add(i[0])
            ml.add(i[1])
            last_bi = i
            last_bi_ind += 1
            if ml == set(letters):
                break
        # last_bi_ind += 1 # after break must add 1
        print(last_bi)
        print(last_bi_ind)

        new_bi_freq = dict(list(bi_freq.items())[0:last_bi_ind])

        print(new_bi_freq)

        dubl = []
        if cc*6 - lc > 0:
            # approach LF oriented
            if app == 0:
                # dubl = list(letter_frq)[:cc*6-lc]
                dubl = list(letter_frq)[:cc*6-len(letter_frq)]

            # approach Vowel oriented
            if app == 1:
                if dataset == "uz":
                    dubl = soft + ['a', 'i', 'o'] + hard    # uz
                if dataset == "en":
                    dubl = soft + ['e', 'a', 'o', 'i'] + hard   # en
                if dataset == "ru":
                    dubl = ['а','о','е'] + soft + hard # ru
                # dubl = dubl[:cc*6-lc]
                dubl = dubl[:cc*6-len(letter_frq)]

                # if cc*6 - lc <= len(soft):
                #     dubl = soft[:cc*6-lc]
                # else:
                #     dubl = soft + list(hard)[:cc*6-lc-len(soft)]

        print("dubl="+",".join(dubl))

        cubletter = ""
        new_dbl = [] # sorted by bigram order

        for i in new_bi_freq:
            if i[0] not in cubletter:
                cubletter += i[0]
                if i[0] in dubl:
                    # cubletter += i[0]
                    dubl.remove(i[0])
                    new_dbl.append(i[0])
                if i[0] in dubl:    # Vowel approachda dublda 2 ta bir xil harf buladi (unlilardan)
                    # cubletter += i[0]
                    dubl.remove(i[0])
                    new_dbl.append(i[0])
            if i[1] not in cubletter:
                cubletter += i[1]
                if i[1] in dubl:
                    # cubletter += i[1]
                    dubl.remove(i[1])
                    new_dbl.append(i[1])
                if i[1] in dubl:
                    # cubletter += i[1]
                    dubl.remove(i[1])
                    new_dbl.append(i[1])

        new_dbl = new_dbl + dubl
        print(cubletter)

        print("new dubl=" + ",".join(new_dbl))

        cubes =[]
        cubes = [[] for i in range(cc)]
        cnt=0
        for j in range(6):
            for i in range(cc):
                if len(cubletter)>cnt:
                    cubes[i].append(cubletter[cnt])
                    cnt += 1

        # for i in range(cc):
        #     for j in range(6):
        #         print(cubes[i][j], ' ')
        #     print(" newline \n ")
        # print("notall=", cubes)

        cnt1 = 0
        di = 0
        for i in range(6):
            for j in range(cc):
                if cnt1 >= cnt:
                    # if cubletter[cnt1] in cubes[j]
                    cubes[j].append(new_dbl[di])
                    di += 1
                cnt1 += 1

        print("Approach -", app, ", Iteration - ", iteration)
        with open("result/test_"+dataset+"/"+str(cc)+"cub/train_res_app"+str(app)+"_it" + str(iteration), "w", encoding="utf8") as file:
            for i in range(cc):
                for j in range(6):
                    file.write(cubes[i][j] + '\t')
                file.writelines("\n")
        for i in range(cc):
            for j in range(6):
                print(cubes[i][j], end='\t')
            print()

        # checking errors in words' letter
        for i in letter_frq:
            if i not in letters:
                print("Errors by mismatch between word letter and letters letter " + i)