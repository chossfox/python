"""
왜 쓸까? 왜 이렇게 분류 했을까?

int: 계산을 하기 위해서

str: 글자를 저장하기 위해서

list: 여러개 변수를 컨트롤하기 위해서
list(), []

dict: 여러개의 list를 컨트롤하기 위해서
dict(), {}

변수: 변하는 수
상수: 고정된 수

tuple: 여러개 상수를 컨트롤하기 위해서
tuple(), ()
"""
a = 1
b = 1
c = 1
d = 1
e = 1
f = 1
g = 1
list1 = [a, b, c, d, e, f, g]
result = list1[0]


dic = {}
dic[0] = "A"
dic[1] = {}
dic[1][0] = "B"
dic[0][4] = "C"

"""
0 | 1 2 3 4 5 6 7 8 9
-------------
2 | 2 4 6 8 10
3 | 3 6 9 12 0
4 | 4 8 0 0 0
5 | 0 0 0 0 0
6 | 0 0 0 0 0
"""
print()
print(dic)