from work2 import table
"""
출력 시 단마다 구분자 생성

---Ex---
2 x 9 = 18
-----------------------------
3 x 1 = 3

"""
print()
for key, values in table.items():
    for k, v in values.items():
        print("{} X {}  = {}".format(key, k , v))

    print("-----------")