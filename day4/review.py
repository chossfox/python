print("------------------------------------------")
"""
function: input: 1 | output: None
del, remove -> function
del: python 모든 자료형에 쓰일 수 있는 함수
remove: list만 쓰이는 함수
"""
list1 = [1, 1, 2, 3, 4, 5, 6, 4, 5, 6, 4, 5, 6]
print(list1)
# [1, 2, 3, 4, 5, 6, 4, 5, 6, 4, 5, 6]
print(list1.remove(1))
# None
print(list1)
# [2, 3, 4, 5, 6, 4, 5, 6, 4, 5, 6]
print(list1.remove(1))
# ValueError: list.remove(x): x not in list
print(list1)
print(len(list1))
# 11
print(list1.count(4))
# 3
print("------------------------------------------")
if 10 in list1:
    pass
elif 11 in list1:
    pass
elif 12 in list1:
    pass
elif 13 in list1:
    pass
else:
    pass

print("------------------------------------------")
val1 = 10
if val1 < 10:
    print("down")
elif val1 > 10:
    print("up")
else:
    print("10")
    # 10