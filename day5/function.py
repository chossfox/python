"""
function: 기능을 여러번 사용 및 수정이 편하도록 만든 것

def 함수_이름(입력 값1, 입력값2...):
    함수 내용
    return 출력 값

함수_이름(입력 값1, 입력값2...)
print()
"""


# 함수 기본 틀
# 입력값 = 파라미터 = 매개변수
# 출력값 = 리턴값
def func_basic(parameter):
    func_contents = None
    return output_value

def func_empty_parameter():
    func_contents = None
    return output_vaule

def func_empty_return(parameter):
    func_contents = None
    # 안써도되고
    # return
    # return None

def func_empty_param_return():
    func_contents = None


# 일반 구현
print()
# for i in range(2, 10):
#     for j in range(1, 10):
#         print("{} X {} = {}".format(i, j, i * j))
#         pass

# ------------------------------------------------------------

# 함수 구현 1
def gugudan(dan):
    dan_i = dan
    for i in range(2, dan_i + 1):
        if dan_i < 10:
            mul = 9
        else:
            mul = i

        for j in range(1, mul + 1):
            print("{} X {} = {}".format(i, j, i * j))


# 함수 실행 1
gugudan(9)

list1 = [1, 2, 3, 4]
result = list1.remove(1)
print(list1)
print(result)

# ------------------------------------------------------------

# 함수 구현 2
def gugudan(dan):
    if dan < 10:
        mul = 9
    else:
        mul = dan

    for j in range(1, mul + 1):
        print("{} X {} = {}".format(dan, j, dan * j))

# 함수 실행 2
# gugudan(8)
for i in range(13):
    # gugudan(i + 1)
    pass

# ------------------------------------------------------------

# 함수 구현 3
def gugudan(dan):
    result_dict = {}
    if dan < 10:
        mul = 9
    else:
        mul = dan

    for j in range(1, mul + 1):
        result_dict[j] = dan * j

    return result_dict

# 함수 실행 3
gugu_dict = {}
for i in range(13):
    # 0 <= i < 13
    # 1 <= i <= 13
    gugu_dict[i + 1] = gugudan(i + 1)

print()
print(gugu_dict[3])

# ------------------------------------------------------------