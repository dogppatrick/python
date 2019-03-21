b = 100000
bank = b*(1+0.2)
dpo = b
diw = b
for m in range(12):
    dpo = dpo*(1+0.1)
for day in range(365):
    diw = diw * (1+0.01)

print("bank=%f\t downpoo=%f\t disha$=%f" % (bank, dpo, diw))
