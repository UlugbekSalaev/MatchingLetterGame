import os
import random
from sklearn.model_selection import KFold


def process_single_dataset(file_path, output_path, num_folds=5):
    # Read and shuffle the lines
    with open(file_path, 'r') as file:
        lines = file.readlines()
    random.shuffle(lines)

    # Split lines into folds using KFold
    kf = KFold(n_splits=num_folds)
    fold_number = 1

    for train_index, test_index in kf.split(lines):
        train_lines = [lines[i] for i in train_index]
        test_lines = [lines[i] for i in test_index]

        # Remove the trailing newline from the last line
        if train_lines and train_lines[-1].endswith('\n'):
            train_lines[-1] = train_lines[-1].rstrip('\n')
        if test_lines and test_lines[-1].endswith('\n'):
            test_lines[-1] = test_lines[-1].rstrip('\n')

        # Generate output file names based on the original file name
        base_filename = os.path.basename(file_path)
        train_file_path = os.path.join(output_path, f"train{fold_number-1}")
        test_file_path = os.path.join(output_path, f"test{fold_number-1}")

        # Write the train and test files for this fold
        with open(train_file_path, 'w') as train_file:
            train_file.writelines(train_lines)
        with open(test_file_path, 'w') as test_file:
            test_file.writelines(test_lines)

        fold_number += 1
        print(f"Processed fold {fold_number - 1} for file {base_filename}")

# Running part of function
datasets = ['de', 'en', 'es', 'fr','kz', 'ms','pl', 'ru', 'sl', 'tr', 'tt', 'uz']
for dataset in datasets:
    process_single_dataset('Dataset/words_'+dataset, 'result/test_'+dataset)

# create empty directory to storing result of training
# for dt in ["de", "fr","ms", "pl", "kz", "tr", "tt", "es"]:
#     for i in ['5', '6', '7', '8']:
#         os.makedirs("result/test_"+dt+"/"+i+"cub", exist_ok=True)