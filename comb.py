# bu page reviewer tomonidan bildirilgan idea asosida testlash uchun yaratildi
# bajarilish ketma-ketligi: comb.py -> testing_comb**.py -> testing_l_comb.py

import collections
import time
# bu kubiklar sifatida 5-fold traindagi eng yaxshi test natijasi chiqqan kubik olingan

cubes = collections.defaultdict(dict)

'''
cubes['uz']['vl'] = [['a','i','l','d','p','s'], ['i','o','m','y','j','h'], ['o','i','n','v','ḡ','t'], ['u','o','s','b','x','k'], ['e','u','h','c','r','q'], ['ō','e','t','z','l','d'], ['a','ō','k','g','m','y'], ['a','r','q','f','n','b']]
cubes['en']['vl'] = [['a','e','n','v','z','c'],	['e','i','d','p','j','t'],	['i','o','l','w','q','h'],	['o','i','c','k','r','b'],	['u','o','t','g','s','m'],	['a','u','h','f','n','p'],	['a','r','b','y','d','g'],	['e','s','m','x','l','f']]
cubes['ru']['vl'] = [['а','ю','е','э','с','ш'],	['ь','ё','е','к','б','х'],	['о','э','и','р','в','ч'],	['е','а','у','т','з','ц'],	['и','а','ы','л','г','ф'],	['у','ь','я','н','д','щ'],	['ы','о','ю','м','й','ъ'],	['я','о','ё','п','ж','б']]
cubes['sl']['vl'] = [['e','a','r','v','h','j'], ['a','o','l','c','f','m'],['o','i','t','b','n','c'],['i','o','p','z','k','b'],['u','i','d','g','r','č'],['e','u','j','ž','l','g'],['e','n','m','č','p','h'],['a','k','s','š','d','f']]

cubes['uz']['lf'] = [['a','o','n','z','x','q'],	['i','u','m','c','r','y'],	['o','e','t','b','l','k'],	['u','ō','q','j','s','d'],	['e','r','y','g','h','v'],	['ō','l','k','f','n','z'],	['a','s','d','p','m','b'],	['i','h','v','ḡ','t','p']	]
cubes['en']['lf'] = [['e','o','c','f','r','v'],	['a','u','h','g','n','m'],	['i','s','b','y','l','p'],	['o','r','v','x','d','k'],	['u','n','m','z','t','w'],	['e','l','p','j','c','f'],	['a','d','k','q','h','g'],	['i','t','w','s','b','y']]
cubes['ru']['lf'] = [['а','ё','к','в','ш','т'], ['ь','ю','р','п','ч','л'],['о','э','т','б','ц','н'],['е','а','л','д','ф','с'],['и','о','н','г','щ','м'],['у','е','с','й','ъ','в'],['я','и','м','х','к','п'],['ы','у','з','ж','р','д']]
cubes['sl']['lf'] = [['e','i','j','g','r','v'],	['a','u','p','ž','l','c'],	['o','n','m','č','t','z'],	['i','k','s','š','d','b'],	['u','r','v','h','j','g'],	['e','l','c','f','p','ž'],	['a','t','z','n','m','š'],	['o','d','b','k','s','h']]

# 0 0 0 0 0 2 3 4
cubes['de']['lf'] = [ ['e', 'i', 'g', 'w', 'y', 'h'], ['i', 'e', 's', 'k', 'q', 'd'], ['a', 'u', 'h', 'f', 'x', 'l'], ['u', 'a', 'd', 'z', 'n', 'b'], ['o', 'n', 'l', 'p', 't', 'm'], ['ü', 'o', 'c', 'v', 'r', 'w'], ['ä', 't', 'b', 'j', 'g', 'k'],  ['ö', 'r', 'm', 'ß', 's', 'f'] ]
cubes['es']['lf'] = [ ['a', 'i', 'm', 'z', 's', 'g'], ['o', 'u', 'p', 'f', 'r', 'd'], ['e', 's', 'g', 'ñ', 'n', 'b'], ['i', 'r', 'd', 'q', 't', 'h'], ['u', 'n', 'b', 'y', 'c', 'v'], ['a', 't', 'h', 'x', 'l', 'j'], ['o', 'c', 'v', 'k', 'm', 'f'], ['e', 'l', 'j', 'w', 'p', 'y'] ]
cubes['fr']['lf'] = [ ['a', 'i', 'm', 'h', 'n', 'g'], ['e', 'o', 'd', 'k', 'r', 'v'], ['i', 'u', 's', 'f', 'l', 'p'], ['o', 'y', 'c', 'j', 't', 'b'], ['u', 'n', 'g', 'z', 'm', 'h'], ['y', 'r', 'v', 'w', 'd', 'k'], ['a', 'l', 'p', 'q', 's', 'f'], ['e', 't', 'b', 'x', 'c', 'j'] ]
cubes['kz']['lf'] = [ ['а', 'я', 'н', 'м', 'ү', 'э'], ['ы', 'ә', 'қ', 'б', 'ң', 'щ'], ['е', 'ю', 'л', 'ш', 'х', 'һ'], ['і', 'а', 'с', 'ж', 'в', 'ё'], ['у', 'ы', 'ғ', 'г', 'ф', 'ъ'], ['о', 'е', 'й', 'п', 'ь', 'р'], ['и', 'р', 'д', 'з', 'ч', 'т'], ['ө', 'т', 'к', 'ұ', 'ц', 'н'] ]
cubes['ms']['lf'] = [ ['a', 'u', 'p', 'c', 'r', 'd'], ['i', 'o', 'm', 'y', 'l', 'h'], ['e', 'n', 'b', 'f', 't', 'g'], ['u', 'r', 'd', 'v', 'k', 'w'], ['o', 'l', 'h', 'z', 's', 'j'], ['a', 't', 'g', 'q', 'p', 'c'], ['i', 'k', 'w', 'x', 'm', 'y'], ['e', 's', 'j', 'n', 'b', 'f'] ]
cubes['pl']['lf'] = [ ['a', 'ę', 'k', 'ł', 'ż', 'n'], ['i', 'a', 'n', 's', 'f', 'l'], ['e', 'i', 'l', 'z', 'ć', 't'], ['o', 'e', 't', 'c', 'ś', 'd'], ['u', 'o', 'p', 'b', 'ń', 'm'], ['y', 'u', 'd', 'h', 'ź', 'w'], ['ó', 'y', 'm', 'g', 'r', 's'], ['ą', 'r', 'w', 'j', 'k', 'z'] ]
cubes['tr']['lf'] = [ ['a', 'e', 'r', 'b', 'c', 'l'], ['e', 'a', 'k', 'h', 'ğ', 't'], ['i', 'u', 'm', 'z', 'g', 'y'], ['u', 'i', 'l', 'ş', 'j', 'd'], ['ı', 'o', 't', 'v', 'n', 's'], ['o', 'ı', 'y', 'ç', 'r', 'b'], ['ü', 'n', 'd', 'p', 'k', 'z'], ['ö', 'ü', 's', 'f', 'm', 'ş'] ]
cubes['tt']['lf'] = [ ['а', 'ү', 'н', 'й', 'х', 'ц'], ['ы', 'а', 'т', 'з', 'җ', 'ъ'], ['е', 'ы', 'г', 'ш', 'э', 'щ'], ['ә', 'е', 'л', 'ч', 'ф', 'ё'], ['у', 'ә', 'с', 'п', 'ю', 'р'], ['и', 'р', 'м', 'ң', 'ь', 'к'], ['о', 'и', 'д', 'я', 'ж', 'н'], ['ө', 'к', 'б', 'в', 'һ', 'т'] ]

# 1 0 0 2 2 0 2 1
cubes['de']['vl'] = [ ['e', 'i', 'ä', 'd', 'f', 'q'], ['i', 'e', 'ü', 'h', 'z', 'g'], ['a', 'e', 'ö', 'l', 'p', 'd'], ['u', 'i', 'n', 'c', 'v', 'h'], ['o', 'a', 'r', 'b', 'ß', 'c'], ['ä', 'a', 't', 'm', 'j', 'b'], ['ü', 'u', 'g', 'w', 'x', 'f'], ['ö', 'o', 's', 'k', 'y', 'j']  ]
cubes['es']['vl'] = [ ['a', 'o', 't', 'h', 'x', 'g'], ['o', 'e', 'c', 'v', 'k', 'd'], ['e', 'i', 'l', 'j', 'w', 'b'], ['i', 'e', 'm', 'z', 'n', 'h'], ['u', 's', 'p', 'f', 'c', 'j'], ['a', 'u', 'g', 'ñ', 'l', 'f'], ['a', 'r', 'd', 'q', 'm', 'ñ'], ['o', 'n', 'b', 'y', 'p', 'k'] ]
cubes['fr']['vl'] = [ ['e', 'a', 'r', 'p', 'w', 'b'], ['a', 'i', 'n', 'c', 'x', 'p'], ['i', 'a', 'l', 'g', 'z', 'c'], ['o', 'i', 't', 'h', 'q', 'g'], ['u', 'o', 's', 'v', 'n', 'h'], ['y', 'o', 'd', 'f', 'l', 'k'], ['e', 'u', 'm', 'k', 'd', 'f'], ['e', 'y', 'b', 'j', 'm', 'a'] ]
cubes['kz']['vl'] = [ ['а', 'я', 'ә', 'й', 'п', 'ь'], ['ы', 'ә', 'р', 'ғ', 'з', 'ч'], ['е', 'ю', 'т', 'д', 'ұ', 'ц'], ['і', 'а', 'н', 'б', 'ң', 'э'], ['у', 'е', 'қ', 'м', 'ү', 'һ'], ['о', 'і', 'л', 'ш', 'х', 'щ'], ['и', 'ө', 'с', 'ж', 'в', 'ё'], ['ө', 'и', 'к', 'г', 'ф', 'ъ'] ]
cubes['ms']['vl'] = [ ['a', 'i', 'r', 'd', 'v', 'b'], ['i', 'e', 'l', 'h', 'z', 'p'], ['e', 'u', 't', 'g', 'q', 'd'], ['u', 'e', 'k', 'w', 'x', 'h'], ['o', 'u', 'm', 'c', 'n', 'g'], ['a', 'o', 's', 'j', 'l', 'c'], ['a', 'o', 'b', 'y', 'k', 'j'], ['i', 'n', 'p', 'f', 'm', 'a'] ]
cubes['pl']['vl'] = [ ['a', 'ę', 'o', 'n', 's', 'f'], ['i', 'a', 'u', 'l', 'z', 'ć'], ['e', 'a', 'y', 't', 'b', 'ś'], ['o', 'i', 'ó', 'p', 'c', 'ń'], ['u', 'i', 'ą', 'm', 'h', 'ź'], ['y', 'e', 'ę', 'd', 'j', 'b'], ['ó', 'e', 'k', 'w', 'g', 'c'], ['ą', 'o', 'r', 'ł', 'ż', 'ć']  ]
cubes['tr']['vl'] = [ ['a', 'i', 'u', 't', 'v', 'd'], ['i', 'a', 'ü', 's', 'p', 'h'], ['e', 'a', 'ö', 'y', 'ç', 'b'], ['ı', 'i', 'r', 'd', 'c', 'ç'], ['o', 'e', 'n', 'h', 'ğ', 'c'], ['u', 'e', 'k', 'b', 'f', 'ğ'], ['ü', 'ı', 'm', 'z', 'g', 'f'], ['ö', 'o', 'l', 'ş', 'j', 'g']  ]
cubes['tt']['vl'] = [ ['а', 'ө', 'ү', 'с', 'ш', 'ю'], ['е', 'а', 'ө', 'м', 'я', 'ь'], ['ы', 'е', 'к', 'д', 'ң', 'ж'], ['ә', 'ы', 'р', 'б', 'х', 'һ'], ['у', 'ә', 'н', 'п', 'в', 'ц'], ['и', 'у', 'т', 'ч', 'җ', 'ъ'], ['о', 'и', 'г', 'й', 'ф', 'щ'], ['ү', 'о', 'л', 'з', 'э', 'ё'] ]
'''
# yuqoridagilar 8 ta kubikli uchun adi
# indi pastdagialr 9 ta kubikli uchun yozib chiqamiz

cubes['de']['lf'] = [ ['e', 'i', 'g', 'w', 'y', 'h'], ['i', 'e', 's', 'k', 'q', 'd'], ['a', 'u', 'h', 'f', 'x', 'l'], ['u', 'a', 'd', 'z', 'n', 'b'], ['o', 'n', 'l', 'p', 't', 'm'], ['ü', 'o', 'c', 'v', 'r', 'w'], ['ä', 't', 'b', 'j', 'g', 'k'],  ['ö', 'r', 'm', 'ß', 's', 'f'] ]
cubes['es']['lf'] = [ ['a', 'i', 'm', 'z', 's', 'g'], ['o', 'u', 'p', 'f', 'r', 'd'], ['e', 's', 'g', 'ñ', 'n', 'b'], ['i', 'r', 'd', 'q', 't', 'h'], ['u', 'n', 'b', 'y', 'c', 'v'], ['a', 't', 'h', 'x', 'l', 'j'], ['o', 'c', 'v', 'k', 'm', 'f'], ['e', 'l', 'j', 'w', 'p', 'y'] ]
cubes['fr']['lf'] = [ ['a', 'i', 'm', 'h', 'n', 'g'], ['e', 'o', 'd', 'k', 'r', 'v'], ['i', 'u', 's', 'f', 'l', 'p'], ['o', 'y', 'c', 'j', 't', 'b'], ['u', 'n', 'g', 'z', 'm', 'h'], ['y', 'r', 'v', 'w', 'd', 'k'], ['a', 'l', 'p', 'q', 's', 'f'], ['e', 't', 'b', 'x', 'c', 'j'] ]
cubes['kz']['lf'] = [ ['а', 'я', 'н', 'м', 'ү', 'э'], ['ы', 'ә', 'қ', 'б', 'ң', 'щ'], ['е', 'ю', 'л', 'ш', 'х', 'һ'], ['і', 'а', 'с', 'ж', 'в', 'ё'], ['у', 'ы', 'ғ', 'г', 'ф', 'ъ'], ['о', 'е', 'й', 'п', 'ь', 'р'], ['и', 'р', 'д', 'з', 'ч', 'т'], ['ө', 'т', 'к', 'ұ', 'ц', 'н'] ]
cubes['ms']['lf'] = [ ['a', 'u', 'p', 'c', 'r', 'd'], ['i', 'o', 'm', 'y', 'l', 'h'], ['e', 'n', 'b', 'f', 't', 'g'], ['u', 'r', 'd', 'v', 'k', 'w'], ['o', 'l', 'h', 'z', 's', 'j'], ['a', 't', 'g', 'q', 'p', 'c'], ['i', 'k', 'w', 'x', 'm', 'y'], ['e', 's', 'j', 'n', 'b', 'f'] ]
cubes['pl']['lf'] = [ ['a', 'ę', 'k', 'ł', 'ż', 'n'], ['i', 'a', 'n', 's', 'f', 'l'], ['e', 'i', 'l', 'z', 'ć', 't'], ['o', 'e', 't', 'c', 'ś', 'd'], ['u', 'o', 'p', 'b', 'ń', 'm'], ['y', 'u', 'd', 'h', 'ź', 'w'], ['ó', 'y', 'm', 'g', 'r', 's'], ['ą', 'r', 'w', 'j', 'k', 'z'] ]
cubes['tr']['lf'] = [ ['a', 'e', 'r', 'b', 'c', 'l'], ['e', 'a', 'k', 'h', 'ğ', 't'], ['i', 'u', 'm', 'z', 'g', 'y'], ['u', 'i', 'l', 'ş', 'j', 'd'], ['ı', 'o', 't', 'v', 'n', 's'], ['o', 'ı', 'y', 'ç', 'r', 'b'], ['ü', 'n', 'd', 'p', 'k', 'z'], ['ö', 'ü', 's', 'f', 'm', 'ş'] ]
cubes['tt']['lf'] = [ ['а', 'ү', 'н', 'й', 'х', 'ц'], ['ы', 'а', 'т', 'з', 'җ', 'ъ'], ['е', 'ы', 'г', 'ш', 'э', 'щ'], ['ә', 'е', 'л', 'ч', 'ф', 'ё'], ['у', 'ә', 'с', 'п', 'ю', 'р'], ['и', 'р', 'м', 'ң', 'ь', 'к'], ['о', 'и', 'д', 'я', 'ж', 'н'], ['ө', 'к', 'б', 'в', 'һ', 'т'] ]

cubes['uz']['lf'] = [ ['a', 'o', 'n', 'q', 'r', 's'], ['i', 'o', 'g', 'b', 'd', 's'], ['o', 'u', 's', 'z', 'd', 'h'], ['u', 'e', 'h', 'v', 'l', 'm'], ['e', 'u', 'm', 'p', 'l', 'h'], ['a', 'e', 't', 'f', 'n', 'm'], ['a', 'r', 'c', 'x', 'n', 't'], ['i', 'd', 'k', 'j', 'g', 't'], ['i', 'l', 'y', 'r', 'g', 'c'] ]
cubes['en']['lf'] = [['e','o','c','f','r','v'],	['a','u','h','g','n','m'],	['i','s','b','y','l','p'],	['o','r','v','x','d','k'],	['u','n','m','z','t','w'],	['e','l','p','j','c','f'],	['a','d','k','q','h','g'],	['i','t','w','s','b','y']]
cubes['ru']['lf'] = [['а','ё','к','в','ш','т'], ['ь','ю','р','п','ч','л'],['о','э','т','б','ц','н'],['е','а','л','д','ф','с'],['и','о','н','г','щ','м'],['у','е','с','й','ъ','в'],['я','и','м','х','к','п'],['ы','у','з','ж','р','д']]
cubes['sl']['lf'] = [['e','i','j','g','r','v'],	['a','u','p','ž','l','c'],	['o','n','m','č','t','z'],	['i','k','s','š','d','b'],	['u','r','v','h','j','g'],	['e','l','c','f','p','ž'],	['a','t','z','n','m','š'],	['o','d','b','k','s','h']]

# 1 0 0 2 2 0 2 1
cubes['de']['vl'] = [ ['e', 'i', 'ä', 'd', 'f', 'q'], ['i', 'e', 'ü', 'h', 'z', 'g'], ['a', 'e', 'ö', 'l', 'p', 'd'], ['u', 'i', 'n', 'c', 'v', 'h'], ['o', 'a', 'r', 'b', 'ß', 'c'], ['ä', 'a', 't', 'm', 'j', 'b'], ['ü', 'u', 'g', 'w', 'x', 'f'], ['ö', 'o', 's', 'k', 'y', 'j']  ]
cubes['es']['vl'] = [ ['a', 'o', 't', 'h', 'x', 'g'], ['o', 'e', 'c', 'v', 'k', 'd'], ['e', 'i', 'l', 'j', 'w', 'b'], ['i', 'e', 'm', 'z', 'n', 'h'], ['u', 's', 'p', 'f', 'c', 'j'], ['a', 'u', 'g', 'ñ', 'l', 'f'], ['a', 'r', 'd', 'q', 'm', 'ñ'], ['o', 'n', 'b', 'y', 'p', 'k'] ]
cubes['fr']['vl'] = [ ['e', 'a', 'r', 'p', 'w', 'b'], ['a', 'i', 'n', 'c', 'x', 'p'], ['i', 'a', 'l', 'g', 'z', 'c'], ['o', 'i', 't', 'h', 'q', 'g'], ['u', 'o', 's', 'v', 'n', 'h'], ['y', 'o', 'd', 'f', 'l', 'k'], ['e', 'u', 'm', 'k', 'd', 'f'], ['e', 'y', 'b', 'j', 'm', 'a'] ]
cubes['kz']['vl'] = [ ['а', 'я', 'ә', 'й', 'п', 'ь'], ['ы', 'ә', 'р', 'ғ', 'з', 'ч'], ['е', 'ю', 'т', 'д', 'ұ', 'ц'], ['і', 'а', 'н', 'б', 'ң', 'э'], ['у', 'е', 'қ', 'м', 'ү', 'һ'], ['о', 'і', 'л', 'ш', 'х', 'щ'], ['и', 'ө', 'с', 'ж', 'в', 'ё'], ['ө', 'и', 'к', 'г', 'ф', 'ъ'] ]
cubes['ms']['vl'] = [ ['a', 'i', 'r', 'd', 'v', 'b'], ['i', 'e', 'l', 'h', 'z', 'p'], ['e', 'u', 't', 'g', 'q', 'd'], ['u', 'e', 'k', 'w', 'x', 'h'], ['o', 'u', 'm', 'c', 'n', 'g'], ['a', 'o', 's', 'j', 'l', 'c'], ['a', 'o', 'b', 'y', 'k', 'j'], ['i', 'n', 'p', 'f', 'm', 'a'] ]
cubes['pl']['vl'] = [ ['a', 'ę', 'o', 'n', 's', 'f'], ['i', 'a', 'u', 'l', 'z', 'ć'], ['e', 'a', 'y', 't', 'b', 'ś'], ['o', 'i', 'ó', 'p', 'c', 'ń'], ['u', 'i', 'ą', 'm', 'h', 'ź'], ['y', 'e', 'ę', 'd', 'j', 'b'], ['ó', 'e', 'k', 'w', 'g', 'c'], ['ą', 'o', 'r', 'ł', 'ż', 'ć']  ]
cubes['tr']['vl'] = [ ['a', 'i', 'u', 't', 'v', 'd'], ['i', 'a', 'ü', 's', 'p', 'h'], ['e', 'a', 'ö', 'y', 'ç', 'b'], ['ı', 'i', 'r', 'd', 'c', 'ç'], ['o', 'e', 'n', 'h', 'ğ', 'c'], ['u', 'e', 'k', 'b', 'f', 'ğ'], ['ü', 'ı', 'm', 'z', 'g', 'f'], ['ö', 'o', 'l', 'ş', 'j', 'g']  ]
cubes['tt']['vl'] = [ ['а', 'ө', 'ү', 'с', 'ш', 'ю'], ['е', 'а', 'ө', 'м', 'я', 'ь'], ['ы', 'е', 'к', 'д', 'ң', 'ж'], ['ә', 'ы', 'р', 'б', 'х', 'һ'], ['у', 'ә', 'н', 'п', 'в', 'ц'], ['и', 'у', 'т', 'ч', 'җ', 'ъ'], ['о', 'и', 'г', 'й', 'ф', 'щ'], ['ү', 'о', 'л', 'з', 'э', 'ё'] ]

cubes['uz']['vl'] = [ ['a', 'o', 'g', 'b', 'l', 'q'], ['i', 'o', 's', 'z', 'n', 'b'], ['o', 'u', 'h', 'v', 'g', 'z'], ['u', 'e', 'm', 'p', 's', 'v'], ['e', 'ō', 't', 'f', 'h', 'p'], ['a', 'r', 'c', 'x', 'm', 'f'], ['a', 'd', 'k', 'j', 't', 'x'], ['i', 'l', 'y', 'r', 'k', 'j'], ['i', 'n', 'q', 'd', 'y', 'ḡ'] ]
cubes['en']['vl'] = [['a','e','n','v','z','c'],	['e','i','d','p','j','t'],	['i','o','l','w','q','h'],	['o','i','c','k','r','b'],	['u','o','t','g','s','m'],	['a','u','h','f','n','p'],	['a','r','b','y','d','g'],	['e','s','m','x','l','f']]
cubes['ru']['vl'] = [['а','ю','е','э','с','ш'],	['ь','ё','е','к','б','х'],	['о','э','и','р','в','ч'],	['е','а','у','т','з','ц'],	['и','а','ы','л','г','ф'],	['у','ь','я','н','д','щ'],	['ы','о','ю','м','й','ъ'],	['я','о','ё','п','ж','б']]
cubes['sl']['vl'] = [['e','a','r','v','h','j'], ['a','o','l','c','f','m'],['o','i','t','b','n','c'],['i','o','p','z','k','b'],['u','i','d','g','r','č'],['e','u','j','ž','l','g'],['e','n','m','č','p','h'],['a','k','s','š','d','f']]

#dataset = "de"  # [uz,en,ru,sl] new dataset [de,es,fr,kz,ms,pl,tr,tt]
for dataset in ['uz']: # uz en ru sl    2 4
    print(dataset)
    case = 0
    start_time = time.time()
    total_time = 0
    for i in range(9):
        for j in range(i+1, 9):
            cc = cubes[dataset]['lf'].copy()

            for k in range(6):
                for z in range(6):
                    case += 1
                    # print(cubes[i], cubes[j], i, j, k, z)
                    buf1 = cc[i][k]
                    buf2 = cc[j][z]

                    cc[i][k] = buf2
                    cc[j][z] = buf1
                    with open("result_67/test_"+dataset+"/9cub/combinations/lf" + str(case), "w", encoding="utf8") as file:
                        for q in range(9): # cub count
                            for w in range(6):
                                file.write(cc[q][w] + '\t')
                            file.write('\n')
    total_time = total_time + (time.time() - start_time)
    print(total_time)  # total_time/case
    print(case)
