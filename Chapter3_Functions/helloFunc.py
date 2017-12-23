import random

def hello():
    print('Howdy!')
    print("Howdy!!!")
    print("Hello There!")


# Argument - The value passed in the function call
# Parameter - The variable inside the function

endsep = """
The print() function has the optional parameters end and sep to specify what should
be printed at the end of its arguments and between its arguments (separating them), respectively.

Below is an example of its usage.
"""

print(endsep)

name = input("Please enter your name: ")

def hello2(name):
    print('Hello ' + name)

hello()
hello2(name)
hello2("Alice")
hello2("Bob")

print("\n")

print("Hello has " + (str(len("Hello")) + " letters in it"))

print("\n")

print('Hello')
print('World')

print("\n")

print('Hello', end=" ")
print('World')
print('cat', 'dog', 'mouse')
print('cat', 'dog', 'mouse', sep=' | ') # Using a seperator to choose how to seperate your strings


print("\n")

def plusOne(number):
    return number + 1

newnumber = (plusOne(2))
print(newnumber)

