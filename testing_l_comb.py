import statistics as st
cc = 8  # number of cubes
dataset = "uz"  # [uz,en,ru,sl] new dataset [de,es,fr,kz,ms,pl,tr,tt] # 0 0 0 0 0 2 3 4

t3 = [0,0,0,0,0]
t4 = [0,0,0,0,0]
t5 = [0,0,0,0,0]
for iteration in range(1):
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
            t5[iteration] += 1

samplet = []  # sample for total
sample3 = []
sample4 = []
sample5 = []  # sample for 5-letter word

for app in range(250):#1008
    # samplet = []  # sample for total
    # sample3 = []
    # sample4 = []
    # sample5 = []  # sample for 5-letter word

    for iteration in range(1):
        words_c = []
        with open("result/test_"+dataset+"/"+str(cc)+"cub/comb_words/vl"+str(app)+"_it"+str(iteration), encoding="utf8") as file: #
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

    # if st.mean(samplet) > 92.2:
    #     # print(samplet, sample3, sample4, sample5)
    #     print(app, '\t', round(st.mean(samplet), 1), '\t', round(st.stdev(samplet),1), '\t', round(st.mean(sample3), 1), '\t', round(st.stdev(sample3),1), '\t', round(st.mean(sample4), 1), '\t', round(st.stdev(sample4),1), '\t', round(st.mean(sample5), 1), '\t', round(st.stdev(sample5),1))

print(dataset, '\t', round(max(samplet), 1),  '\t', round(st.mean(samplet), 1), '\t', round(st.pstdev(samplet),2), '\t', round(st.mean(sample3), 1), '\t', round(st.pstdev(sample3),2), '\t', round(st.mean(sample4), 1), '\t', round(st.pstdev(sample4),2), '\t', round(st.mean(sample5), 1), '\t', round(st.pstdev(sample5),2))
