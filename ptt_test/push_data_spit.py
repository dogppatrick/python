import pandas as pd
data_in = pd.read_csv("push_data_too_big.csv", decimal=",")
all_data = []
data_c = ["uuid", "a_id", "a_data", "p_id", "push_c"]
df = pd.DataFrame(columns=data_c)
file_spit = 0
# fn = "push_data_spit" + "%03d" % (file_spit,) + ".csv"
for i in range(len(data_in)):
    a = []
    for j in range(5):
        a.append(data_in.iloc[i, j])
    # print(a)
    s = pd.Series(a, index=data_c)
    df = df.append(s, ignore_index=True)

    if (i+1) % 50000 == 0:
        fn = "push_data_spit" + "%03d" % (file_spit,) + ".csv"
        df.to_csv(fn, encoding="utf-8", index=False, mode="w")
        print(fn, "\t data saved")
        file_spit = file_spit + 1
        df = pd.DataFrame(columns=data_c)
fn = "push_data_spit" + "%03d" % (file_spit,) + ".csv"
df.to_csv(fn, encoding="utf-8", index=False, mode="w")

