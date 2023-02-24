import math

type = input("How would you like to calculate? (*,/,+,-)")

if type == "*":
    firstInteger = input("First integer: ")
    secondInteger = input("Second integer: ")
    ans = int(firstInteger)*int(secondInteger)
    print(f"Your answer is {ans}")
elif type == "/":
    firstInteger = input("First integer: ")
    secondInteger = input("Second integer(divider): ")
    ans = int(firstInteger)/int(secondInteger)
    print(f"Your answer is {ans}")
elif type == "+":
    firstInteger = input("First integer: ")
    secondInteger = input("Second integer: ")
    ans = int(firstInteger)+int(secondInteger)
    print(f"Your answer is {ans}")
elif type == "-":
    firstInteger = input("First integer: ")
    secondInteger = input("Second integer(subtractor): ")
    ans = int(firstInteger)/int(secondInteger)
    print(f"Your answer is {ans}")
else:
    print("Please enter a valid input (*,/,+,-)")
