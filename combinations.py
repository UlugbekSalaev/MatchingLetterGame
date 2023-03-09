import itertools
from itertools import combinations, product, permutations
import copy
from math import comb

# Define the given set of letters
letters = ['a', 'i', 'o', 'r', 'l', 's', 't', 'u', 'n', 'm', 'q', 'k', 'y', 'h', 'b', 'e', 'd', 'z', 'v', 'ō', 'p', 'f',
           'g', 'j', 'ḡ', 'x', 'c']  # 'ş', 'ç'

# # Generate all possible combinations of the given letters
# combos = list(itertools.combinations(letters, 6))
#
# print(len(combos))

# define the 8 cubes as strings
cubes = ['aildps', 'iomyjh', 'oinvḡt', 'uosbxk', 'euhcrq', 'ōetzld', 'aōkgmy', 'arqfnb']

cubes1 = [['a','i','l','d','p','s'], ['i','o','m','y','j','h'], ['o','i','n','v','ḡ','t'], ['u','o','s','b','x','k'], ['e','u','h','c','r','q'], ['ō','e','t','z','l','d'], ['a','ō','k','g','m','y'], ['a','r','q','f','n','b']]

# # define a function to generate all possible combinations
# def generate_combinations():
#     # loop over all possible combinations of 5 cubes
#     for c in itertools.combinations(range(8), 5):
#         # loop over all possible ways to keep at least 5 letters in their own cube
#         for k in range(6):
#             for l in range(k, 6):
#                 for m in range(l, 6):
#                     for n in range(m, 6):
#                         for o in range(n, 6):
#                             # get the letters that are kept in their own cube
#                             keep = [cubes[i][k] for i in c] + [cubes[i][l] for i in c] + [cubes[i][m] for i in c] + [cubes[i][n] for i in c] + [cubes[i][o] for i in c]
#                             # loop over all possible ways to swap the remaining letters
#                             for perm in itertools.product(range(8), repeat=5):
#                                 # get the letters from the other cubes
#                                 swap = [cubes[perm[i]][j] for i in range(5) for j in range(6) if i not in c]
#                                 # combine the letters and yield the result
#                                 yield keep + swap
#
# # print the total number of combinations
# print(len(list(generate_combinations())))

# -------------
# # Group 5 letters from each cube
# groups = [list(itertools.combinations(cube, 5)) for cube in cubes]
#
# # Generate all possible sets of 8 cubes
# sets = list(itertools.product(*groups))
#
# # Print the total number of sets generated
# print("Total sets generated:", len(sets))
#
# # Print the first 10 sets
# for i in range(10):
#     print("Set", i+1, ":", sets[i])
# print(len(sets))
#------------------
# Generate all possible swaps
swaps = list(permutations(range(8), 2))

# Generate all possible sets of cubes
sets_of_cubes = []
for i in range(len(cubes)):
    for j in range(i + 1, len(cubes)):
        for k in range(j + 1, len(cubes)):
            for l in range(k + 1, len(cubes)):
                for m in range(l + 1, len(cubes)):
                    for n in range(m + 1, len(cubes)):
                        for o in range(n + 1, len(cubes)):
                            for p in range(o + 1, len(cubes)):
                                new_set = [cubes[i], cubes[j], cubes[k], cubes[l], cubes[m], cubes[n], cubes[o], cubes[p]]
                                for swap in swaps:
                                    i, j = swap
                                    new_set[i] = new_set[i][:5] + new_set[j][5]
                                    new_set[j] = new_set[j][:5] + new_set[i][5]
                                    print(new_set)
                                    if new_set not in sets_of_cubes:
                                        sets_of_cubes.append(new_set)

# Print the number of possible sets of cubes
print(len(sets_of_cubes))