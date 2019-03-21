import random
win = 0
lose = 0
total = 10000
d = 4
wd = 1
for i in range(total):
    door = ["w"]*wd + ["l"]*(d-wd)
    random.shuffle(door)
    c = random.randint(0, len(door)-1)
    door.pop(c)
    for j in range(1):
        door.remove("l")
    if door[0] == "w":
        win = win + 1
    else:
        lose = lose + 1
print("Total doors:%d\tTotal win doors:%d" % (d, wd))
print(win, "\t", lose, "\t", "%.3f" % (win/total*100), "%")
