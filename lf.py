# calculate letter frequency for a language
import operator
# dataset= "fr"

for dataset in ["de", "fr", "ms", "pl", "kz", "tr", "tt", "es"]:
    print(dataset)
    with open("Dataset/words_"+dataset, encoding="utf8") as file:
        lines = file.readlines()
    words = [line.rstrip() for line in lines]
    letter_frq = {}
    for word in words:
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
    print(total)
    for key, value in letter_frq.items():
        if value*100/total >= 5 or True:
            print(key, '\t', value, round(value*100/total, 1))

