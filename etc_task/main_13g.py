# 讀取資料
sj = ""
item_class = ["Attention", "Activity Level", "Impulsivity", "Adaptation",
              "Moods & Confidence", "Energy & Feelings", "Social Abilities", "Sensitivity & Regulation"]
item_class_des = ["注意力", "活動量", "衝動性", "適應性", "情緒與自信", "活力與情感表達", "社交性", "感覺敏感與思考調節"]
age_class_des = ["2歲~2歲11個月", "3歲~3歲11個月", "4歲~6歲11個月", "7歲~20歲11個月"]
check_item = [9, 5, 5, 3, 10, 4, 6, 9]
item_sum = []
item_count = []
item_scale = []
age_class = ["a", "b", "c", "d"]
c = -1
q = 0
with open("input.txt", "r") as f:
    rl = f.read(1)
    subject_age_class = rl
    rl = f.readline()
    while rl != "":
        rl = f.readline()
        if rl == "\n":
            item_sum.append(int(0))
            item_count.append(int(0))
            c = c + 1
            itc = 0
        else:
            if rl != "":
                item_sum[c] = item_sum[c] + int(rl)
                item_count[c] = item_count[c] + 1
                itc = itc + 1
                if int(rl) > 3 or int(rl) == 0:
                    print(item_class_des[c], "題目數值錯誤於第", itc, "題出現錯誤\n該題分數為", int(rl), "應為1~3分")
# read data and count total score
sc = age_class.index(subject_age_class)

with open("scale.txt", "r") as f2:
    scale_data = f2.read()
    data_sp = scale_data.split(sep="\n")
    for i in range(len(data_sp)):
        if i % 5 == sc+1:
            item_scale.append(int(data_sp[i].split(sep="\t")[item_sum[q]-item_count[q]]))
            q = q + 1

cognitive_social_total = item_sum[0] + item_sum[1] + item_sum[2] + item_sum[6]
emotions_regulation = sum(item_sum) - cognitive_social_total
sum_scale_raw = []
sum_item_count = []
sum_scale = []
sum_scale_raw.append(cognitive_social_total)
sum_scale_raw.append(emotions_regulation)
sum_item_count.append(item_count[0] + item_count[1] + item_count[2] + item_count[6])
sum_item_count.append(sum(item_count)-sum_item_count[0])
q = 0
with open("scale_total.txt", "r") as f4:
    scale_data = f4.read()
    data_sp = scale_data.split(sep="\n")
    for i in range(len(data_sp)):
        if i % 5 == sc+1:

            sum_scale.append(int(data_sp[i].split(sep="\t")[sum_scale_raw[q]-sum_item_count[q]]))
            q = q + 1

with open("output.txt", "w", encoding="utf-8") as f3:
    f3.write("Leiter-R Parent Rating Scale\n")
    f3.write("年齡 class:" + age_class_des[sc] + "\tclass:" + subject_age_class.upper() + "\n")
    f3.write("領域\t\t\t原始分數\t量表\t\n")
    for i in range(len(item_class)):
        f3.write("%-16s" % (item_class_des[i]))
        for j in range(9-len(item_class_des[i])):
            f3.write(" ")
        f3.write("%-3d\t\t" % (item_sum[i]))
        if item_scale[i] >= 6:
            f3.write("%-s*\t\t\t" % (item_scale[i]))
        else:
            f3.write("%-s\t\t\t" % (item_scale[i]))
        f3.write("\n")
    f3.write("量表\t\t原始總分\t量尺總分\n")
    f3.write("認知／社交功能: %3d\t\t%3s\n" % (cognitive_social_total, sum_scale[0]))
    f3.write("情緒／調節:     %3d\t\t%3s\n" % (emotions_regulation, sum_scale[1]))
    f3.write("註：標註(*)為達臨床顯著性(cutoff point<=6)")
for i in range(len(item_count)):
    if item_count[i] != check_item[i]:
        # msg = item_class_des[i], "題數錯誤，目前有:", item_count[i], "\t應有:", check_item[i]
        print(item_class_des[i], "題數錯誤，目前有:", item_count[i], "\t應有:", check_item[i])
