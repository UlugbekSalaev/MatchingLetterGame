import operator
dataset="ru"
with open("words_"+dataset, encoding="utf8") as file:
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
total=0
for key, value in letter_frq.items():
    print(key,'\t', value)
    total +=value
print(total)
