from itertools import product, permutations
import os
import statistics


def read_words(file_path):
    with open(file_path, "r") as file:
        words = {line.strip() for line in file.readlines()}
    word_sets = {3: set(), 4: set(), 5: set()}
    for word in words:
        if len(word) in word_sets:
            word_sets[len(word)].add(word)
    return word_sets


def read_cubes(file_path):
    with open(file_path, "r") as file:
        return [line.strip().split('\t') for line in file.readlines()]

def read_all_cube_sets(directory):
    cube_sets = []
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        cube_sets.append(read_cubes(file_path))
    return cube_sets


def is_exist(word: str, n: int, cubic: tuple):
    for i in range(n):
        if word[i] not in cubic[i]:
            return False
    return True


def can_form_word(word, cubes):
    if len(word) > len(cubes):
        return False

    n = len(word)  # word's length
    for i in permutations(cubes, n):
        if is_exist(word, n, i):
            return True
    return False

    # for combination in product(*cubes[:len(word)]):
    #     if all(letter in cube for letter, cube in zip(word, cubes)):
    #         return True
    # return False

def count_words_by_length(words, cube_sets):
    results = []
    for cubes in cube_sets:
        count_3 = sum(1 for word in words[3] if can_form_word(word, cubes))
        count_4 = sum(1 for word in words[4] if can_form_word(word, cubes))
        count_5 = sum(1 for word in words[5] if can_form_word(word, cubes))
        results.append((count_3, count_4, count_5))
        print(len(results))
    return results

def print_statistics(words, word_counts):
    for i, length in enumerate([3, 4, 5]):
        counts = [wc[i] for wc in word_counts]
        print(f"{len(counts)} \t {len(words[length])} \t {max(counts)} \t {sum(counts)*100/(len(counts)*len(words[length])):.2f} \t {statistics.stdev(counts) if len(counts) > 1 else 0:.2f}")



# File paths
# datasets = ['de', 'en', 'es', 'fr', 'kz', 'ms', 'pl', 'ru', 'sl', 'tr', 'tt', 'uz']
for dataset in ['sl']:
    print(dataset)
    words = read_words(f"Dataset/letter35/words_{dataset}")
    cube_sets = read_all_cube_sets(f"result/{dataset}/8cub/optimized")
    word_counts = count_words_by_length(words, cube_sets)

    print_statistics(words, word_counts)
