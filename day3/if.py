"""
조건문
실행을 할 때 특정 조건에서만 돌아갈 수 있도록 만드는 것
function
if 조건
"""
list1 = [1, 2, 3]
if 1 in list1 \
        and 5 in list1 \
        and 6 in list1 \
        and not 0 in list1:
    print("1 in")
    # 1 in

if 0 in list1:
    print("0 in")

print("------------------------------------------")
if 4 in list1:
    pass
elif 5 in list1:
    pass
elif 6 in list1:
    pass
elif 1 in list1:
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

if val1 == 10:
    print("10")
    # 10