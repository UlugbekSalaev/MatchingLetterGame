from itertools import permutations
import operator

dataset = "fr"  # [uz,en,ru,sl] new dataset [de,es,fr,kz,ms,pl,tr,tt]
cc = 8  # cubic count 5-8
print(dataset + " " + str(cc) + "cub")

if dataset == "uz":
    soft = ['a', 'i', 'o', 'u', 'e', 'ō']  # uz
if dataset == "en":
    soft = ['e', 'a', 'o', 'i', 'u']  # en
if dataset == "ru":
    soft = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я', 'ь']  # ru
if dataset == "sl":
    soft = ['a', 'e', 'o', 'i', 'u']  # sl
if dataset == "de":
    soft = ['a', 'e', 'i', 'o', 'u', 'ä', 'ö', 'ü']
if dataset == "es":
    soft = ['a', 'e', 'i', 'o', 'u']
if dataset == "fr":
    soft = ['a', 'e', 'i', 'o', 'u', 'y']
if dataset == "kz":
    soft = ['ә', 'ө', 'і', 'а', 'е', 'и', 'о', 'у', 'ю', 'я', 'ы']
if dataset == "ms":
    soft = ['a', 'e', 'i', 'o', 'u']
if dataset == "pl":
    soft = ['a', 'ą', 'e', 'ę', 'i', 'o', 'ó', 'u', 'y']
if dataset == "tr":
    soft = ['a', 'e', 'ı', 'i', 'o', 'ö', 'u', 'ü']
if dataset == "tt":
    soft = ['а', 'ә', 'е', 'и', 'о', 'ө', 'у', 'ү', 'ы']

cubics = []
words = []


def is_exist(word: str, n: int, cubic: tuple):
    for i in range(n):
        if word[i] not in cubic[i]:
            return False
    return True


for app in range(2):
    for iteration in range(5):
        print("App=", app, " iteration=", iteration)

        with open("result/test_" + dataset + "/test" + str(iteration), encoding="utf8") as file:
            lines = file.readlines()
        words = [line.rstrip() for line in lines]

        with open("result/test_" + dataset + "/" + str(cc) + "cub/train_res_app" + str(app) + "_it" + str(iteration),
                  encoding="utf8") as file:  # one row is cubic's letter
            lines = file.readlines()
            cubics = [line.rstrip().split() for line in lines]

        # checking restrictions
        all_softs = 0
        for i in cubics:
            for j in i:
                if j in soft:
                    all_softs += 1
        per_max_soft = int(all_softs / cc) + 1
        per_min_soft = int(all_softs / cc)
        # print("Per softs = ", per_min_soft, per_max_soft, all_softs, all_softs % cc)
        for i in cubics:
            ss = set(i)
            if len(ss) != len(i):
                print("there is dublicate in cubic", i)
            sc = 0
            for j in i:
                if j in soft:
                    sc += 1
            # if app == 0:
            #     if sc>2:
            #         print("There is more vowel in cubic:", i)
            # else:
            #     if sc>3:
            #         print("There is more vowel in cubic:", i)
            if sc > per_max_soft:  # sc < per_min_soft or
                print("Vowel not in min_max range in cubic:", i)
        card_words_cnt = {}

        for word in words:
            # shu kubiklarga nicha suz yasash mumkinligni hisobla chiq,
            # keyin yana boshqa yul bn kubik yasa, hisobla
            n = len(word)  # word's length
            for i in permutations(cubics, n):
                if is_exist(word, n, i):
                    if word in card_words_cnt:
                        card_words_cnt[word] += 1
                    else:
                        card_words_cnt[word] = 1

        card_words_cnt = dict(sorted(card_words_cnt.items(), key=operator.itemgetter(1), reverse=True))
        with open("result/test_" + dataset + "/" + str(cc) + "cub/test_res_app" + str(app) + "_it" + str(iteration),
                  "w", encoding="utf8") as file:
            for i in card_words_cnt:
                file.writelines(i + "," + str(card_words_cnt[i]) + "\n")
