# bu dastur testni natijalarini hisoblab chiqish uchun ishlatiladi
import statistics as st

cc = 9  # cubes number 5-8

# datasets = ["es"]
datasets = ['de', 'en', 'es', 'fr','kz', 'ms','pl', 'ru', 'sl', 'tr', 'tt', 'uz']
for dataset in datasets:

    for app in range(1, 2):
        total_avg = []
        total3_avg = []
        total4_avg = []
        total5_avg = []
        total6_avg = []
        total7_avg = []
        for iteration in range(5):

            with open("Dataset/letter67_fold/"+dataset+"/test"+str(iteration), encoding="utf8") as file:  #
                lines = file.readlines()
                words_c = [line.rstrip().split(',')[0] for line in lines]

            t3 = 0
            t4 = 0
            t5 = 0
            t6 = 0
            t7 = 0
            for i in words_c:
                if len(i) == 3:
                    t3 += 1
                if len(i) == 4:
                    t4 += 1
                if len(i) == 5:
                    t5 += 1
                if len(i) == 6:
                    t6 += 1
                if len(i) == 7:
                    t7 += 1

            with open("result/"+dataset+"/"+str(cc)+"cub/test_res_app"+str(app)+"_it"+str(iteration), encoding="utf8") as file: #
                lines = file.readlines()
                words_c = [line.rstrip().split(',')[0] for line in lines]

            cnt3 = 0
            cnt4 = 0
            cnt5 = 0
            cnt6 = 0
            cnt7 = 0

            for i in words_c:
                if len(i) == 3:
                    cnt3 += 1
                if len(i) == 4:
                    cnt4 += 1
                if len(i) == 5:
                    cnt5 += 1
                if len(i) == 6:
                    cnt6 += 1
                if len(i) == 7:
                    cnt7 += 1
            # print(app, '\t', iteration, '\t', (t6+t7), '\t', t6, '\t', t7)
            # print(app, '\t', iteration, '\t', (cnt6+cnt7), '\t', cnt6, '\t', cnt7)

            # print(app, '\t', iteration, '\t', round(len(words_c) / ( t6 + t7) * 100, 1), '\t', round(cnt6 / t6 * 100, 3), '\t', round(cnt7 / t7 * 100, 3) )
            # print(app, '\t', iteration, '\t', round(len(words_c) / (t3 + t4 + t5) * 100, 1), '\t', round(cnt3 / t3 * 100, 3), '\t', round(cnt4 / t4 * 100, 3), '\t', round(cnt5 / t5 * 100, 3))

            # total_avg.append(round(len(words_c) / (t3 + t4 + t5) * 100, 1))
            total_avg.append(round(len(words_c) / ( t6 + t7) * 100, 1))

            # total3_avg.append(round(cnt3 / t3 * 100, 3))
            # total4_avg.append(round(cnt4 / t4 * 100, 3))
            # total5_avg.append(round(cnt5 / t5 * 100, 3))
            #
            total6_avg.append(round(cnt6 / t6 * 100, 3))
            total7_avg.append(round(cnt7 / t7 * 100, 3))
        # print()
        # print(dataset, '\t', max(total_avg), '\t', st.mean(total_avg), '\t', st.stdev(total_avg), '\t', st.mean(total3_avg), '\t', st.stdev(total3_avg), '\t', st.mean(total4_avg), '\t', st.stdev(total4_avg), '\t', st.mean(total5_avg), '\t', st.stdev(total5_avg))
        print(dataset, '\t', max(total_avg), '\t', st.mean(total_avg), '\t', st.stdev(total_avg), '\t', st.mean(total6_avg), '\t', st.stdev(total6_avg), '\t', st.mean(total7_avg), '\t', st.stdev(total7_avg), '\t' )
