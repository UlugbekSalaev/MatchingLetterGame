# calculate letter frequency for a language
import operator
datasets = ['de', 'en', 'es', 'fr','kz', 'ms','pl', 'ru', 'sl', 'tr', 'tt', 'uz']
datasets = ['uz']
'''
for dataset in ["tt"]:
    with open("Dataset/letter67/words_"+dataset, encoding="utf8") as file:
        lines = file.readlines()
    words = [line.rstrip() for line in lines]
    soft = ['а', 'ә', 'е', 'и', 'о', 'ө', 'у', 'ү', 'ы']
    with open(dataset+"_new", 'w') as test_file:
        for word in words:
            if not (any(char in soft for char in word)):
                test_file.writelines(word+'\n')

exit()
'''
for dataset in datasets:
    with open("Dataset/letter67/words_"+dataset, encoding="utf8") as file:
        lines = file.readlines()
    words = [line.rstrip() for line in lines]

    words_cnt_byLetter = [0,0,0,0,0,0,0,0]  # 3,4,5,6,7

    letter_frq = {}
    for word in words:
        words_cnt_byLetter[len(word)] +=1
        for c in word:
            if c in letter_frq:
                letter_frq[c] += 1
            else:
                letter_frq[c] = 1

    letter_frq = dict(sorted(letter_frq.items(), key=operator.itemgetter(1), reverse=True))
    total = 0
    for key, value in letter_frq.items():
        # print(key,'\t', value, value*100/total)
        total += value
    # print(dataset, '\t', len(words), '\t', words_cnt_byLetter[3], '\t', words_cnt_byLetter[4], '\t', words_cnt_byLetter[5], '\t', words_cnt_byLetter[6], '\t', words_cnt_byLetter[7], '\t', total)
    print(dataset)
    for key, value in letter_frq.items():
       if value*100/total >= 5 or True:
           print(key, '\t', value, '\t', round(value*100/total, 1))
    #
    print()