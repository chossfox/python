"""
구구단을 딕셔너리에 담기


"""
print()
table = {}  # 1. 변수 만들기
for i in range(2, 97):
    table[i] = {}
    # table = {i: {}}
    # table[2] = {}
    for j in range(1, 97):
        table[i][j] = i * j
        # table = {i: {j: i * j}}
        # 2 x 1 = 2
        # table[2][1] = 2

dic1 = {"a":1, "b":2}
print(dic1.items())


if __name__ == "__main__":
    print()
    for key, values in table.items():
        print(key, values)