"""
class: 함수랑 변수를 같이 컨트롤하기 위한 기능

class 클래스 명:
    def __init__(value):
        self.value = 5
        self.func1()
        return


    def func1(self):
        print(self.value)
        return
"""


class Test:
    def __init__(self, value):
        self.value = value
        value2 = 1
        return

    def func1(self):
        print(self.value)
        return


if __name__ == "__main__":
    print()
    test = Test(value=10)
    print(test.value)
    test.func1()
    "안다비".count("안")
    list1 = [1, 2, 3, 4]
    list1.remove(1)

