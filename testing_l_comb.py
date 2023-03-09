import statistics as st
cc = 8  # number of cubes
dataset = "sl"

t3 = [0,0]
t4 = [0,0]
t5 = [0,0]
for iteration in range(2):
    words_c = []
    with open("result/test_" + dataset + "/test" + str(iteration), encoding="utf8") as file:  #
        lines = file.readlines()
        words_c = [line.rstrip().split(',')[0] for line in lines]

    for i in words_c:
        if len(i) == 3:
            t3[iteration] += 1
        elif len(i) == 4:
            t4[iteration] += 1
        else:
            t5[iteration] = t5[iteration]+1

for app in range(1008):
    samplet = []
    sample3 = []
    sample4 = []
    sample5 = []  # sample for 5-fold

    for iteration in range(2):
        words_c = []
        with open("result/test_"+dataset+"/"+str(cc)+"cub/comb_words/lf"+str(app)+"_it"+str(iteration), encoding="utf8") as file: #
            lines = file.readlines()
            words_c = [line.rstrip().split(',')[0] for line in lines]
        cnt3 = 0 # total found sample
        cnt4 = 0
        cnt5 = 0
        for i in words_c:
            if len(i) == 3:
                cnt3 += 1
            elif len(i) == 4:
                cnt4 += 1
            else:
                cnt5 += 1
        # print(app, '\t', iteration, '\t', (t3+t4+t5), '\t', t3, '\t', t4, '\t', t5)
        # print(app, '\t', iteration, '\t', (cnt3+cnt4+cnt5), '\t', cnt3, '\t', cnt4, '\t', cnt5)
        # print(app, '\t', iteration, '\t', round(len(words_c) / (t3 + t4 + t5) * 100, 1), '\t', round(cnt3 / t3 * 100, 3), '\t', round(cnt4 / t4 * 100, 3), '\t', round(cnt5 / t5 * 100, 3))
        samplet.append((len(words_c) / (t3[iteration] + t4[iteration] + t5[iteration]) * 100))
        sample3.append(cnt3/t3[iteration]*100)
        sample4.append(cnt4/t4[iteration]*100)
        sample5.append(cnt5/t5[iteration]*100)

    if st.mean(samplet) > 92.2:
        # print(samplet, sample3, sample4, sample5)
        print(app, '\t', round(st.mean(samplet), 1), '\t', round(st.stdev(samplet),1), '\t', round(st.mean(sample3), 1), '\t', round(st.stdev(sample3),1), '\t', round(st.mean(sample4), 1), '\t', round(st.stdev(sample4),1), '\t', round(st.mean(sample5), 1), '\t', round(st.stdev(sample5),1))