# result/testuz/8cub/combination ichidagilarni hisoblash uchun
from itertools import permutations
import operator

cc = 8

def is_exist(word:str, n:int, cubic: tuple):
    for i in range(n):
        if word[i] not in cubic[i]:
            return False
    return True

for dataset in ('sl',):
    words = [[],[],]
    for iteration in range(2):
        with open("result/test_" + dataset + "/test" + str(iteration), encoding="utf8") as file:
            lines = file.readlines()
        words[iteration]=([line.rstrip() for line in lines])

    for app in range(0,1008):
        cubics = []
        with open("result/test_" + dataset + "/" + str(cc) + "cub/combinations/" + str(app + 1), encoding="utf8") as file:  # one row is cubic's letter
            lines = file.readlines()
            cubics = [line.rstrip().split() for line in lines]

        for iteration in range(2):
            print(dataset, " App=", app, " iteration=", iteration)

            # checking restrictions
            # all_softs = 0
            # for i in cubics:
            #     for j in i:
            #         if j in soft:
            #             all_softs += 1
            # per_max_soft = int(all_softs / cc) +1
            # per_min_soft = int(all_softs / cc)
            # # print("Per softs = ", per_min_soft, per_max_soft, all_softs, all_softs % cc)
            # for i in cubics:
                # ss = set(i)
                # if len(ss) != len(i):
                #     print("there is dublicate in cubic", i)
                # sc = 0
                # for j in i:
                #     if j in soft:
                #         sc += 1
                # if app == 0:
                #     if sc>2:
                #         print("There is more vowel in cubic:", i)
                # else:
                #     if sc>3:
                #         print("There is more vowel in cubic:", i)
                # if sc > per_max_soft: #sc < per_min_soft or
                #     print("Vowel not in min_max range in cubic:", i)
            card_words_cnt = {}

            for word in words[iteration]:
                #shu kubiklarga nicha suz yasash mumkinligni hisobla chiq,
                #keyin yana boshqa yul bn kubik yasa, hisobla
                n = len(word)  # word's length
                for i in permutations(cubics, n):
                    if is_exist(word, n, i):
                        # if word in card_words_cnt:
                        #     card_words_cnt[word] += 1
                        # else:
                        #     card_words_cnt[word] = 1
                        card_words_cnt[word] = 1
                        continue

            # card_words_cnt = dict(sorted(card_words_cnt.items(), key=operator.itemgetter(1), reverse=True))
            with open("result/test_"+dataset+"/"+str(cc)+"cub/comb_words/lf"+str(app)+"_it"+str(iteration), "w", encoding="utf8") as file:
                for i in card_words_cnt:
                    file.writelines(i + "," + str(card_words_cnt[i]) + "\n")