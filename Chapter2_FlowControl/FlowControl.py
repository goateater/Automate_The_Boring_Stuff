fcs = """

Flow Control
=============
So you know the basics of individual instructions and that a program is just a 
series of instructions. But the real strength of programming isn’t just running (or 
executing) one instruction after another like a weekend errand list. Based on how 
the expressions evaluate, the program can decide to skip instructions, repeat them, 
or choose one of several instructions to run. In fact, you almost never want your 
programs to start from the first line of code and simply execute every line, straight 
to the end. Flow control statements can decide which Python instructions to 
execute under which conditions.


These flow control statements directly correspond to the symbols in a flowchart, so 
I’ll provide flowchart versions of the code discussed in this chapter. Figure 2-1 
shows a flowchart for what to do if it’s raining. Follow the path made by the arrows 
from Start to End.

Figure 2-1) https://automatetheboringstuff.com/images/000105.jpg


In a flowchart, there is usually more than one way to go from the start to the end. 
The same is true for lines of code in a computer program. 
Flowcharts represent these branching points with diamonds, while the other steps are represented with rectangles. 
The starting and ending steps are represented with rounded rectangles.

But before you learn about flow control statements, you first need to learn how to represent those yes and no options, 
and you need to understand how to write those branching points as Python code. To that end, let’s explore Boolean values, 
comparison operators, and Boolean operators.


Boolean Values
===============
While the integer, floating-point, and string data types have an unlimited number of possible values, 
the Boolean data type has only two values: True and False. 

(Boolean is capitalized because the data type is named after mathematician George Boole.) 
When typed as Python code, the Boolean values True and False lack the quotes you place around strings, 
and they always start with a capital T or F, with the rest of the word in lowercase. 

Like any other value, Boolean values are used in expressions and can be stored in variables ❶. 
If you don’t use the proper case ❷ or you try to use True and False for variable names ❸, Python will give you an error message.

Comparison Operators
====================
== Equal to
!= Not equal to
<  Less than
> Greater than
<- Less than or equal to
-> Greater than or equal to

Boolean Operators
==================
he three Boolean operators (and, or, and not) are used to compare Boolean values. 
Like comparison operators, they evaluate these expressions down to a Boolean value. 
Let’s explore these operators in detail, starting with the and operator.

Binary Boolean Operators
=========================
The (and) and (or) operators always take two Boolean values (or expressions), so they’re considered binary operators. 
The and operator evaluates an expression to True if both Boolean values are True; otherwise, it evaluates to False. 


The AND Operator's Truth Table
------------------------------
The AND operator evaluates an expression to True if both Boolean values are True; otherwise, it evaluates to False.
Expression              Evaluates to...
-------------           ----------------
True and True               True
True and False              False
False and True              False
False and False             False


The not Operator
================
Unlike and and or, the not operator operates on only one Boolean value (or expression). 
The not operator simply evaluates to the opposite Boolean value.

Much like using double negatives in speech and writing, you can nest not operators ❶, 
though there’s never not no reason to do this in real programs. 

Table 2-4. The not Operator’s Truth Table

Expression      Evaluates to...
---------       ---------------
not True        False           
not False       True


Mixing Boolean and Comparison Operators
========================================
Since the comparison operators evaluate to Boolean values, you can use them in expressions with the Boolean operators.
Recall that the and, or, and not operators are called Boolean operators because they always operate on the Boolean values
True and False. While expressions like 4 < 5 aren’t Boolean values, they are expressions that evaluate down to Boolean values.

The computer will evaluate the left expression first, and then it will evaluate the right expression. 
When it knows the Boolean value for each, it will then evaluate the whole expression down to one Boolean value. 
You can think of the computer’s evaluation process for (4 < 5) and (5 < 6) as shown in Figure 2-2.

You can also use multiple Boolean operators in an expression, along with the comparison operators.

Boolean Order of Operation
==========================
The Boolean operators have an order of operations just like the math operators do. 
After any math and comparison operators evaluate, Python evaluates the not operators first, then the and operators, and then the or operators.


Elements of Flow Control
========================
Flow control statements often start with a part called the condition, and all are followed by a block of code called the clause. 
Before you learn about Python’s specific flow control statements, I’ll cover what a condition and a block are.

Conditions
==========
The Boolean expressions you’ve seen so far could all be considered conditions, which are the same thing as expressions; 
condition is just a more specific name in the context of flow control statements. 

Conditions always evaluate down to a Boolean value, True or False. 
A flow control statement decides what to do based on whether its condition is True or False, 
and almost every flow control statement uses a condition.

Blocks of Code
==============
Lines of Python code can be grouped together in blocks. 
You can tell when a block begins and ends from the indentation of the lines of code. 
There are three rules for blocks.

1) Blocks begin when the indentation increases.
2) Blocks can contain other blocks.
3) Blocks end when the indentation decreases to zero or to a containing block’s indentation.

Blocks are easier to understand by looking at some indented code, so let’s find the blocks in part of a small game program, shown here:


name = 'Mary'
password = 'swordfish'
if name == 'Mary':
    print('Hello Mary')
    if password == 'swordfish':
        print('Access granted.')
    else:
        print('Wrong password.')


The first block of code 
❶ starts at the line print('Hello Mary') and contains all the lines after it. 
Inside this block is another block ❷, which has only a single line in it: print('Access Granted.'). 
The third block ❸ is also one line long: print('Wrong password.').

Program Execution
==================
In the previous chapter’s hello.py program, Python started executing instructions at the top of the program going down, one after another. 
The program execution (or simply, execution) is a term for the current instruction being executed. 
If you print the source code on paper and put your finger on each line as it is executed, you can think of your finger as the program execution.

Not all programs execute by simply going straight down, however. 
If you use your finger to trace through a program with flow control statements, 
you’ll likely find yourself jumping around the source code based on conditions, and you’ll probably skip entire clauses.

Flow Control Statements
=======================
Now, let’s explore the most important piece of flow control: the statements themselves. 
The statements represent the diamonds you saw in the flowchart in Figure 2-1, and they are the actual decisions your programs will make.


if Statements
=============
The most common type of flow control statement is the if statement. 
An if statement’s clause (that is, the block following the if statement) will execute if the statement’s condition is True. 
The clause is skipped if the condition is False.

In plain English, an if statement could be read as, “If this condition is true, execute the code in the clause.” 
In Python, an if statement consists of the following:

* The if keyword
* A condition (that is, an expression that evaluates to True or False)
* A colon
* Starting on the next line, an indented block of code (called the if clause)

For example, let’s say you have some code that checks to see whether someone’s name is Alice. 
(Pretend name was assigned some value earlier.)

if name == 'Alice':
    print('Hi, Alice.')
    
All flow control statements end with a colon and are followed by a new block of code (the clause). 
This if statement’s clause is the block with print('Hi, Alice.'). 

Figure 2-3 shows what a flowchart of this code would look like.

Figure 2-3 -The flowchart for an if statement- https://automatetheboringstuff.com/images/000019.jpg


else Statements
===============
An if clause can optionally be followed by an else statement. 
The else clause is executed only when the if statement’s condition is False. 
In plain English, an else statement could be read as, “If this condition is true, execute this code. Or else, execute that code.” 
An else statement doesn’t have a condition, and in code, an else statement always consists of the following:

* The else keyword
* A colon
* Starting on the next line, an indented block of code (called the else clause)

Returning to the Alice example, let’s look at some code that uses an else statement to offer a different greeting if the person’s name isn’t Alice.

Figure 2-4 shows what a flowchart of this code would look like.

https://automatetheboringstuff.com/images/000106.png


elif Statements
===============
While only one of the if or else clauses will execute, you may have a case where you want one of many possible clauses to execute. 
The elif statement is an “else if” statement that always follows an if or another elif statement. 
It provides another condition that is checked only if all of the previous conditions were False. 
In code, an elif statement always consists of the following:

* The elif keyword
* A condition (that is, an expression that evaluates to True or False)
* A colon
* Starting on the next line, an indented block of code (called the elif clause)

Let’s add an elif to the name checker to see this statement in action.

This time, you check the person’s age, and the program will tell them something different if they’re younger than 12. 
You can see the flowchart for this in Figure 2-5.

Figure 2-5. The flowchart for an elif statement  -- https://automatetheboringstuff.com/images/000107.png

The elif clause executes if age < 12 is True and name == 'Alice' is False. 
However, if both of the conditions are False, then both of the clauses are skipped. 
It is not guaranteed that at least one of the clauses will be executed. 
When there is a chain of elif statements, only one or none of the clauses will be executed. 
Once one of the statements’ conditions is found to be True, the rest of the elif clauses are automatically skipped. 

For example, open a new file editor window and enter the following code, saving it as vampire.py:

Here I’ve added two more elif statements to make the name checker greet a person with different answers based on age. 
Figure 2-6 shows the flowchart for this: https://automatetheboringstuff.com/images/000088.png


The order of the elif statements does matter, however. 
Let’s rearrange them to introduce a bug. 
Remember that the rest of the elif clauses are automatically skipped once a True condition has been found, 
so if you swap around some of the clauses in vampire.py, you run into a problem. 

Change the code to look like the following, and save it as vampire2.py:

Say the age variable contains the value 3000 before this code is executed. 
You might expect the code to print the string 'Unlike you, Alice is not an undead, immortal vampire.'. 
However, because the age > 100 condition is True (after all, 3000 is greater than 100) 
❶, the string 'You are not Alice, grannie.' is printed, and the rest of the elif statements are automatically skipped. 
Remember, at most only one of the clauses will be executed, and for elif statements, the order matters!


Figure 2-7 shows the flowchart for the previous code. 
Notice how the diamonds for age > 100 and age > 2000 are swapped.
https://automatetheboringstuff.com/images/000089.png

Optionally, you can have an else statement after the last elif statement. 
In that case, it is guaranteed that at least one (and only one) of the clauses will be executed. 
If the conditions in every if and elif statement are False, then the else clause is executed. 
For example, let’s re-create the Alice program to use if, elif, and else clauses.

Figure 2-8 shows the flowchart for this new code, which we’ll save as littleKid.py.
https://automatetheboringstuff.com/images/000089.png


In plain English, this type of flow control structure would be, “If the first condition is true, do this. 
Else, if the second condition is true, do that. 
Otherwise, do something else.” 
When you use all three of these statements together, remember these rules about how to order them to avoid bugs like the one in Figure 2-7. 
First, there is always exactly one if statement. 
Any elif statements you need should follow the if statement. 
Second, if you want to be sure that at least one clause is executed, close the structure with an else statement.

Figure 2-7. The flowchart for the vampire2.py program. - https://automatetheboringstuff.com/images/000090.png 
The crossed-out path will logically never happen, because if age were greater than 2000, it would have already been greater than 100.


"""

print(fcs)
print()
print (42 == 42)
print (True and True)
myAge = 26
myPet = 'cat'
print (myAge > 20 and myPet == 'cat')

print()

print("this is the vampire part 1...")
name = 'Dracula'
age = 4000
if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print('You are not Alice, kiddo.')
elif age > 2000:
    print('Unlike you, Alice is not an undead, immortal vampire.')
elif age > 100:
    print('You are not Alice, grannie.')

print()

print("this is the vampire part 2...")
name = 'Dracula'
age = 4000
if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print('You are not Alice, kiddo.')
elif age > 100:
    print('You are not Alice, grannie.')
elif age > 2000:
    print('Unlike you, Alice is not an undead, immortal vampire.')

print()


print("What about Bob?")
name = 'Bob'
age = 30
if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print('You are not Alice, kiddo.')
else:
    print('You are neither Alice nor a little kid.')


