c = 0
data_w = ""
find_list = ["花店", "花卉", "鮮花", "盆栽", "園藝"]
with open("Business_r_with_flower.csv", "r", encoding="utf-8") as f:
    data = f.readline()
    while data != "":
        data = f.readline()
        if any(item in data for item in find_list):
            data_w = data_w + data
            c = c + 1

        if ((c+1) % 100) == 0:
            with open("flower_b_data_2.csv", "a", encoding="utf-8") as fr:
                fr.write(data_w)
                data_w = ""

                print("data_saved")
    with open("flower_b_data_2.csv", "a", encoding="utf-8") as fr:
        fr.write(data)
