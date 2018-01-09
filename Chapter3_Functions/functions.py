funkytown = """

Functions
=========
You’re already familiar with the print(), input(), and len() functions from the previous chapters. 
Python provides several builtin functions like these, but you can also write your own functions. 
A function is like a mini-program within a program.

To better understand how functions work, let’s create one. 
Type this program into the file editor and save it as helloFunc.py:

❶ def hello():
❷     print('Howdy!')
       print('Howdy!!!')
       print('Hello there.')
❸ hello()
   hello()
   hello()
   

The first line is a def statement ❶, which defines a function named hello(). 
The code in the block that follows the def statement ❷ is the body of the function. 
This code is executed when the function is called, not when the function is first defined.

The hello() lines after the function ❸ are function calls. 
In code, a function call is just the function’s name followed by parentheses, possibly with some 
number of arguments in between the parentheses. 

When the program execution reaches these calls, it will jump to the top line in the function and begin 
executing the code there. When it reaches the end of the function, the execution returns to the line that 
called the function and continues moving through the code as before.

Since this program calls hello() three times, the code in the hello() function is executed three times. 
When you run this program, the output looks like this:


Howdy!
Howdy!!!
Hello there.
Howdy!
Howdy!!!
Hello there.
Howdy!
Howdy!!!
Hello there.

A major purpose of functions is to group code that gets executed multiple times. 
Without a function defined, you would have to copy and paste this code each time, and the program would look like this:


print('Howdy!')
print('Howdy!!!')
print('Hello there.')
print('Howdy!')
print('Howdy!!!')
print('Hello there.')
print('Howdy!')
print('Howdy!!!')
print('Hello there.')
   
In general, you always want to avoid duplicating code, because if you ever decide to update the code—
if, for example, you find a bug you need to fix—you’ll have to remember to change the code everywhere you copied it.

As you get more programming experience, you’ll often find yourself deduplicating code, 
which means getting rid of duplicated or copy-and-pasted code. Deduplication makes your 
programs shorter, easier to read, and easier to update.

def Statements with Parameters
===============================
When you call the print() or len() function, you pass in values, 
called arguments in this context, by typing them between the parentheses. 

You can also define your own functions that accept arguments. 
Type this example into the file editor and save it as helloFunc2.py:

❶ def hello(name):
❷     print('Hello ' + name)

❸ hello('Alice')
  hello('Bob')
When you run this program, the output looks like this:


Hello Alice
Hello Bob

The definition of the hello() function in this program has a parameter called name 
❶. A parameter is a variable that an argument is stored in when a function is 
called. The first time the hello() function is called, it’s with the argument 'Alice' 
❸. The program execution enters the function, and the variable name is 
automatically set to 'Alice', which is what gets printed by the print() statement ❷.

One special thing to note about parameters is that the value stored in a parameter 
is forgotten when the function returns. For example, if you added print(name) 
after hello('Bob') in the previous program, the program would give you a 
NameError because there is no variable named name. This variable was destroyed 
after the function call hello('Bob') had returned, so print(name) would refer to a 
name variable that does not exist.

This is similar to how a program’s variables are forgotten when the program terminates. 
I’ll talk more about why that happens later in the chapter, when I discuss what a function’s local scope is.

Return Values and return Statements
===================================
When you call the len() function and pass it an argument such as 'Hello', the 
function call evaluates to the integer value 5, which is the length of the string you 
passed it. In general, the value that a function call evaluates to is called the return 
value of the function.

When creating a function using the def statement, you can specify what the return 
value should be with a return statement. A return statement consists of the following:

* The return keyword
* The value or expression that the function should return

When an expression is used with a return statement, the return value is what this 
expression evaluates to. For example, the following program defines a function 
that returns a different string depending on what number it is passed as an 
argument. Type this code into the file editor and save it as magic8Ball.py:

❶ import random
❷ def getAnswer(answerNumber):
❸     if answerNumber == 1:
           return 'It is certain'
       elif answerNumber == 2:
           return 'It is decidedly so'
       elif answerNumber == 3:
           return 'Yes'
       elif answerNumber == 4:
           return 'Reply hazy try again'
       elif answerNumber == 5:
           return 'Ask again later'
       elif answerNumber == 6:
           return 'Concentrate and ask again'
       elif answerNumber == 7:
           return 'My reply is no'
       elif answerNumber == 8:
           return 'Outlook not so good'
       elif answerNumber == 9:
           return 'Very doubtful'

❹ r = random.randint(1, 9)
❺ fortune = getAnswer(r)
❻ print(fortune)


When this program starts, Python first imports the random module ❶. Then the 
getAnswer() function is defined ❷. Because the function is being defined (and not 
called), the execution skips over the code in it. Next, the random.randint() 
function is called with two arguments, 1 and 9 ❹. It evaluates to a random integer 
between 1 and 9 (including 1 and 9 themselves), and this value is stored in a 
variable named r.

The getAnswer() function is called with r as the argument ❺. The program 
execution moves to the top of the getAnswer() function ❸, and the value r is stored 
in a parameter named answerNumber. Then, depending on this value in 
answerNumber, the function returns one of many possible string values. The 
program execution returns to the line at the bottom of the program that originally 
called getAnswer() ❺. The returned string is assigned to a variable named fortune, 
which then gets passed to a print() call ❻ and is printed to the screen.

Note that since you can pass return values as an argument to another function call, 
you could shorten these three lines:


r = random.randint(1, 9)
fortune = getAnswer(r)
print(fortune)

to this single equivalent line:

print(getAnswer(random.randint(1, 9)))

Remember, expressions are composed of values and operators. A function call can 
be used in an expression because it evaluates to its return value.

The None Value
==============
In Python there is a value called None, which represents the absence of a value. 
None is the only value of the NoneType data type. (Other programming languages 
might call this value null, nil, or undefined.) Just like the Boolean True and False 
values, None must be typed with a capital N.

This value-without-a-value can be helpful when you need to store something that 
won’t be confused for a real value in a variable. One place where None is used is as 
the return value of print(). The print() function displays text on the screen, but it 
doesn’t need to return anything in the same way len() or input() does. But since 
all function calls need to evaluate to a return value, print() returns None. To see 
this in action, enter the following into the interactive shell:


>>> spam = print('Hello!')
Hello!
>>> None == spam
True

Behind the scenes, Python adds return None to the end of any function definition 
with no return statement. This is similar to how a while or for loop implicitly ends 
with a continue statement. Also, if you use a return statement without a value 
(that is, just the return keyword by itself), then None is returned.


Keyword Arguments and print()
=============================
Most arguments are identified by their position in the function call. For example, 
random.randint(1, 10) is different from random.randint(10, 1). The function call 
random.randint(1, 10) will return a random integer between 1 and 10, because the 
first argument is the low end of the range and the second argument is the high end 
(while random.randint(10, 1) causes an error).

However, keyword arguments are identified by the keyword put before them in 
the function call. Keyword arguments are often used for optional parameters. For 
example, the print() function has the optional parameters end and sep to specify 
what should be printed at the end of its arguments and between its arguments 
(separating them), respectively.

If you ran the following program:

print('Hello')
print('World')
the output would look like this:

Hello
World

The two strings appear on separate lines because the print() function 
automatically adds a newline character to the end of the string it is passed. 
However, you can set the end keyword argument to change this to a different 
string. For example, if the program were this:


print('Hello', end='')
print('World')
the output would look like this:


HelloWorld

The output is printed on a single line because there is no longer a new-line printed 
after 'Hello'. Instead, the blank string is printed. This is useful if you need to 
disable the newline that gets added to the end of every print() function call.

Similarly, when you pass multiple string values to print(), the function will 
automatically separate them with a single space. Enter the following into the 
interactive shell:

>>> print('cats', 'dogs', 'mice')
cats dogs mice

But you could replace the default separating string by passing the sep keyword 
argument. Enter the following into the interactive shell:


>>> print('cats', 'dogs', 'mice', sep=',')
cats,dogs,mice


You can add keyword arguments to the functions you write as well, but first you’ll 
have to learn about the list and dictionary data types in the next two chapters. For 
now, just know that some functions have optional keyword arguments that can be 
specified when the function is called.

Local and Global Scope
======================
Parameters and variables that are assigned in a called function are said to exist in 
that function’s local scope. Variables that are assigned outside all functions are 
said to exist in the global scope. A variable that exists in a local scope is called a 
local variable, while a variable that exists in the global scope is called a global 
variable. A variable must be one or the other; it cannot be both local and global.

Think of a scope as a container for variables. When a scope is destroyed, all the 
values stored in the scope’s variables are forgotten. There is only one global scope, 
and it is created when your program begins. When your program terminates, the 
global scope is destroyed, and all its variables are forgotten. Otherwise, the next 
time you ran your program, the variables would remember their values from the 
last time you ran it.

A local scope is created whenever a function is called. Any variables assigned in 
this function exist within the local scope. When the function returns, the local 
scope is destroyed, and these variables are forgotten. The next time you call this 
function, the local variables will not remember the values stored in them from the 
last time the function was called.

Scopes matter for several reasons:
----------------------------------
* Code in the global scope cannot use any local variables.
* However, a local scope can access global variables.
* Code in a function’s local scope cannot use variables in any other local scope.
* You can use the same name for different variables if they are in different 
scopes. That is, there can be a local variable named spam and a global variable 
also named spam.

The reason Python has different scopes instead of just making everything a global 
variable is so that when variables are modified by the code in a particular call to a 
function, the function interacts with the rest of the program only through its 
parameters and the return value. This narrows down the list code lines that may 
be causing a bug. If your program contained nothing but global variables and had 
a bug because of a variable being set to a bad value, then it would be hard to track 
down where this bad value was set. It could have been set from anywhere in the 
program—and your program could be hundreds or thousands of lines long! But if 
the bug is because of a local variable with a bad value, you know that only the code 
in that one function could have set it incorrectly.

While using global variables in small programs is fine, it is a bad habit to rely on 
global variables as your programs get larger and larger.

Local Variables Cannot Be Used in the Global Scope
==================================================
Consider this program, which will cause an error when you run it:


def spam():
    eggs = 31337

spam()
print(eggs)



If you run this program, the output will look like this:


Traceback (most recent call last):
  File "C:/test3784.py", line 4, in <module>
    print(eggs)
NameError: name 'eggs' is not defined


The error happens because the eggs variable exists only in the local scope created 
when spam() is called. Once the program execution returns from spam, that local 
scope is destroyed, and there is no longer a variable named eggs. So when your 
program tries to run print(eggs), Python gives you an error saying that eggs is not 
defined. This makes sense if you think about it; when the program execution is in 
the global scope, no local scopes exist, so there can’t be any local variables. This is 
why only global variables can be used in the global scope.

Local Scopes Cannot Use Variables in Other Local Scopes
=======================================================
A new local scope is created whenever a function is called, including when a 
function is called from another function. Consider this program:


  def spam():
❶    eggs = 99
❷    bacon()
❸    print(eggs)

  def bacon():
      ham = 101
❹    eggs = 0

❺ spam()


When the program starts, the spam() function is called ❺, and a local scope is created. 
The local variable eggs ❶ is set to 99. Then the bacon() function is called ❷, and a 
second local scope is created. Multiple local scopes can exist at the same time. 

In this new local scope, the local variable ham is set to 101, and a local variable eggs—which 
is different from the one in spam()’s local scope—is also created ❹ and set to 0.

When bacon() returns, the local scope for that call is destroyed. The program execution continues 
in the spam() function to print the value of eggs ❸, and since the local scope for the call to spam() 
still exists here, the eggs variable is set to 99. This is what the program prints.

The upshot is that local variables in one function are completely separate from the local variables in another function.

Global Variables Can Be Read from a Local Scope
===============================================
Consider the following program:

def spam():
    print(eggs)
eggs = 42
spam()
print(eggs)

Since there is no parameter named eggs or any code that assigns eggs a value in 
the spam() function, when eggs is used in spam(), Python considers it a reference to 
the global variable eggs. This is why 42 is printed when the previous program is run.

Local and Global Variables with the Same Name
=============================================
To simplify your life, avoid using local variables that have the same name as a 
global variable or another local variable. But technically, it’s perfectly legal to do so 
in Python. To see what happens, type the following code into the file editor and 
save it as sameName.py:

def spam():
❶     eggs = 'spam local'
       print(eggs) # prints 'spam local'
   def bacon():

❷     eggs = 'bacon local'
       print(eggs) # prints 'bacon local'
       spam()
       print(eggs) # prints 'bacon local'

❸ eggs = 'global'
   bacon()
   print(eggs) # prints 'global'
When you run this program, it outputs the following:


bacon local
spam local
bacon local
global

There are actually three different variables in this program, but confusingly they 
are all named eggs. The variables are as follows:

❶ A variable named eggs that exists in a local scope when spam() is called.

❷ A variable named eggs that exists in a local scope when bacon() is called.

❸ A variable named eggs that exists in the global scope.

Since these three separate variables all have the same name, it can be confusing to 
keep track of which one is being used at any given time. This is why you should 
avoid using the same variable name in different scopes.

The Global Statement
====================
If you need to modify a global variable from within a function, use the global 
statement. If you have a line such as global eggs at the top of a function, it tells 
Python, “In this function, eggs refers to the global variable, so don’t create a local 
variable with this name.” For example, type the following code into the file editor 
and save it as sameName2.py:

  def spam():
❶    global eggs
❷    eggs = 'spam'

  eggs = 'global'
  spam()
  print(eggs)
  
When you run this program, the final print() call will output this: 
spam


Because eggs is declared global at the top of spam() ❶, when eggs is set to 'spam' 
❷, this assignment is done to the globally scoped eggs. No local eggs variable is created.


There are four rules to tell whether a variable is in a local scope or global scope:

1) If a variable is being used in the global scope (that is, outside of all functions), then it is always a global variable.

2) If there is a global statement for that variable in a function, it is a global variable.

3) Otherwise, if the variable is used in an assignment statement in the function, it is a local variable.

4) But if the variable is not used in an assignment statement, it is a global variable.


To get a better feel for these rules, here’s an example program. 
Type the following code into the file editor and save it as sameName3.py:

  def spam():
❶  global eggs
    eggs = 'spam' # this is the global

  def bacon():
❷  eggs = 'bacon' # this is a local
  def ham():
❸  print(eggs) # this is the global

  eggs = 42 # this is the global
  spam()
  print(eggs)

In the spam() function, eggs is the global eggs variable, because there’s a global 
statement for eggs at the beginning of the function ❶. In bacon(), eggs is a local 
variable, because there’s an assignment statement for it in that function ❷. In 
ham() ❸, eggs is the global variable, because there is no assignment statement or 
global statement for it in that function. If you run sameName3.py, the output will 
look like this:

spam

In a function, a variable will either always be global or always be local. There’s no 
way that the code in a function can use a local variable named eggs and then later 
in that same function use the global eggs variable.


Note
=====
If you ever want to modify the value stored in a global variable from in a 
function, you must use a global statement on that variable.

If you try to use a local variable in a function before you assign a value to it, as in 
the following program, Python will give you an error. To see this, type the 
following into the file editor and save it as sameName4.py:


  def spam():
      print(eggs) # ERROR!
❶    eggs = 'spam local'

❷ eggs = 'global'
   spam()
If you run the previous program, it produces an error message.


Traceback (most recent call last):
  File "C:/test3784.py", line 6, in <module>
    spam()
  File "C:/test3784.py", line 2, in spam
    print(eggs) # ERROR!
UnboundLocalError: local variable 'eggs' referenced before assignment

This error happens because Python sees that there is an assignment statement for 
eggs in the spam() function ❶ and therefore considers eggs to be local. But because 
print(eggs) is executed before eggs is assigned anything, the local variable eggs 
doesn’t exist. Python will not fall back to using the global eggs variable ❷.

Functions as “Black Boxes”

Often, all you need to know about a function are its inputs (the parameters) and 
output value; you don’t always have to burden yourself with how the function’s 
code actually works. When you think about functions in this high-level way, it’s 
common to say that you’re treating the function as a “black box.”

This idea is fundamental to modern programming. Later chapters in this book will 
show you several modules with functions that were written by other people. While 
you can take a peek at the source code if you’re curious, you don’t need to know 
how these functions work in order to use them. And because writing functions 
without global variables is encouraged, you usually don’t have to worry about the 
function’s code interacting with the rest of your program.

Exception Handling (Error Handling)
===================================
Right now, getting an error, or exception, in your Python program means the 
entire program will crash. You don’t want this to happen in real-world programs. 
Instead, you want the program to detect errors, handle them, and then continue to run.

For example, consider the following program, which has a “divide-by-zero” error. 
Open a new file editor window and enter the following code, saving it as zeroDivide.py:

def spam(divideBy):
    return 42 / divideBy

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))

We’ve defined a function called spam, given it a parameter, and then printed the 
value of that function with various parameters to see what happens. This is the 
output you get when you run the previous code:

21.0
3.5
Traceback (most recent call last):
  File "C:/zeroDivide.py", line 6, in <module>
    print(spam(0))
  File "C:/zeroDivide.py", line 2, in spam
    return 42 / divideBy
ZeroDivisionError: division by zero

A ZeroDivisionError happens whenever you try to divide a number by zero. From 
the line number given in the error message, you know that the return statement in 
spam() is causing an error.

Errors can be handled with try and except statements. The code that could 
potentially have an error is put in a try clause. The program execution moves to 
the start of a following except clause if an error happens.


You can put the previous divide-by-zero code in a try clause and have an except 
clause contain code to handle what happens when this error occurs.


def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument.')

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))

When code in a try clause causes an error, the program execution immediately 
moves to the code in the except clause. After running that code, the execution 
continues as normal. The output of the previous program is as follows:

21.0
3.5
Error: Invalid argument.
None
42.0


Note that any errors that occur in function calls in a try block will also be caught. 
Consider the following program, which instead has the spam() calls in the try block:

def spam(divideBy):
    return 42 / divideBy

try:
    print(spam(2))
    print(spam(12))
    print(spam(0))
    print(spam(1))
except ZeroDivisionError:
    print('Error: Invalid argument.')
    

When this program is run, the output looks like this:


21.0
3.5
Error: Invalid argument.

The reason print(spam(1)) is never executed is because once the execution jumps 
to the code in the except clause, it does not return to the try clause. Instead, it just 
continues moving down as normal.

A Short Program: Guess the Number (Writing a Guess the Number Game)
===================================================================
The toy examples I’ve shown you so far are useful for introducing basic concepts, 
but now let’s see how everything you’ve learned comes together in a more 
complete program. In this section, I’ll show you a simple “guess the number” 
game. When you run this program, the output will look something like this:

I am thinking of a number between 1 and 20.
Take a guess.
10
Your guess is too low.
Take a guess.
15
Your guess is too low.
Take a guess.
17
Your guess is too high.
Take a guess.
16
Good job! You guessed my number in 4 guesses!

Type the following source code into the file editor, and save the file as 
guessTheNumber.py:

# This is a guess the number game.
import random
secretNumber = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')

# Ask the player to guess 6 times.
for guessesTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break    # This condition is the correct guess!

if guess == secretNumber:
    print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))
    
    
    
Let’s look at this code line by line, starting at the top.
=========================================================
# This is a guess the number game.
import random
secretNumber = random.randint(1, 20)

First, a comment at the top of the code explains what the program does. Then, the 
program imports the random module so that it can use the random.randint() function 
to generate a number for the user to guess. The return value, a random integer 
between 1 and 20, is stored in the variable secretNumber.

print('I am thinking of a number between 1 and 20.')

# Ask the player to guess 6 times.
for guessesTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())
    
The program tells the player that it has come up with a secret number and will give 
the player six chances to guess it. The code that lets the player enter a guess and 
checks that guess is in a for loop that will loop at most six times. The first thing 
that happens in the loop is that the player types in a guess. Since input() returns a 
string, its return value is passed straight into int(), which translates the string into 
an integer value. This gets stored in a variable named guess.

if guess < secretNumber:
    print('Your guess is too low.')
elif guess > secretNumber:
    print('Your guess is too high.')
These few lines of code check to see whether the guess is less than or greater than 
the secret number. In either case, a hint is printed to the screen.


else:
    break    # This condition is the correct guess!
    
If the guess is neither higher nor lower than the secret number, then it must be 
equal to the secret number, in which case you want the program execution to 
break out of the for loop.

if guess == secretNumber:
    print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))
    
After the for loop, the previous if...else statement checks whether the player has 
correctly guessed the number and prints an appropriate message to the screen. In 
both cases, the program displays a variable that contains an integer value 
(guessesTaken and secretNumber). Since it must concatenate these integer values to 
strings, it passes these variables to the str() function, which returns the string 
value form of these integers. Now these strings can be concatenated with the + 
operators before finally being passed to the print() function call.

Summary
=======
Functions are the primary way to compartmentalize your code into logical groups. 
Since the variables in functions exist in their own local scopes, the code in one 
function cannot directly affect the values of variables in other functions. This 
limits what code could be changing the values of your variables, which can be 
helpful when it comes to debugging your code.

Functions are a great tool to help you organize your code. You can think of them as 
black boxes: They have inputs in the form of parameters and outputs in the form 
of return values, and the code in them doesn’t affect variables in other functions.

In previous chapters, a single error could cause your programs to crash. In this 
chapter, you learned about try and except statements, which can run code when an 
error has been detected. This can make your programs more resilient to common error cases.

"""

print(funkytown)


