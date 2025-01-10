# yumshatish va ayirish belsini chiqarib tashlanadi
# 27 ta harf
from nltk import ngrams
from itertools import combinations
import operator
import random
import time

dataset = "tt"  # [uz,en,ru,sl] new dataset [de,es,fr,kz,ms,pl,tr,tt]
cc = 8  # cubic count 5-8

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
if dataset == "sl":
    letters = ['a', 'b', 'c', 'č', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 'š', 't', 'u', 'v', 'z', 'ž']  #  sloven
    soft = ['a', 'e', 'o', 'i', 'u']
    hard =  ['b', 'c', 'č', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'r', 's', 'š', 't', 'v', 'z', 'ž']  #  english
if dataset == "de":
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'ä', 'ö', 'ü', 'ß']  #  german
    soft = ['a', 'e', 'i', 'o', 'u', 'ä', 'ö', 'ü']
    hard = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z', 'ß']
if dataset == "es":
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']  # spanish
    soft = ['a', 'e', 'i',  'o', 'u']
    hard = [ 'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'ñ', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
if dataset == "fr":
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'é', 'è', 'ê', 'ë', 'ç', 'à', 'â', 'æ', 'ï', 'ô', 'û', 'œ', 'î', 'ÿ']  #  french
    soft = ['a', 'e', 'i', 'o', 'u', 'y', 'é', 'è', 'ê', 'ë', 'à', 'â', 'æ', 'ï', 'ô', 'û', 'œ', 'î', 'ÿ']
    hard = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z', 'ç']
if dataset == "kz":
    letters = ['ә', 'ғ', 'қ', 'ң', 'ө', 'ұ', 'ү', 'һ', 'і', 'а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я', 'ь', 'б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ']  #  german
    soft = ['ә', 'ө', 'і', 'а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я', 'ь']
    hard = ['ғ', 'қ', 'ң', 'ұ', 'ү', 'һ', 'б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ']
if dataset == "ms":
    letters = ['a',	'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']  # malay
    soft = ['a', 'e', 'i', 'o', 'u']
    hard = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
if dataset == "pl":
    letters = ['a', 'ą', 'b', 'c', 'ć', 'd', 'e', 'ę', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'ł', 'm', 'n', 'ń', 'o', 'ó', 'p', 'r', 's', 'ś', 't', 'u', 'w', 'y', 'z', 'ź', 'ż']  # polish
    soft = ['a', 'ą', 'e', 'ę', 'i', 'o', 'ó', 'u', 'y']
    hard = ['b', 'c', 'ć', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'ł', 'm', 'n', 'ń', 'p', 'r', 's', 'ś', 't', 'w', 'z', 'ź', 'ż']
if dataset == "tr":
    letters = ['a', 'e', 'ı', 'i', 'o', 'ö', 'u', 'ü', 'b', 'c', 'ç', 'd', 'f', 'g', 'ğ', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'r', 's', 'ş', 't', 'v', 'y', 'z']  # turkish
    soft = ['a', 'e', 'ı', 'i', 'o', 'ö', 'u', 'ü']
    hard = ['b', 'c', 'ç', 'd', 'f', 'g', 'ğ', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'r', 's', 'ş', 't', 'v', 'y', 'z']
if dataset == "tt":
    letters = ['а', 'ә', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'җ', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'ң', 'о', 'ө', 'п', 'р', 'с', 'т', 'у', 'ү', 'ф', 'х', 'һ', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']  #  tatar
    soft = ['а', 'ә', 'е', 'и', 'о', 'ө', 'у', 'ү', 'ы']
    hard = ['ё', 'б', 'в', 'г', 'д', 'ж', 'җ', 'з', 'й', 'к', 'л', 'м', 'н', 'ң', 'п', 'р', 'с', 'т', 'ф', 'х', 'һ', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ь', 'э', 'ю', 'я']

lc = len(letters) # length of alphabet
# print("Len of the alphabet="+str(len(letters)))

# words = []
# with open("words_"+dataset, encoding="utf8") as file:
#     lines = file.readlines()
# words = [line.rstrip() for line in lines]
# letter_frq = {}
# obsh=0
# print(len(words))
# for word in words:
#     for c in word:
#         obsh+=1
#         if c in letter_frq:
#             letter_frq[c] += 1
#         else:
#             letter_frq[c] = 1

# print(letter_frq)
# print(obsh)
# for x,y in letter_frq.items():
#     print(x, '\t', y)

# ## get datasets as training and test dataset
# random.shuffle(words)
# k = 5
# print(words)

#
train = [[],[],[],[],[]]
# test = [[],[],[],[],[]]
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
#     train[0] = words[:3448]
#     test[0]  = words[3448:]
#
#     train[1] = words[:2586] + words[3448:]
#     test[1]  = words[2586:3448]
#
#     train[2] = words[:1724] + words[2586:]
#     test[2]  = words[1724:2586]
#
#     train[3] = words[:862] + words[1724:]
#     test[3]  = words[862:1724]
#
#     train[4] = words[862:]
#     test[4]  = words[:862]
# if dataset == "sl":
#     train[0] = words[:5024]
#     test[0]  = words[5024:]
#
#     train[1] = words[:3768] + words[5024:]
#     test[1]  = words[3768:5024]
#
#     train[2] = words[:2512] + words[3768:]
#     test[2]  = words[2512:3768]
#
#     train[3] = words[:1256] + words[2512:]
#     test[3]  = words[1256:2512]
#
#     train[4] = words[1256:]
#     test[4]  = words[:1256]

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
    total_time = 0
    for iteration in range(5):
        start_time = time.time()
        # print("app=",app, "iter=", iteration)
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
        # print(last_bi)
        # print(last_bi_ind)

        new_bi_freq = dict(list(bi_freq.items())[0:last_bi_ind])

        # print(new_bi_freq)

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
                    dubl = soft+ ['а','о','е'] + hard # ru
                if dataset == "sl":
                    dubl = soft+ ['a', 'e', 'o', 'i'] + hard # ru

                if dataset == "de":
                    dubl = soft+ ['e', 'a', 'i'] + hard
                if dataset == "fr":
                    dubl = soft+ ['a', 'e', 'i', 'o'] + hard
                if dataset == "ms":
                    dubl = soft+ ['a', 'i', 'e', 'u', 'o'] + hard
                if dataset == "pl":
                    dubl = soft + ['a', 'o', 'i', 'e'] + hard
                if dataset == "kz":
                    dubl = soft+ ['а', 'е', 'ы'] + hard
                if dataset == "tr":
                    dubl = soft + ['a', 'e', 'i'] + hard
                if dataset == "tt":
                    dubl = soft + ['а', 'е', 'ә'] + hard
                if dataset == "es":
                    dubl = soft + ['a', 'o', 'e'] + hard

                # dubl = dubl[:cc*6-lc]
                dubl = dubl[:cc*6-len(letter_frq)]

                # if cc*6 - lc <= len(soft):
                #     dubl = soft[:cc*6-lc]
                # else:
                #     dubl = soft + list(hard)[:cc*6-lc-len(soft)]

        # print("dubl="+",".join(dubl))

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
        # print(cubletter)

        # print("new dubl=" + ",".join(new_dbl))

        cubes =[]
        cubes = [[] for i in range(cc)]
        #  --------------new version to cubes ----------
        cubletter1 = cubletter + "".join(new_dbl)
        # print(cubletter1)
        scub = hcub = ""  # scub = soft letter cub, hcub = hard letter cube
        for i in cubletter1:
            if i in soft:
                scub = scub + i
            else:
                hcub = hcub + i
        # print(scub, hcub)
        cubletter1 = scub + hcub

        for j in range(6):
            for i in range(cc):
                ii = 0
                while ii<len(cubletter1):
                    if cubletter1[ii:ii+1] not in cubes[i]:
                        cubes[i].append(cubletter1[ii:ii+1])
                        cubletter1 = cubletter1[:ii] + cubletter1[ii+1:]
                        break
                    else:
                        ii = ii + 1
                if ii== len(cubletter1):
                    cubes[i].append(cubletter1[0:1])
                    cubletter1 = cubletter1[:0] + cubletter1[1:]

        # print("Qolgan harfla=", cubletter1)

        # for i in range(cc):
        #     for j in range(6):
        #         print(cubes[i][j], end='\t')
        #     print()
        # exit()

        # cnt=0
        # for j in range(6):
        #     for i in range(cc):
        #         if len(cubletter)>cnt:
        #             cubes[i].append(cubletter[cnt])
        #             cnt += 1

        # cnt1 = 0
        # di = 0
        # for i in range(6):
        #     for j in range(cc):
        #         if cnt1 >= cnt:
        #             # if cubletter[cnt1] in cubes[j]
        #             cubes[j].append(new_dbl[di])
        #             di += 1
        #         cnt1 += 1

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

        # # checking errors in words' letter
        # for i in letter_frq:
        #     if i not in letters:
        #         print("Errors by mismatch between word letter and letters letter " + i)
        total_time = total_time + (time.time() - start_time)
    print("--- %s seconds ---" % (total_time/5))
    print("--- %s seconds ---" % (total_time))

print("finish")