import os
import shutil
from itertools import combinations
from copy import deepcopy


def read_cubes(file_path):
    with open(file_path, "r") as file:
        return [line.strip().split('\t') for line in file.readlines()]


def is_valid_cube(cube):
    return len(set(cube)) == len(cube)


def generate_swapped_cubes(cubes):
    unique_cubes = set()
    num_cubes = len(cubes)

    for i, j in combinations(range(num_cubes), 2):  # Select two different cubes
        for a in range(6):  # Each letter in cube i
            for b in range(6):  # Each letter in cube j
                new_cubes = deepcopy(cubes)
                # Swap letters
                new_cubes[i][a], new_cubes[j][b] = new_cubes[j][b], new_cubes[i][a]

                # Ensure all rows remain unique
                if all(is_valid_cube(cube) for cube in new_cubes):
                    unique_cubes.add(tuple(tuple(cube) for cube in new_cubes))

    return unique_cubes


def write_cubes_to_files(cubes, output_path):
    for idx, cube_set in enumerate(cubes):
        file_name = f"{output_path}/cub{idx + 1}.txt"
        with open(file_name, "w") as file:
            for cube in cube_set:
                file.write('\t'.join(cube) + "\n")


# File paths
datasets = ['en', 'es', 'fr', 'kz', 'ms', 'pl', 'ru', 'sl', 'tr', 'tt', 'uz']
for dataset in datasets:
    input_file = f"result/{dataset}/8cub/train_res_app1_it0"
    output_path = f"result/{dataset}/8cub/optimized"

    if os.path.exists(output_path):
        shutil.rmtree(dir)
    os.makedirs(output_path)

    # Process cubes
    cubes = read_cubes(input_file)
    generated_cubes = generate_swapped_cubes(cubes)
    write_cubes_to_files(generated_cubes, output_path)

    print(f"Generated {len(generated_cubes)} unique cube set files.")
