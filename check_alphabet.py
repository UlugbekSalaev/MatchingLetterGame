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
if dataset == "sl":
    letters = ['a', 'b', 'c', 'č', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 'š', 't', 'u', 'v', 'z', 'ž']  #  sloven
    soft = ['a', 'e', 'o', 'i', 'u']
    hard = ['b', 'c', 'č', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'r', 's', 'š', 't', 'v', 'z', 'ž']  #  english
if dataset == "fr":
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'é', 'è', 'ê', 'ë', 'ç', 'à', 'â', 'æ', 'ï', 'ô', 'û', 'œ', 'î', 'ÿ']  #  french
    soft = ['a', 'e', 'i', 'o', 'u', 'y', 'é', 'è', 'ê', 'ë', 'à', 'â', 'æ', 'ï', 'ô', 'û', 'œ', 'î', 'ÿ']
    hard = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z', 'ç']
if dataset == "tt":
    letters = ['а', 'ә', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'җ', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'ң', 'о', 'ө', 'п', 'р', 'с', 'т', 'у', 'ү', 'ф', 'х', 'һ', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']  #  tatar
    soft = ['а', 'ә', 'е', 'ё', 'и', 'о', 'ө', 'у', 'ү', 'ы']
    hard = ['б', 'в', 'г', 'д', 'ж', 'җ', 'з', 'й', 'к', 'л', 'м', 'н', 'ң', 'п', 'р', 'с', 'т', 'ф', 'х', 'һ', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ь', 'э', 'ю', 'я']
if dataset == "de":
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'ä', 'ö', 'ü', 'ß']  #  german
    soft = ['a', 'e', 'i', 'o', 'u', 'ä', 'ö', 'ü']
    hard = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z', 'ß']
if dataset == "kz":
    letters = ['ә', 'ғ', 'қ', 'ң', 'ө', 'ұ', 'ү', 'һ', 'і', 'а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я', 'ь', 'б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ']  #  german
    soft = ['ә', 'ө', 'і', 'а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я', 'ь']
    hard = ['ғ', 'қ', 'ң', 'ұ', 'ү', 'һ', 'б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ']
if dataset == "ms":
    letters = ['a',	'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']  # malay
    soft = ['a', 'e', 'i', 'o', 'u']
    hard = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
if dataset == "pl":
    letters = ['a', 'ą', 'b', 'c', 'ć', 'd', 'e', 'ę', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'ł', 'm', 'n', 'ń', 'o', 'ó', 'p', 'r', 's', 'ś', 't', 'u', 'w', 'y', 'z', 'ź', 'ż']  # polish
    soft = ['a', 'ą', 'e', 'ę', 'i', 'o', 'ó', 'u', 'y']
    hard = ['b', 'c', 'ć', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'ł', 'm', 'n', 'ń', 'p', 'r', 's', 'ś', 't', 'w', 'z', 'ź', 'ż']
if dataset == "es":
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']  # spanish
    soft = ['a', 'e', 'i',  'o', 'u']
    hard = [ 'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'ñ', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
if dataset == "tr":
    letters = ['a', 'e', 'ı', 'i', 'o', 'ö', 'u', 'ü', 'b', 'c', 'ç', 'd', 'f', 'g', 'ğ', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'r', 's', 'ş', 't', 'v', 'y', 'z']  # turkish
    soft = ['a', 'e', 'ı', 'i', 'o', 'ö', 'u', 'ü']
    hard = ['b', 'c', 'ç', 'd', 'f', 'g', 'ğ', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'r', 's', 'ş', 't', 'v', 'y', 'z']

with open("dataset_prep/words_"+dataset, encoding="utf8") as file:
    lines = file.readlines()
words = [line.rstrip() for line in lines]

f = open("dataset_prep/words_done_"+dataset, "w", encoding="utf8")

for word in words:
    w = True
    for char in word:
        if char not in letters:
            print(char)
            w = False
            break;
    # if w and 2 < len(word) < 6:
    if w and 5 < len(word) < 8:
        f.write(word+"\n")
f.close()

