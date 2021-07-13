from os import system
import math


def clear():
    system("cls")
    print()

def show_cmd(current_data):
    clear()
    print("_" * 25)
    print("|{0:>23}|".format(current_data))

    print("_" * 25)
    print("|{0:^5}".format("%"), end="")
    print("|{0:^5}".format("CE"), end="")
    print("|{0:^5}".format("C"), end="")
    print("|{0:^5}|".format("Del"))

    print("_" * 25)
    print("|{0:^5}".format("1/x"), end="")
    print("|{0:^5}".format("Pow"), end="")
    print("|{0:^5}".format("Sqrt"), end="")
    print("|{0:^5}|".format("/"))

    print("_" * 25)
    print("|{0:^5}".format("7"), end="")
    print("|{0:^5}".format("8"), end="")
    print("|{0:^5}".format("9"), end="")
    print("|{0:^5}|".format("X"))

    print("_" * 25)
    print("|{0:^5}".format("4"), end="")
    print("|{0:^5}".format("5"), end="")
    print("|{0:^5}".format("6"), end="")
    print("|{0:^5}|".format("-"))

    print("_" * 25)
    print("|{0:^5}".format("1"), end="")
    print("|{0:^5}".format("2"), end="")
    print("|{0:^5}".format("3"), end="")
    print("|{0:^5}|".format("+"))

    print("_" * 25)
    print("|{0:^5}".format("+/-"), end="")
    print("|{0:^5}".format("0"), end="")
    print("|{0:^5}".format("."), end="")
    print("|{0:^5}|".format("="))

    print("_" * 25)


