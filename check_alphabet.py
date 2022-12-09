# check all letter from dataset is exist in alphabet of this language
dataset = "en"
if dataset == "uz":
    letters = ['a', 'i', 'o', 'r', 'l', 's', 't', 'u', 'n', 'm', 'q', 'k', 'y', 'h', 'b', 'e', 'd', 'z', 'v', 'ō', 'p', 'f', 'g', 'j', 'ḡ', 'x', 'c']  # 'ş', 'ç'
    soft = ['a', 'i', 'o', 'u', 'e', 'ō']
    hard = ['r', 'l', 's', 't', 'n', 'm', 'q', 'k', 'y', 'h', 'b', 'd', 'z', 'v', 'p', 'f', 'g', 'j', 'ḡ', 'x', 'c']
if dataset == "en":
    letters = ['e', 'a', 's', 'o', 'r', 'l', 't', 'i', 'd', 'n', 'c', 'u', 'b', 'p', 'm', 'h', 'g', 'f', 'y', 'k', 'w', 'v', 'x', 'z', 'j', 'q']  #  english
    soft = ['e', 'a', 'o', 'i', 'u']
    hard = ['s', 'r', 'l', 't', 'd', 'n', 'c', 'b', 'p', 'm', 'h', 'g', 'f', 'y', 'k', 'w', 'v', 'x', 'z', 'j', 'q']
if dataset == "ru":
    letters = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я', 'ь', 'б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ']  #  russian
    soft = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я', 'ь']
    hard = ['б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ']

with open("words_"+dataset, encoding="utf8") as file:
    lines = file.readlines()
words = [line.rstrip() for line in lines]

for word in words:
    for char in word:
        if char not in letters:
            print(char)
            break;