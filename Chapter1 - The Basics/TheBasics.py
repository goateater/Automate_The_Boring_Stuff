expressions_sample = 2 + 2
print ('2 + 2 = ', + expressions_sample)
print (type(expressions_sample))
print("\n")
print("In Python, '2 + 2' is called an expression, Its the most basic kind of programming instruction in the Python language.")
print("The values of expressions are the operands or the 2's, and the operands, which a few examples would be... + - * and so on, values and operands always evaluate to a result")

print("\n")

print('Alice ' * 5)
print("Variables")
spam = 40
eggs = 2

print(spam + eggs + spam)
print(spam + 2)


error_messages = """
If you want to know more about an error message, you can search for the exact message text online to find out more about that specific error.
You can also check out the resources at http://nostarch.com/automatestuff/ to see a list of common Python error messages and their meanings.

"""

print(error_messages)
print("\n")

print('Hello World!')
print("My first program")
print("----------------")
# This program says hello and asks for my name.

myName = input('What is your name? ')
myNameLength = (len(myName))
print('It is good to meet you, ' + myName.capitalize())
print('The length of your name is ' +str(myNameLength) + ' letters long')
myAge = input('What is your age? ')
print('You will be ' +str((int(myAge)) + 1) + ' in a year ' + myName.capitalize() + '.')
print('You will be ' +str(int(myAge) +1) + 'in a year.')
print('You will be ' + str(int('4') + 1) + ' in a year.')
print('You will be ' + str(   4+1   ) + ' in a year.')
print('You will be ' + str(5) + ' in a year.')
print('You will be ' + '5' + 'in a year.')
print('You will be 5' + 'in a year.')
print('You will be 5 in a year')


print("\n")

print("String, Int's, and Floats... Oh My!")
print("-----------------------------------")
print (str(0))
print(str(-3.14))
print(int('42'))
print(int(-99))
print(int(1.25))
print(int(1.99))
print(float('3.14'))
print(float(10))

print("\n")

print('round function')
print('--------------')
print('More information on the function can be found here:  https://www.tutorialspoint.com/python/number_round.htm')
print("round(80.23456, 2) : ", round(80.23456,2))
print ("round(100.000056, 3) : ", round(100.000056, 3))
print("round(-100.000056, 3) : ", round(-100.000056, 3))



