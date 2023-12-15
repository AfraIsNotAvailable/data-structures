from bit_operation import get_bit
import os


def print_menu():
    options = {
        1: "Get the ith bit from number",
        2: "Set the ith bit from number",
        3: "Clear the ith bit from number",
        4: "Update the ith bit from number",
        5: "exit",
    }
    
    os.system("clear")

    for key in options.keys():
        print(key, ". ", options[key], sep="")

    option = int(input(">> "))
    
    os.system("clear")

    if option == 1:
        print("1. Get the ith bit from number")
        num = int(input("num="))
        i = int(input("i="))
        i-=1

        if i + 1 == 1:
            ending = "st"
        elif i + 1 == 2:
            ending = "nd"
        elif i + 1 == 3:
            ending = "rd"
        else:
            ending = "th"

        output = get_bit(num, i)
        i+=1

        print(f"The {i}{ending} bit is {output}")


while True:
    print_menu()
    input()