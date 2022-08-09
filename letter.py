# letter analysis at the word
letters = ['a', 'b', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'ō', 'p', 'q', 'r', 's', 'c', 't', 'u',
           'v', 'x', 'y', 'z', 'ḡ']

soft = ['a', 'e', 'i', 'o', 'ō', 'u']
hard = ['b', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 'c', 't', 'v', 'x', 'y', 'z', 'ḡ']

with open("words", encoding="utf8") as file:
    lines = file.readlines()
words = [line.rstrip() for line in lines]

# for 5-letter words
cnt = 0
cnt1 = 0
cnt2 = 0
cnt3 = 0

for word in words:
    if len(word) != 5:
        continue
    if word[0] in hard and word[1] in soft and word[2] in hard and word[3] in soft and word[4] in hard:
        cnt1 += 1
    if word[0] in soft and word[1] in hard and word[2] in soft and word[3] in hard and word[4] in soft:
        cnt2 += 1
    if word[0] in hard and word[1] in soft and word[2] in hard and word[3] in hard and word[4] in soft:
        cnt3 += 1
    cnt += 1
print('5-letter words:')
print("#*#*# ", cnt1)
print("*#*#*", cnt2)
print("#*##*", cnt3)
print("Total=", cnt)

# for 4-letter words
cnt = 0
cnt1 = 0
cnt2 = 0
cnt3 = 0
cnt4 = 0

for word in words:
    if len(word) != 4:
        continue
    if word[0] in hard and word[1] in soft and word[2] in hard and word[3] in soft:
        cnt1 += 1
    if word[0] in soft and word[1] in hard and word[2] in soft and word[3] in hard:
        cnt2 += 1
    if word[0] in hard and word[1] in soft and word[2] in hard and word[3] in hard:
        cnt3 += 1
    if word[0] in soft and word[1] in hard and word[2] in hard and word[3] in soft:
        cnt4 += 1
    cnt += 1
print('4-letter words:')
print("#*#* ", cnt1)
print("*#*#", cnt2)
print("#*##", cnt3)
print("*##*", cnt4)
print("Total=", cnt)
