# Made the function parameters be used
# Avoided Code repetition
# fixed some problems some functions


import math


def addiction(a, b):
    res = a + b
    print(f"{a} + {b} = {res}")
    return res


def subtraction(a, b):
    sub = a - b
    print(f"{a} - {b} is {sub}")
    return sub


def multiplication(a, b):
    mult = a * b
    print(f"{a} * {b} is {mult}")
    return mult


def division(a, b):
    div = a / b
    print(f"{a} / {b} is {div}")
    return div


def sen(a):
    s = math.sin(a)
    print(f"sin is {s}.")
    return s


def cos(a):
    co = math.cos(a)
    print(f"cos is {co}.")
    return co


def tang(a):
    tan = math.tan(a)
    print(f"tan is {tan}.")
    return tan


def cotan(a):
    cot = math.cos(a) / math.sin(a)
    print(f"cotan is {cot}.")
    return cot


def root(a):
    r = math.sqrt(a)
    print(f"root of {a} is {r}.")
    return r


def power(a, b):
    p = a ** b
    print(f"{a} to the power of {b} is {p}.")
    return p


def chosen_operation():
    boolean = True

    while boolean:
        choice = int(input("Please Choose Your operation: "))
        if choice < 1 or choice > 11:
            print("Invalid Option!!!")

        if choice == 1:
            values = input("Enter the values, separated by space: ").split(" ")
            a = float(values[0])
            b = float(values[1])
            addiction(a, b)
        elif choice == 2:
            values = input("Enter the values, separated by space: ").split(" ")
            a = float(values[0])
            b = float(values[1])
            subtraction(a, b)
        elif choice == 3:
            values = input("Enter the values, separated by space: ").split(" ")
            a = float(values[0])
            b = float(values[1])
            multiplication(a, b)
        elif choice == 4:
            values = input("Enter the values, separated by space: ").split(" ")
            a = float(values[0])
            b = float(values[1])
            division(a, b)
        elif choice == 5:
            a = int(input("Enter the angle: "))
            sen(a)
        elif choice == 6:
            a = int(input("Enter the angle: "))
            cos(a)
        elif choice == 7:
            a = int(input("Enter the angle: "))
            tang(a)
        elif choice == 8:
            a = int(input("Enter the angle: "))
            cotan(a)
        elif choice == 9:
            a = float(input("Enter a positive number: "))
            root(a)
        elif choice == 10:
            values = input("Enter the values, first the base and then the exponent, separate by space: ").split(" ")
            a = float(values[0])
            b = float(values[1])
            power(a, b)
        elif choice == 11:
            print("Sure thing, the program is going to stop here...")
            boolean = False


def menu():
    list_of_operations = [
        "Add",
        "Subtract",
        "Multiply",
        "Divide",
        "Calculate sin",
        "Calculate cos",
        "Calculate tan",
        "Calculate cotan",
        "Calculate square-root",
        "Calculate the power",
        "Quit"
    ]

    print("Menu: ")

    for i in range(len(list_of_operations)):
        j = i + 1
        print(f"{j}. {list_of_operations[i]}")
    print("")
    chosen_operation()


print("Basic Calculator")
print("_" * 20)
menu()
