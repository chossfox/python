# 1. 값이 덮어씌워 지는것과 아닌것
val1 = 1
val2 = 2
"""
= 오른쪽에서 왼쪽으로 대입
ex) val1 = 1
ex) val1 += 1
ex) val1 = val1 + 1
"""
# print(val1, val2)
# 4, 1
print("------------------------------------------")
list1 = [1, 2, 3, 4, 5, 6, 4, 5, 6, 4, 5, 6]
"""
a * 3: a를 3번 반복
len: length(길이를 세는 것)
"""
print(list1 * 3)
# [1, 2, 3, 4, 5, 6, 4, 5, 6, 4, 5, 6, 1, 2, 3, 4, 5, 6, 4, 5, 6, 4, 5, 6, 1, 2, 3, 4, 5, 6, 4, 5, 6, 4, 5, 6]
print(len(list1 * 3))
# 36
print("------------------------------------------")
"""
function: input: 1 | output: None
del, remove -> function
del: python 모든 자료형에 쓰일 수 있는 함수
remove: list만 쓰이는 함수
"""
# [1, 2, 3, 4, 5, 6, 4, 5, 6, 4, 5, 6]
print(list1.remove(1))
# None
print(list1)
# [2, 3, 4, 5, 6, 4, 5, 6, 4, 5, 6]
# print(list1.remove(1))
# ValueError: list.remove(x): x not in list
print(list1)
print(len(list1))
# 11
print(list1.count(4))
# 3
print("------------------------------------------")