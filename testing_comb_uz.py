# result/testuz/8cub/combination ichidagilarni hisoblash uchun
from itertools import permutations
import operator
import time

# dataset = "de"  # [uz,en,ru,sl] new dataset [de,es,fr,kz,ms,pl,tr,tt] # 0 0 0 0 0 2 3 4   # # 1 0 0 2 2 0 2 1

start_time = time.time()


def is_exist(word: str, n: int, cubic: tuple):
    for i in range(n):
        if word[i] not in cubic[i]:
            return False
    return True

cc = 9
datasets =  ['uz']
approach = "lf"
iterations = [0] # 2 4

for i in range(len(datasets)):
    print(datasets[i], iterations[i])

    dataset = datasets[i]
    iteration= iterations[i]

    words = [[], [], [], [], []]

    with open("result_67/test_" + dataset + "/test" + str(iteration), encoding="utf8") as file:
        lines = file.readlines()
    words[iteration] = ([line.rstrip() for line in lines])

    for app in range(10):
        cubics = []
        with open("result_67/test_" + dataset + "/" + str(cc) + "cub/combinations/"+approach + str(app + 1),
                  encoding="utf8") as file:  # one row is cubic's letter
            lines = file.readlines()
            cubics = [line.rstrip().split() for line in lines]

        if True:#for iteration in range(4, 5):
            print(dataset, " File=", app, "Approach=", approach,  " iteration=", iteration)

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
                # shu kubiklarga nicha suz yasash mumkinligni hisobla chiq,
                # keyin yana boshqa yul bn kubik yasa, hisobla
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
            with open(
                    "result_67/test_" + dataset + "/" + str(cc) + "cub/comb_words/" +approach + str(app) + "_it" + str(iteration),
                    "w", encoding="utf8") as file:
                for i in card_words_cnt:
                    file.writelines(i + "," + str(card_words_cnt[i]) + "\n")
print(time.time() - start_time)
