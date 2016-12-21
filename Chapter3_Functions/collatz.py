"""
number = input("Please enter a number: ")

def collatz(number):
    number = int(number)
    if number % 2 == 0:
        print(number // 2)
    elif number % 2 == 1:
        print (3 * number + 1)

collatz(number)
"""

numberTwo = input("Please enter a number: ")

def collatzTwo(numberTwo):
    numberTwo = int(numberTwo)
    while numberTwo > 1:
        if numberTwo % 2 == 0:
            even = numberTwo // 2
            print(even)
        elif numberTwo % 2 == 1:
            odd = (3 * numberTwo) + 1
            print(odd)

print(numberTwo)

collatzTwo(numberTwo)

