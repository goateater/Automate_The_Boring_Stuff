while_intro = """

while Loop Statements (while Loops, break, and continue)
========================================================

You can make a block of code execute over and over again with a while statement.
The code in a while clause will be executed as long as the while statement’s 
condition is True. In code, a while statement always consists of the following:

* The while keyword
* A condition (that is, an expression that evaluates to True or False)
* A colon
* Starting on the next line, an indented block of code (called the while clause)

You can see that a while statement looks similar to an if statement. The difference 
is in how they behave. At the end of an if clause, the program execution continues 
after the if statement. But at the end of a while clause, the program execution 
jumps back to the start of the while statement. The while clause is often called the 
while loop or just the loop.

Let’s look at an if statement and a while loop that use the same condition and take 
the same actions based on that condition. Here is the code with an if statement:


Here is the code with an if statement:
========================================
spam = 0
if spam < 5:
    print('Hello, world.')
    spam = spam + 1


Hello, world.



Here is the code with a while statement:
========================================
spam = 0
while spam < 5:
    print('Hello, world.')
    spam = spam + 1
    
    
Hello, world.
Hello, world.
Hello, world.
Hello, world.
Hello, world.
    

These statements are similar—both if and while check the value of spam, and if it’s 
less than five, they print a message. But when you run these two code snippets, 
something very different happens for each one. For the if statement, the output is 
simply "Hello, world.". But for the while statement, it’s "Hello, world." 
repeated five times! Take a look at the flowcharts for these two pieces of code, 
Figure 2-9 and Figure 2-10, to see why this happens.


https://automatetheboringstuff.com/images/000091.png
Figure 2-9. The flowchart for the if statement code



https://automatetheboringstuff.com/images/000094.png
Figure 2-10. The flowchart for the while statement code



The code with the if statement checks the condition, and it prints Hello, world. 
only once if that condition is true. The code with the while loop, on the other hand, 
will print it five times. It stops after five prints because the integer in spam is 
incremented by one at the end of each loop iteration, which means that the loop 
will execute five times before spam < 5 is False.

In the while loop, the condition is always checked at the start of each iteration 
(that is, each time the loop is executed). If the condition is True, then the clause is 
executed, and afterward, the condition is checked again. The first time the 
condition is found to be False, the while clause is skipped.


An Annoying while Loop
======================
Here’s a small example program that will keep asking you to type, literally, your 
name. Select File▸New File to open a new file editor window, enter the following 
code, and save the file as yourName.py:

name = ''                           # (1)
while name != 'your name':          # (2)
    print('Please type your name.')
    name = input()                  # (3)
print('Thank you!')       


First, the program sets the name variable ❶ to an empty string. This is so that the 
name != 'your name' condition will evaluate to True and the program execution 
will enter the while loop’s clause ❷.


The code inside this clause asks the user to type their name, which is assigned to 
the name variable ❸. Since this is the last line of the block, the execution moves 
back to the start of the while loop and reevaluates the condition. If the value in 
name is not equal to the string 'your name', then the condition is True, and the 
execution enters the while clause again.

But once the user types your name, the condition of the while loop will be 'your 
name' != 'your name', which evaluates to False. The condition is now False, and 
instead of the program execution reentering the while loop’s clause, it skips past it 
and continues running the rest of the program ❹. Figure 2-11 shows a flowchart 
for the yourName.py program.

https://automatetheboringstuff.com/images/000097.png
Figure 2-11. A flowchart of the yourName.py program --  

Now, let’s see yourName.py in action. Press F5 to run it, and enter something 
other than your name a few times before you give the program what it wants.


Please type your name.
Al
Please type your name.
Albert
Please type your name.
%#@#%*(^&!!!
Please type your name.
your name
Thank you!


If you never enter your name, then the while loop’s condition will never be False, 
and the program will just keep asking forever. Here, the input() call lets the user 
enter the right string to make the program move on. In other programs, the 
condition might never actually change, and that can be a problem. Let’s look at 
how you can break out of a while loop.

BREAK Statements
================
There is a shortcut to getting the program execution to break out of a while loop’s 
clause early. If the execution reaches a break statement, it immediately exits the 
while loop’s clause. In code, a break statement simply contains the break keyword.

Pretty simple, right? Here’s a program that does the same thing as the previous 
program, but it uses a break statement to escape the loop. Enter the following 
code, and save the file as yourName2.py:

while True:                         # (1)
    print('Please type your name.')
    name = input()                  # (2)
    if name == 'your name':         # (3)
        break                       # (4)
print('Thank you!')     


The first line ❶ creates an infinite loop; it is a while loop whose condition is 
always True. (The expression True, after all, always evaluates down to the value 
True.) The program execution will always enter the loop and will exit it only when 
a break statement is executed. (An infinite loop that never exits is a common 
programming bug.)


Just like before, this program asks the user to type your name ❷. Now, however, 
while the execution is still inside the while loop, an if statement gets executed ❸ 
to check whether name is equal to your name. If this condition is True, the break 
statement is run ❹, and the execution moves out of the loop to print('Thank 
you!') ❺. Otherwise, the if statement’s clause with the break statement is 
skipped, which puts the execution at the end of the while loop. At this point, the 
program execution jumps back to the start of the while statement ❶ to recheck the 
condition. Since this condition is merely the True Boolean value, the execution 
enters the loop to ask the user to type your name again. See Figure 2-12 for the 
flowchart of this program.

Run yourName2.py, and enter the same text you entered for yourName.py. The 
rewritten program should respond in the same way as the original.

Figure 2-12. The flowchart for the yourName2.py program with an infinite loop. 
Note that the X path will logically never happen because the loop condition is always True.
https://automatetheboringstuff.com/images/000099.jpg

continue Statements
===================
Like break statements, continue statements are used inside loops. When the 
program execution reaches a continue statement, the program execution 
immediately jumps back to the start of the loop and reevaluates the loop’s 
condition. (This is also what happens when the execution reaches the end of the 
loop.)

Trapped in an Infinite Loop?

If you ever run a program that has a bug causing it to get stuck in an infinite loop, 
press CTRL-C. This will send a KeyboardInterrupt error to your program and 
cause it to stop immediately. To try it, create a simple infinite loop in the file 
editor, and save it as infiniteloop.py.


while True:
    print('Hello world!')
    
    
When you run this program, it will print Hello world! to the screen forever, 
because the while statement’s condition is always True. In IDLE’s interactive shell 
window, there are only two ways to stop this program: press CTRL-C or select Shell 
▸ restart Shell from the menu. CTRL-C is handy if you ever want to terminate 
your program immediately, even if it’s not stuck in an infinite loop.

Let’s use continue to write a program that asks for a name and password. Enter 
the following code into a new file editor window and save the program as 
swordfish.py.


while True:
  print('Who are you?')
  name = input()
  if name != 'Joe':       #(1)
    continue              #(2)
  print('Hello, Joe. What is the password? (It is a fish.)') 
  password = input()      #(3)
  if password == 'swordfish':
    break                 #(4)
print('Access granted.')  #(5)


If the user enters any name besides Joe ❶, the continue statement ❷ causes the 
program execution to jump back to the start of the loop. When it reevaluates the 
condition, the execution will always enter the loop, since the condition is simply 
the value True. Once they make it past that if statement, the user is asked for a 
password ❸. If the password entered is swordfish, then the break statement ❹ is 
run, and the execution jumps out of the while loop to print Access granted ❺. 

Otherwise, the execution continues to the end of the while loop, where it then 
jumps back to the start of the loop. See Figure 2-13 for this program’s flowchart.

https://automatetheboringstuff.com/images/000100.jpg
Figure 2-13. A flowchart for swordfish.py. The X path will logically never happen 
because the loop condition is always True.


“Truthy” and “Falsey” Values
============================
There are some values in other data types that conditions will consider equivalent 
to True and False. When used in conditions, 0, 0.0, and '' (the empty string) are 
considered False, while all other values are considered True. For example, look at 
the following program:

name = ''
while not name: #(1)
    print('Enter your name:')
    name = input()
print('How many guests will you have?')
numOfGuests = int(input())
if numOfGuests: #(2)
    print('Be sure to have enough room for all your guests.') #(3)
print('Done')

If the user enters a blank string for name, then the while statement’s condition will 
be True ❶, and the program continues to ask for a name. If the value for 
numOfGuests is not 0 ❷, then the condition is considered to be True, and the 
program will print a reminder for the user ❸.

You could have typed not name != '' instead of not name, and numOfGuests != 0 
instead of numOfGuests, but using the truthy and falsey values can make your code 
easier to read.


Run this program and give it some input. Until you claim to be Joe, it shouldn’t 
ask for a password, and once you enter the correct password, it should exit.

Who are you?
I'm fine, thanks. Who are you?
Who are you?
Joe
Hello, Joe. What is the password? (It is a fish.)
Mary
Who are you?
Joe
Hello, Joe. What is the password? (It is a fish.)
swordfish
Access granted.


for Loops and the range() Function (for Loops and range())
==========================================================
The while loop keeps looping while its condition is True (which is the reason for its 
name), but what if you want to execute a block of code only a certain number of 
times? You can do this with a for loop statement and the range() function.

In code, a for statement looks something like for i in range(5): and always 
includes the following:

* The for keyword
* A variable name
* The in keyword
* A call to the range() method with up to three integers passed to it
* A colon
* Starting on the next line, an indented block of code (called the for clause)

Let’s create a new program called fiveTimes.py to help you see a for loop in action.


print('My name is')
for i in range(5):
    print('Jimmy Five Times (' + str(i) + ')')
    
My name is
Jimmy Five Times (0)
Jimmy Five Times (1)
Jimmy Five Times (2)
Jimmy Five Times (3)
Jimmy Five Times (4)


The code in the for loop’s clause is run five times. The first time it is run, the 
variable i is set to 0. The print() call in the clause will print Jimmy Five Times 
(0). After Python finishes an iteration through all the code inside the for loop’s 
clause, the execution goes back to the top of the loop, and the for statement 
increments i by one. This is why range(5) results in five iterations through the 
clause, with i being set to 0, then 1, then 2, then 3, and then 4. The variable i will 
go up to, but will not include, the integer passed to range(). 


Figure 2-14 shows a flowchart for the fiveTimes.py program.


Figure 2-14. The flowchart for fiveTimes.py
https://automatetheboringstuff.com/images/000102.png

When you run this program, it should print Jimmy Five Times followed by the 
value of i five times before leaving the for loop.


My name is
Jimmy Five Times (0)
Jimmy Five Times (1)
Jimmy Five Times (2)
Jimmy Five Times (3)
Jimmy Five Times (4)


Note
====
You can use break and continue statements inside for loops as well. The continue 
statement will continue to the next value of the for loop’s counter, as if the 
program execution had reached the end of the loop and returned to the start. In 
fact, you can use continue and break statements only inside while and for loops. 
If you try to use these statements elsewhere, Python will give you an error.

As another for loop example, consider this story about the mathematician Karl 
Friedrich Gauss. When Gauss was a boy, a teacher wanted to give the class some 
busywork. The teacher told them to add up all the numbers from 0 to 100. Young 
Gauss came up with a clever trick to figure out the answer in a few seconds, but 
you can write a Python program with a for loop to do this calculation for you.


total = 0               #(1)
for num in range(101):  #(2)
   total = total + num  #(3)
print(total)            #(4)


The result should be 5,050. When the program first starts, the total variable is set 
to 0 ❶. The for loop ❷ then executes total = total + num ❸ 100 times. By the 
time the loop has finished all of its 100 iterations, every integer from 0 to 100 
will have been added to total. At this point, total is printed to the screen ❹. 
Even on the slowest computers, this program takes less than a second to complete.

(Young Gauss figured out that there were 50 pairs of numbers that added up to 
101: 1 + 100, 2 + 99, 3 + 98, 4 + 97, and so on, until 50 + 51. Since 50 × 101 
is 5,050, the sum of all the numbers from 0 to 100 is 5,050. Clever kid!)


An Equivalent while Loop
========================
You can actually use a while loop to do the same thing as a for loop; for loops are
just more concise. Let’s rewrite fiveTimes.py to use a while loop equivalent of a 
for loop.

print('My name is')
i = 0
while i < 5:
    print('Jimmy Five Times (' + str(i) + ')')
    i = i + 1

If you run this program, the output should look the same as the fiveTimes.py 
program, which uses a for loop.

My name is
Jimmy Five Times (0)
Jimmy Five Times (1)
Jimmy Five Times (2)
Jimmy Five Times (3)
Jimmy Five Times (4)

The Starting, Stopping, and Stepping Arguments to range()
==========================================================
Some functions can be called with multiple arguments separated by a comma, and 
range() is one of them. This lets you change the integer passed to range() to follow 
any sequence of integers, including starting at a number other than zero.


for i in range(12, 16):
    print(i)
    
The first argument will be where the for loop’s variable starts, and the second 
argument will be up to, but not including, the number to stop at.


12
13
14
15

The range() function can also be called with three arguments. The first two 
arguments will be the start and stop values, and the third will be the step 
argument. The step is the amount that the variable is increased by after each 
iteration.

for i in range(0, 10, 2):
    print(i)
    
    
So calling range(0, 10, 2) will count from zero to eight by intervals of two.


0
2
4
6
8

The range() function is flexible in the sequence of numbers it produces for for 
loops. For example (I never apologize for my puns), you can even use a negative 
number for the step argument to make the for loop count down instead of up.

for i in range(5, -1, -1):
    print(i)

Running a for loop to print i with range(5, -1, -1) should print from five down 
to zero.


5
4
3
2
1
0

Importing Modules
=================
All Python programs can call a basic set of functions called built-in functions, 
including the print(), input(), and len() functions you’ve seen before. Python 
also comes with a set of modules called the standard library. Each module is a 
Python program that contains a related group of functions that can be embedded 
in your programs. For example, the math module has mathematics-related 
functions, the random module has random number–related functions, and so on.

Before you can use the functions in a module, you must import the module with an 
import statement. In code, an import statement consists of the following:

* The import keyword
* The name of the module
* Optionally, more module names, as long as they are separated by commas

Once you import a module, you can use all the cool functions of that module. Let’s 
give it a try with the random module, which will give us access to the 
random.randint() function.

Enter this code into the file editor, and save it as printRandom.py:

import random
for i in range(5):
    print(random.randint(1, 10))
    

When you run this program, the output will look something like this:


4
1
8
4
1

The random.randint() function call evaluates to a random integer value between 
the two integers that you pass it. Since randint() is in the random module, you 
must first type random. in front of the function name to tell Python to look for this 
function inside the random module.

Here’s an example of an import statement that imports four different modules:

import random, sys, os, math

Now we can use any of the functions in these four modules. We’ll learn more about 
them later in the book.

from import Statements
=======================

An alternative form of the import statement is composed of the from keyword, 
followed by the module name, the import keyword, and a star; for example, 
from random import *.

With this form of import statement, calls to functions in random will not need the 
random. prefix. However, using the full name makes for more readable code, so it 
is better to use the normal form of the import statement.

Ending a Program Early with sys.exit()
======================================
The last flow control concept to cover is how to terminate the program. This 
always happens if the program execution reaches the bottom of the instructions. 
However, you can cause the program to terminate, or exit, by calling the 
sys.exit() function. Since this function is in the sys module, you have to import 
sys before your program can use it.

Open a new file editor window and enter the following code, saving it as 
exitExample.py:


import sys

while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        sys.exit()
    print('You typed ' + response + '.')
    
Run this program in IDLE. This program has an infinite loop with no break 
statement inside. The only way this program will end is if the user enters exit, 
causing sys.exit() to be called. When response is equal to exit, the program 
ends. Since the response variable is set by the input() function, the user must 
enter exit in order to stop the program.


Summary
=======
By using expressions that evaluate to True or False (also called conditions), you 
can write programs that make decisions on what code to execute and what code to 
skip. You can also execute code over and over again in a loop while a certain 
condition evaluates to True. The break and continue statements are useful if you 
need to exit a loop or jump back to the start.

These flow control statements will let you write much more intelligent programs. 
There’s another type of flow control that you can achieve by writing your own 
functions, which is the topic of the next chapter.



"""


print('Difference between If statements and While Loops')
print('------------------------------------------------')
print(while_intro)

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

print("Take a look at the Chapter 2 Practive Questions, to see if you need to review any of the topics")
# --------------------------- End Using the continue statement ---------------------------