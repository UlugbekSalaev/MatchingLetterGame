import time
cubes_uz_vl = [['a','i','l','d','p','s'], ['i','o','m','y','j','h'], ['o','i','n','v','ḡ','t'], ['u','o','s','b','x','k'], ['e','u','h','c','r','q'], ['ō','e','t','z','l','d'], ['a','ō','k','g','m','y'], ['a','r','q','f','n','b']]
cubes_en_vl = [['a','e','n','v','z','c'],	['e','i','d','p','j','t'],	['i','o','l','w','q','h'],	['o','i','c','k','r','b'],	['u','o','t','g','s','m'],	['a','u','h','f','n','p'],	['a','r','b','y','d','g'],	['e','s','m','x','l','f']]
cubes_ru_lf = [['а','ё','к','в','ш','т'], ['ь','ю','р','п','ч','л'],['о','э','т','б','ц','н'],['е','а','л','д','ф','с'],['и','о','н','г','щ','м'],['у','е','с','й','ъ','в'],['я','и','м','х','к','п'],['ы','у','з','ж','р','д']]
cubes_sl_vl = [['e','a','r','v','h','j'], ['a','o','l','c','f','m'],['o','i','t','b','n','c'],['i','o','p','z','k','b'],['u','i','d','g','r','č'],['e','u','j','ž','l','g'],['e','n','m','č','p','h'],['a','k','s','š','d','f']]

cubes_uz_lf = [['a','o','n','z','x','q'],	['i','u','m','c','r','y'],	['o','e','t','b','l','k'],	['u','ō','q','j','s','d'],	['e','r','y','g','h','v'],	['ō','l','k','f','n','z'],	['a','s','d','p','m','b'],	['i','h','v','ḡ','t','p']	]
cubes_en_lf = [['e','o','c','f','r','v'],	['a','u','h','g','n','m'],	['i','s','b','y','l','p'],	['o','r','v','x','d','k'],	['u','n','m','z','t','w'],	['e','l','p','j','c','f'],	['a','d','k','q','h','g'],	['i','t','w','s','b','y']]
cubes_ru_vl = [['а','ю','е','э','с','ш'],	['ь','ё','е','к','б','х'],	['о','э','и','р','в','ч'],	['е','а','у','т','з','ц'],	['и','а','ы','л','г','ф'],	['у','ь','я','н','д','щ'],	['ы','о','ю','м','й','ъ'],	['я','о','ё','п','ж','б']]
cubes_sl_lf = [['e','i','j','g','r','v'],	['a','u','p','ž','l','c'],	['o','n','m','č','t','z'],	['i','k','s','š','d','b'],	['u','r','v','h','j','g'],	['e','l','c','f','p','ž'],	['a','t','z','n','m','š'],	['o','d','b','k','s','h']]

dataset="sl"
case=0
start_time = time.time()
total_time = 0
for i in range(7):
    for j in range(i+1, 8):
        cc = cubes.copy()

        for k in range(6):
            for z in range(6):
                case += 1
                # print(cubes[i], cubes[j], i, j, k, z)
                buf1 = cc[i][k]
                buf2 = cc[j][z]

                cc[i][k] = buf2
                cc[j][z] = buf1
                with open("result/test_"+dataset+"/8cub/combinations/" + str(case), "w", encoding="utf8") as file:
                    for q in range(8):
                        for w in range(6):
                            file.write(cc[q][w] + '\t')
                        file.write('\n')
total_time = total_time + (time.time() - start_time)
print(total_time/case)
print(case)
