"""
2 ~ 9단 출력

---Ex---
2 x 1 = 2
2 x 2 = 4
"""
print()
for i in range(2, 10):
    for j in range(1, 10):
        print("{} X {} = {}".format(i, j, i * j))
