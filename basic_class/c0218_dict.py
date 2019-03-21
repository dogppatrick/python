f1 = open("data01.txt", "r", encoding="utf-8")
context = f1.read()
f1.close()
result = {}
for c in context:
    if c in result:
        result[c] = result[c] + 1
    else:
        result[c] = 1
print(result)
