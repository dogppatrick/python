item_class_des = ["注意力", "活動量", "衝動性", "適應性", "情緒與自信", "活力與情感表達", "社交性", "感覺敏感與思考調節"]
for item in item_class_des:
    print("%20s" % item, end="")
    for j in range(15-len(item)):
        print(" ", end="")
    print(len(item))
