"""
반복문(FOR)
for: start(시작), end(끝), step(증감 값)
for iterator in range(start, end, step):
"""

# 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
# start: 1
# end: 11
# step: 1

# iterator: 10
# print(iterator)
# iterator = iterator + step
# if iterator < end
print()
for index in range(1, 11, 1):
    print(index, end=" ")
    # 1 2 3 4 5 6 7 8 9 10

print()
for index in range(0, 10, 1):
    print(index + 1, end=" ")
    # 1 2 3 4 5 6 7 8 9 10

print()
for i in range(0, 10):
    print(i + 1, end=" ")
    # 1 2 3 4 5 6 7 8 9 10

print()
for i in range(10):
    print(i + 1, end=" ")
    # 1 2 3 4 5 6 7 8 9 10

print("\n\n1-----------------------------------------")
for i in range(2, 10):
    print("\n" + str(i) + ":", end=" ")
    for j in range(1, 10):
        print(j, end=" ")
        # 2: 1 2 3 4 5 6 7 8 9
        # 3: 1 2 3 4 5 6 7 8 9
        # 4: 1 2 3 4 5 6 7 8 9
        # 5: 1 2 3 4 5 6 7 8 9
        # 6: 1 2 3 4 5 6 7 8 9
        # 7: 1 2 3 4 5 6 7 8 9
        # 8: 1 2 3 4 5 6 7 8 9
        # 9: 1 2 3 4 5 6 7 8 9

print("\n\n2-----------------------------------------")
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print()

for i in range(len(list1)):
    lst = list1[i]

    print(lst, end=" ")

for lst in list1:
    print(lst, end=" ")
    # 1 2 3 4 5 6 7 8 9 10

print()