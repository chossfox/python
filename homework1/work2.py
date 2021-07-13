"""
구구단을 딕셔너리에 담기
"""
table = {}
for i in range(2, 10):
    table[i] = {}
    for j in range(1, 10):
        table[i][j] = i * j

if __name__ == "__main__":
    print()
    for key, values in table.items():
        print(key, values)