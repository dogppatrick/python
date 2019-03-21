def p(*it):
        print(it)


def p_d(**it):
    for k, v in it.items():
        print(k, ":", v)


dict1 = {'a1': 'v1', 'a2': 'v2'}
dict2 = {'a1': 'v1', 'a3': 'v3', 'a2': 'v2.0'}
dict3 = dict2
dict3["a2"] = "0000"
print(dict2)
