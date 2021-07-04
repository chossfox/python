from work2 import table
"""
6이 들어 있는 단은 무엇인가?
"""
print()
for key, values in table.items():
    for k, v in values.items():
        if v == 96:
            print("{}단".format(key))
            # print(str(key) + "단")