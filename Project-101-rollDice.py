import random

data = input("Do you want to roll a dice? Type < Y > for Yes or < N > for No. Remember to avoid using SPACES.   Answer: ")

while data== "Y":
    number = random.randint(1,6)
    if number == 1: 
        print("_____")
        print("|   |")
        print("| * |")
        print("|___|")
    elif number == 2:
        print("_____")
        print("|*  |")
        print("|   |")
        print("|__*|")
    elif number == 3:
        print("_____")
        print("|*  |")
        print("| * |")
        print("|__*|")
    elif number == 4:
        print("_____")
        print("|* *|")
        print("|   |")
        print("|*_*|")
    elif number == 5:
        print("_____")
        print("|* *|")
        print("| * |")
        print("|*_*|")
    elif number == 6:
        print("_____")
        print("|* *|")
        print("|* *|")
        print("|*_*|")
    
    data = input("Do you want to roll the dice again? Type < Y > for Yes or < N > to exit. Remember to avoid using SPACES.  Answer: ")


if data == "N":
    print("Thank you for your time.")

if data != "N" or "Y":
    print("Please write only Y or N.")