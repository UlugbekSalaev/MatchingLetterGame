# letter analysis at the word
dataset = "ru"
if dataset == "uz":
    letters = ['a', 'i', 'o', 'r', 'l', 's', 't', 'u', 'n', 'm', 'q', 'k', 'y', 'h', 'b', 'e', 'd', 'z', 'v', 'ō', 'p', 'f', 'g', 'j', 'ḡ', 'x', 'c']  # 'ş', 'ç'
    soft = ['a', 'i', 'o', 'u', 'e', 'ō']
    hard = ['r', 'l', 's', 't', 'n', 'm', 'q', 'k', 'y', 'h', 'b', 'd', 'z', 'v', 'p', 'f', 'g', 'j', 'ḡ', 'x', 'c']
if dataset == "en":
    letters = ['e', 'a', 's', 'o', 'r', 'l', 't', 'i', 'd', 'n', 'c', 'u', 'b', 'p', 'm', 'h', 'g', 'f', 'y', 'k', 'w', 'v', 'x', 'z', 'j', 'q']  #  english
    soft = ['e', 'a', 'o', 'i', 'u', 'y']
    hard = ['s', 'r', 'l', 't', 'd', 'n', 'c', 'b', 'p', 'm', 'h', 'g', 'f', 'k', 'w', 'v', 'x', 'z', 'j', 'q']
if dataset == "ru":
    letters = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я', 'ь', 'б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ']  #  russian
    soft = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я', 'ь']
    hard = ['б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ']

with open("words_"+dataset, encoding="utf8") as file:
    lines = file.readlines()
words = [line.rstrip() for line in lines]

# for 5-letter words
cnt= cnt1= cnt2= cnt3= cnt4= cnt5= cnt6= cnt7= cnt8= cnt9= cnt10= cnt11= cnt12= cnt13= cnt14= cnt15= cnt16= cnt17= cnt18= cnt19= cnt20= cnt21= cnt22= cnt23= cnt24= cnt25= cnt26= cnt27=cnt28= cnt29= cnt30= cnt31= cnt32 = 0

for word in words:
    if len(word) != 5:
        continue
    cnt += 1
    if word[0] in soft and word[1] in soft and word[2] in soft and word[3] in soft and word[4] in soft:
        cnt1 += 1
        continue
    if word[0] in soft and word[1] in soft and word[2] in soft and word[3] in soft and word[4] in hard:
        cnt2 += 1
        continue
    if word[0] in soft and word[1] in soft and word[2] in soft and word[3] in hard and word[4] in soft:
        cnt3 += 1
        continue
    if word[0] in soft and word[1] in soft and word[2] in soft and word[3] in hard and word[4] in hard:
        cnt4 += 1
        continue
    if word[0] in soft and word[1] in soft and word[2] in hard and word[3] in soft and word[4] in soft:
        cnt5 += 1
        continue
    if word[0] in soft and word[1] in soft and word[2] in hard and word[3] in soft and word[4] in hard:
        cnt6 += 1
        continue
    if word[0] in soft and word[1] in soft and word[2] in hard and word[3] in hard and word[4] in soft:
        cnt7 += 1
        continue
    if word[0] in soft and word[1] in soft and word[2] in hard and word[3] in hard and word[4] in hard:
        cnt8 += 1
        continue
    if word[0] in soft and word[1] in hard and word[2] in soft and word[3] in soft and word[4] in soft:
        cnt9 += 1
        continue
    if word[0] in soft and word[1] in hard and word[2] in soft and word[3] in soft and word[4] in hard:
        cnt10 += 1
        continue
    if word[0] in soft and word[1] in hard and word[2] in soft and word[3] in hard and word[4] in soft:
        cnt11 += 1
        continue
    if word[0] in soft and word[1] in hard and word[2] in soft and word[3] in hard and word[4] in hard:
        cnt12 += 1
        continue
    if word[0] in soft and word[1] in hard and word[2] in hard and word[3] in soft and word[4] in soft:
        cnt13 += 1
        continue
    if word[0] in soft and word[1] in hard and word[2] in hard and word[3] in soft and word[4] in hard:
        cnt14 += 1
        continue
    if word[0] in soft and word[1] in hard and word[2] in hard and word[3] in hard and word[4] in soft:
        cnt15 += 1
        continue
    if word[0] in soft and word[1] in hard and word[2] in hard and word[3] in hard and word[4] in hard:
        cnt16 += 1
        continue
    if word[0] in hard and word[1] in soft and word[2] in soft and word[3] in soft and word[4] in soft:
        cnt17 += 1
        continue
    if word[0] in hard and word[1] in soft and word[2] in soft and word[3] in soft and word[4] in hard:
        cnt18 += 1
        continue
    if word[0] in hard and word[1] in soft and word[2] in soft and word[3] in hard and word[4] in soft:
        cnt19 += 1
        continue
    if word[0] in hard and word[1] in soft and word[2] in soft and word[3] in hard and word[4] in hard:
        cnt20 += 1
        continue
    if word[0] in hard and word[1] in soft and word[2] in hard and word[3] in soft and word[4] in soft:
        cnt21 += 1
        continue
    if word[0] in hard and word[1] in soft and word[2] in hard and word[3] in soft and word[4] in hard:
        cnt22 += 1
        continue
    if word[0] in hard and word[1] in soft and word[2] in hard and word[3] in hard and word[4] in soft:
        cnt23 += 1
        continue
    if word[0] in hard and word[1] in soft and word[2] in hard and word[3] in hard and word[4] in hard:
        cnt24 += 1
        continue
    if word[0] in hard and word[1] in hard and word[2] in soft and word[3] in soft and word[4] in soft:
        cnt25 += 1
        continue
    if word[0] in hard and word[1] in hard and word[2] in soft and word[3] in soft and word[4] in hard:
        cnt26 += 1
        continue
    if word[0] in hard and word[1] in hard and word[2] in soft and word[3] in hard and word[4] in soft:
        cnt27 += 1
        continue
    if word[0] in hard and word[1] in hard and word[2] in soft and word[3] in hard and word[4] in hard:
        cnt28 += 1
        continue
    if word[0] in hard and word[1] in hard and word[2] in hard and word[3] in soft and word[4] in soft:
        cnt29 += 1
        continue
    if word[0] in hard and word[1] in hard and word[2] in hard and word[3] in soft and word[4] in hard:
        cnt30 += 1
        continue
    if word[0] in hard and word[1] in hard and word[2] in hard and word[3] in hard and word[4] in soft:
        cnt31 += 1
        continue
    if word[0] in hard and word[1] in hard and word[2] in hard and word[3] in hard and word[4] in hard:
        cnt32 += 1
        continue
print('5-letter words:')
print("***** 	", cnt1)
print("****# 	", cnt2)
print("***#* 	", cnt3)
print("***## 	", cnt4)
print("**#** 	", cnt5)
print("**#*# 	", cnt6)
print("**##* 	", cnt7)
print("**### 	", cnt8)
print("*#*** 	", cnt9)
print("*#**# 	", cnt10)
print("*#*#* 	", cnt11)
print("*#*## 	", cnt12)
print("*##** 	", cnt13)
print("*##*# 	", cnt14)
print("*###* 	", cnt15)
print("*#### 	", cnt16)
print("#**** 	", cnt17)
print("#***# 	", cnt18)
print("#**#* 	", cnt19)
print("#**## 	", cnt20)
print("#*#** 	", cnt21)
print("#*#*# 	", cnt22)
print("#*##* 	", cnt23)
print("#*### 	", cnt24)
print("##*** 	", cnt25)
print("##**# 	", cnt26)
print("##*#* 	", cnt27)
print("##*## 	", cnt28)
print("###** 	", cnt29)
print("###*# 	", cnt30)
print("####* 	", cnt31)
print("##### 	", cnt32)
print(cnt1 + cnt2 + cnt3 + cnt4 + cnt5 + cnt6 + cnt7 + cnt8 + cnt9 + cnt10 + cnt11 + cnt12 + cnt13 + cnt14+cnt15+cnt16+cnt17+cnt18+cnt19+cnt20+cnt21+cnt22+cnt23+cnt24+cnt25+cnt26+cnt27+cnt28+cnt29+cnt30+cnt31+cnt32)
print("Total=", cnt)

# for 4-letter words
cnt= cnt1= cn2= cn3= cnt4= cnt5= cnt6= cnt7= cnt8= cnt9= cnt10= cnt11= cnt12= cnt13= cnt14= cnt15= cnt16 = 0

for word in words:
    if len(word) != 4:
        continue
    cnt += 1
    if word[0] in soft and word[1] in soft and word[2] in soft and word[3] in soft:
        cnt1 += 1
        continue
    if word[0] in soft and word[1] in soft and word[2] in soft and word[3] in hard:
        cnt2 += 1
        continue
    if word[0] in soft and word[1] in soft and word[2] in hard and word[3] in soft:
        cnt3 += 1
        continue
    if word[0] in soft and word[1] in soft and word[2] in hard and word[3] in hard:
        cnt4 += 1
        continue
    if word[0] in soft and word[1] in hard and word[2] in soft and word[3] in soft:
        cnt5 += 1
        continue
    if word[0] in soft and word[1] in hard and word[2] in soft and word[3] in hard:
        cnt6 += 1
        continue
    if word[0] in soft and word[1] in hard and word[2] in hard and word[3] in soft:
        cnt7 += 1
        continue
    if word[0] in soft and word[1] in hard and word[2] in hard and word[3] in hard:
        cnt8 += 1
        continue
    if word[0] in hard and word[1] in soft and word[2] in soft and word[3] in soft:
        cnt9 += 1
        continue
    if word[0] in hard and word[1] in soft and word[2] in soft and word[3] in hard:
        cnt10 += 1
        continue
    if word[0] in hard and word[1] in soft and word[2] in hard and word[3] in soft:
        cnt11 += 1
        continue
    if word[0] in hard and word[1] in soft and word[2] in hard and word[3] in hard:
        cnt12 += 1
        continue
    if word[0] in hard and word[1] in hard and word[2] in soft and word[3] in soft:
        cnt13 += 1
        continue
    if word[0] in hard and word[1] in hard and word[2] in soft and word[3] in hard:
        cnt14 += 1
        continue
    if word[0] in hard and word[1] in hard and word[2] in hard and word[3] in soft:
        cnt15 += 1
        continue
    if word[0] in hard and word[1] in hard and word[2] in hard and word[3] in hard:
        cnt16 += 1
        print(word)
        continue
print('4-letter words:')
print("**** 	", cnt1)
print("***# 	", cnt2)
print("**#* 	", cnt3)
print("**## 	", cnt4)
print("*#** 	", cnt5)
print("*#*# 	", cnt6)
print("*##* 	", cnt7)
print("*### 	", cnt8)
print("#*** 	", cnt9)
print("#**# 	", cnt10)
print("#*#* 	", cnt11)
print("#*## 	", cnt12)
print("##** 	", cnt13)
print("##*# 	", cnt14)
print("###* 	", cnt15)
print("#### 	", cnt16)
print(cnt1 + cnt2 + cnt3 + cnt4 + cnt5 + cnt6+cnt7+cnt8+cnt9+cnt10+cnt11+cnt12+cnt13+cnt14+cnt15+cnt16)
print("Total=", cnt)

# for 3-letter words
cnt = 0
cnt1 = 0
cnt2 = 0
cnt3 = 0
cnt4 = 0
cnt5 = 0
cnt6 = 0
cnt7 = 0
cnt8 = 0

for word in words:
    if len(word) != 3:
        continue
    cnt += 1

    if word[0] in soft and word[1] in soft and word[2] in soft:
        cnt1 += 1
    if word[0] in soft and word[1] in soft and word[2] in hard:
        cnt2 += 1
    if word[0] in soft and word[1] in hard and word[2] in soft:
        cnt3 += 1
    if word[0] in soft and word[1] in hard and word[2] in hard:
        cnt4 += 1
    if word[0] in hard and word[1] in soft and word[2] in soft:
        cnt5 += 1
    if word[0] in hard and word[1] in soft and word[2] in hard:
        cnt6 += 1
    if word[0] in hard and word[1] in hard and word[2] in soft:
        cnt7 += 1
    if word[0] in hard and word[1] in hard and word[2] in hard:
        cnt8 += 1

print('3-letter words:')
print("*** 	", cnt1)
print("**# 	", cnt2)
print("*#* 	", cnt3)
print("*## 	", cnt4)
print("#** 	", cnt5)
print("#*# 	", cnt6)
print("##* 	", cnt7)
print("### 	", cnt8)
print(cnt1 + cnt2 + cnt3+cnt4+cnt5+cnt6+cnt7+cnt8)
print("Total=", cnt)
