import pandas as pd
data = pd.read_csv("push_count.csv", sep=",")
p_gt300 = []
for d in range(len(data)):
    push_id = data.iloc[d, 0]
    push_c = data.iloc[d, 1]
    if push_c > 300:
        p_gt300.append(push_id)
# print(p_gt120)
# print(len(p_gt120))
data_p = pd.read_csv("push_data_too_big.csv", sep=",")
push_data = []
print("===done push >120")
for d in range(len(data_p)):
    uuid = data_p.iloc[d, 0]
    p_id = data_p.iloc[d, 3]
    a = [uuid, p_id]
    if p_id in p_gt300:
        push_data.append(tuple(a))

print("=====print push_data")
for a, p_id in push_data:
    print(a, p_id)
print(len(push_data))
