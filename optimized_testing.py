import math
from itertools import permutations
import os
import statistics


def read_all_res(directory, words, dataset):
    res_set = []
    i = 0
    for filename in os.listdir(directory):
        i += 1
        file_path = os.path.join(directory, filename)
        with open(file_path, "r") as file:
            row = [line.strip().split(',') for line in file.readlines()]
            # print(row[0])

            res_set.append((row[0][0], row[0][1]))  # 0 - 6 letter, 1 - 7 letter

    # for i, length in enumerate([6, 7]):
    counts6 = [int(wc[0]) for wc in res_set]
    counts7 = [int(wc[1]) for wc in res_set]
    count_t = [int(wc[0])+int(wc[1]) for wc in res_set]

    # dataset, generated cubes count, avg 6letter, stdev 6letter, avg 7letter, stdev 7letter, avg total, stdev total, max in total
    _, _, files = next(os.walk(f"result/{dataset}/9cub/optimized"))
    cubset_count = len(files)

    print(f"{dataset} \t {len(count_t)}/{cubset_count} \t "
          f"{sum(counts6) / len(counts6) / len(words[6])*100:.4f} \t "
          f"{statistics.stdev(counts6) if len(counts6) > 1 else 0:.2f} \t"
          f"{sum(counts7) / len(counts7) / len(words[7])*100:.4f} \t "
          f"{statistics.stdev(counts7) if len(counts7) > 1 else 0:.2f} \t"
          f"{sum(count_t) / len(count_t) / (len(words[6])+len(words[7]))*100:.4f} \t "
          f"{statistics.stdev(count_t) if len(count_t) > 1 else 0:.2f} \t"
          f"{max(count_t) / (len(words[6]) + len(words[7])) * 100:.4f}"
          )

def read_words(file_path):
    with open(file_path, "r") as file:
        words1 = {line.strip() for line in file.readlines()}
    # word_sets = {3: set(), 4: set(), 5: set()}
    word_sets = {6: set(), 7: set()}
    for word in words1:
        if len(word) in word_sets:
            word_sets[len(word)].add(word)
    return word_sets


def read_cubes(file_path):
    with open(file_path, "r") as file:
        return [line.strip().split('\t') for line in file.readlines()]


def read_all_cube_sets(directory):
    cube_sets1 = []
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        cube_sets1.append(read_cubes(file_path))
    return cube_sets1[:math.floor(len(cube_sets1)/8)]
    # return cube_sets


def is_exist(word: str, n: int, cubic: tuple):
    for i in range(n):
        if word[i] not in cubic[i]:
            return False
    return True


def can_form_word(word, cubes):
    # print(word)
    # print(cubes)
    # if len(word) > len(cubes):
    #     return False

    n = len(word)  # word's length
    for i in permutations(cubes, n):
        if is_exist(word, n, i):
            return True
    return False

    # for combination in product(*cubes[:len(word)]):
    #     if all(letter in cube for letter, cube in zip(word, cubes)):
    #         return True
    # return False


def count_words_by_length(words1, cube_sets1, dataset1, path):
    results = []
    i = 67
    for cubes in cube_sets1[67:]:
        i = i + 1
        # count_3 = sum(1 for word in words[3] if can_form_word(word, cubes))
        # count_4 = sum(1 for word in words[4] if can_form_word(word, cubes))
        # count_5 = sum(1 for word in words[5] if can_form_word(word, cubes))
        count_6 = sum(1 for word in words1[6] if can_form_word(word, cubes))
        count_7 = sum(1 for word in words1[7] if can_form_word(word, cubes))
        # results.append((count_3, count_4, count_5))

        with open(f"{path}/res/{i}", "w") as file:
            file.writelines(str(count_6) + "," + str(count_7))

        print(i)
    return results


def print_statistics(words1, word_counts1, dataset1, cub_soni):
    print(dataset1, cub_soni)
    for i, length in enumerate([6, 7]):
        counts = [wc[i] for wc in word_counts1]
        print(f"{len(counts)} \t {len(words1[length])} \t {max(counts)} \t "
              f"{sum(counts)*100/(len(counts)*len(words[length])):.4f} \t "
              f"{statistics.stdev(counts) if len(counts) > 1 else 0:.2f}")


# File paths
datasets = ['en', 'es', 'fr', 'kz', 'ms', 'pl', 'ru', 'sl', 'tr', 'tt', 'uz']

for dataset in datasets:
    words = read_words(f"Dataset/letter67/words_{dataset}")
    read_all_res(f"result/{dataset}/9cub/res", words, dataset)
exit()

for dataset in ["pl"]:

    path = f"result/{dataset}/9cub"
    print(path)
    cube_sets = read_all_cube_sets(path + "/optimized")
    print("Kubikla soni=", len(cube_sets))
    words = read_words(f"Dataset/letter67/words_{dataset}")
    word_counts = count_words_by_length(words, cube_sets, dataset, path)
    # print_statistics(words, word_counts, dataset, "8cub")
