"""
96이 들어 있는 단은 무엇인가?
"""
print()
num = 6144
for i in range(2, num + 1):
    if num % i == 0:
        print("{}단".format(i))