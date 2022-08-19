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
cnt4 = 0
cnt5 = 0
cnt6 = 0
cnt7 = 0
cnt8 = 0
cnt9 = 0
cnt10 = 0
cnt11 = 0
cnt12 = 0
cnt13 = 3
cnt14 = 3

for word in words:
    if len(word) != 5:
        continue
    cnt += 1
    if word[0] in hard and word[1] in soft and word[2] in hard and word[3] in soft and word[4] in hard:
        cnt1 += 1
        continue
    if word[0] in soft and word[1] in hard and word[2] in soft and word[3] in hard and word[4] in soft:
        cnt2 += 1
        continue
    if word[0] in hard and word[1] in soft and word[2] in hard and word[3] in hard and word[4] in soft:
        cnt3 += 1
        continue
    if word[0] in soft and word[1] in hard and word[2] in hard and word[3] in soft and word[4] in hard:
        cnt4 += 1
        continue
    if word[0] in soft and word[1] in hard and word[2] in soft and word[3] in hard and word[4] in hard:
        cnt5 += 1
        continue
    if word[0] in soft and word[1] in hard and word[2] in hard and word[3] in hard and word[4] in soft:
        cnt6 += 1
        continue
    if word[0] in hard and word[1] in soft and word[2] in hard and word[3] in hard and word[4] in hard:
        cnt7 += 1
        continue
    if word[0] in hard and word[1] in hard and word[2] in soft and word[3] in hard and word[4] in soft:
        cnt8 += 1
        continue
    if word[0] in hard and word[1] in hard and word[2] in soft and word[3] in hard and word[4] in hard:
        cnt9 += 1
        continue
    if word[0] in hard and word[1] in hard and word[2] in hard and word[3] in soft and word[4] in hard:
        cnt10 += 1
        continue
    if word[0] in hard and word[1] in soft and word[2] in soft and word[3] in hard and word[4] in hard:
        cnt11 += 1
        continue
    if word[0] in hard and word[1] in soft and word[2] in soft and word[3] in hard and word[4] in soft:
        cnt12 += 1
        continue
    if word[0] in hard and word[1] in soft and word[2] in hard and word[3] in soft and word[4] in soft:
        cnt13 += 1
        continue
    if word[0] in hard and word[1] in hard and word[2] in soft and word[3] in soft and word[4] in hard:
        cnt14 += 1
        continue

print('5-letter words:')
print("#*#*# ", cnt1)
print("*#*#*", cnt2)
print("#*##*", cnt3)
print("*##*#", cnt4)
print("*#*##", cnt5)
print("*###*", cnt6)
print("#*###", cnt7)
print("##*#*", cnt8)
print("##*##", cnt9)
print("###*#", cnt10)
print("#**##", cnt11)
print("#**#*", cnt12)
print("#*#**", cnt13)
print("##**#", cnt14)
print(cnt1 + cnt2 + cnt3 + cnt4 + cnt5 + cnt6 + cnt7 + cnt8 + cnt9 + cnt10 + cnt11 + cnt12 + cnt13 + cnt14)
print("Total=", cnt)

# for 4-letter words
cnt = 0
cnt1 = 0
cnt2 = 0
cnt3 = 0
cnt4 = 0
cnt5 = 0
cnt6 = 0

for word in words:
    if len(word) != 4:
        continue
    cnt += 1

    if word[0] in hard and word[1] in soft and word[2] in hard and word[3] in soft:
        cnt1 += 1
        continue
    if word[0] in soft and word[1] in hard and word[2] in soft and word[3] in hard:
        cnt2 += 1
        continue
    if word[0] in hard and word[1] in soft and word[2] in hard and word[3] in hard:
        cnt3 += 1
        continue
    if word[0] in soft and word[1] in hard and word[2] in hard and word[3] in soft:
        cnt4 += 1
        continue
    if word[0] in hard and word[1] in soft and word[2] in soft and word[3] in hard:
        cnt5 += 1
        continue
    if word[0] in hard and word[1] in hard and word[2] in soft and word[3] in hard:
        cnt6 += 1
        continue

print('4-letter words:')
print("#*#* ", cnt1)
print("*#*#", cnt2)
print("#*##", cnt3)
print("*##*", cnt4)
print("#**#", cnt5)
print("##*#", cnt6)
print(cnt1 + cnt2 + cnt3 + cnt4 + cnt5 + cnt6)
print("Total=", cnt)

# for 3-letter words
cnt = 0
cnt1 = 0
cnt2 = 0
cnt3 = 0
cnt4 = 0
hard1 = 0
soft1 = 0
soft_frq = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'ō': 0, 'u': 0}



for word in words:
    for letter in word:
        if letter in hard:
            hard1 += 1

        if letter in soft:
            soft1 += 1
            soft_frq[letter] += 1

    if len(word) != 3:
        continue
    if word[0] in hard and word[1] in soft and word[2] in hard:
        cnt1 += 1
    if word[0] in soft and word[1] in hard and word[2] in soft:
        cnt2 += 1
    if word[0] in soft and word[1] in hard and word[2] in hard:
        cnt3 += 1
    cnt += 1
print('3-letter words:')
print("#*#", cnt1)
print("*#*", cnt2)
print("*##", cnt3)
print(cnt1 + cnt2 + cnt3)
print("Total=", cnt)
print("Soft letters: " + str(soft1))
print("Hard letters: " + str(hard1))
print(soft_frq)