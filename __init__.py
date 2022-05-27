# yumshatish va ayirish belsini chiqarib tashlanadi
# 27 ta harf

letters = ['а', 'b', 'd', 'е', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'о', 'p', 'q', 'r', 's', 't',
           'u', 'v', 'x', 'y', 'ḡ', 'ō', 'ş', 'ç']

from itertools import combinations

lst = ["a", "b", "c", "d"]

k = 0
cubics = []
for i in combinations(letters, 6):
    cubics.append(i)
print(len(cubics))

k=0
for i in combinations(cubics, 8):
    print(i)
    k+=1
    if k==1:
         break;
print(k)