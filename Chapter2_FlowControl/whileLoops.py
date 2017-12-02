intro = """
You can make a block of code execute over and over again with a while statement.
The code in a while clause will be executed as long as the while statement’s condition is True.
In code, a while statement always consists of the following:

    The while keyword

    A condition (that is, an expression that evaluates to True or False)

    A colon

    Starting on the next line, an indented block of code (called the while clause)

You can see that a while statement looks similar to an if statement.
The difference is in how they behave. At the end of an if clause, the program execution continues after the if statement.
But at the end of a while clause, the program execution jumps back to the start of the while statement.
The while clause is often called the while loop or just the loop.

Let’s look at an if statement and a while loop that use the same condition and take the same actions based on that condition. 
Here is the code with an if statement:

spam = 0
if spam < 5:
    print('Hello, world.')
    spam = spam + 1
    

Here is the code with a while statement:

spam = 0
while spam < 5:
    print('Hello, world.')
    spam = spam + 1
    

These statements are similar—both if and while check the value of spam, and if it’s less than five, they print a message. 
But when you run these two code snippets, something very different happens for each one. 
For the if statement, the output is simply "Hello, world.". 
But for the while statement, it’s "Hello, world." repeated five times! 
Take a look at the flowcharts for these two pieces of code, Figure 2-9 and Figure 2-10, to see why this happens.

2-9) https://automatetheboringstuff.com/images/000091.png
2-10) https://automatetheboringstuff.com/images/000094.png

The code with the if statement checks the condition, and it prints Hello, world. 
only once if that condition is true. 
The code with the while loop, on the other hand, will print it five times. 
It stops after five prints because the integer in spam is incremented by one at the end of each loop iteration, 
which means that the loop will execute five times before spam < 5 is False.

In the while loop, the condition is always checked at the start of each iteration (that is, each time the loop is executed). 
If the condition is True, then the clause is executed, and afterward, the condition is checked again. 
The first time the condition is found to be False, the while clause is skipped.


An Annoying while Loop
======================


"""


print('Difference between If statements and While Loops')
print('------------------------------------------------')
print(intro)

print('\n')
print('Sample of an If statement result')
print('--------------------------------')
spam = 0
if spam < 5:
    print('Hello World.')
    spam = spam + 1


print('\n')
print('Sample of a while loop result')
print('-----------------------------')

# --------------------------- Intro to While Loops---------------------------
spam = 0
while spam < 5: # iteration (looping) - loops 5 times and is increased by 1 each time
    print('Hello World!')
    spam = spam + 1

print('\n')

# Input Validation
name = ''
while name != 'your name':
    print ('Please type your name: ')
    name = input()
print('Thank you very much!')

print('\n')

print('My name is')
i = 0
while i < 5:
    print('Jimmy Five Times (' + str(i) + ')')
    # i += 1
    i = i + 1

# --------------------------- End Intro to While Loops---------------------------

print("\n")

# --------------------------- Using the break statement ---------------------------

isbroken = """
There is a shortcut to getting the program execution to break out of a while loop’s clause early.
If the execution reaches a break statement, it immediately exits the while loop’s clause.
In code, a break statement simply contains the break keyword.
"""

print(isbroken)
print('\n')

name = ''
while True:
    print('Please type my name.')
    name = input()
    if name == 'my name':
        break
print('Thank you!!!!!')

# --------------------------- End Using the break statement ---------------------------

print("\n")

# --------------------------- Using the continue statement ---------------------------

keepgoing = """
Like break statements, continue statements are used inside loops.
When the program execution reaches a continue statement, the program execution immediately jumps back to the start of
the loop and reevaluates the loop’s condition. (This is also what happens when the execution reaches the end of the loop.)
"""

print(keepgoing)
print('\n')

spam = 0
while spam < 5:
    spam = spam + 1
    if spam == 3:
        continue # takes you back to the start of the loop and re-check the condition
    print('spam is ' + str(spam))

print('\n')

while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue
    print('Hello, Joe. What is the password? (It is a fish.)')
    password = input()
    if password == 'swordfish':
        break
print('Access granted!')


print('\n')


"""
There are some values in other data types that conditions will consider equivalent to True and False.
When used in conditions, 0, 0.0, and '' (the empty string) are considered False, while all other values are considered True.
For example, look at the following program:
"""

name = ''
while not name:
    print('Enter your name: ')
    name = input()
print('How many guests will you have?')
numOfGuests = int(input())
if numOfGuests:
    print('Be sure to have enough room for all of your guests.')
print('Done')


"""
If the user enters a blank string for name, then the while statement’s condition will be True, and the program continues to ask for a name.
If the value for numOfGuests is not 0, then the condition is considered to be True, and the program will print a reminder for the user.

You could have typed not name != '' instead of not name, and numOfGuests != 0 instead of numOfGuests, but using the truthy
 and falsey values can make your code easier to read.
"""

# --------------------------- End Using the continue statement ---------------------------