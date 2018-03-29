fcs = """
Flow Control Statements
=======================
A flow chart is a good metaphor for how the execution can move around in your program.
Instructions called "Flow control statements" can decide which python instructions to execute under which conditions, nut
before you learn about "Flow control statements", you first need to know about your yes and no options.

Boolean data type only has 2 values, True and False.
Integers and strings effectivley have an infinite number of values, you can just keep making then larger and larger.


Comparison Operators
====================
== Equal to
!= Not equal to
<  Less than
> Greater than
<- Less than or equal to
-> Greater than or equal to

Boolean Operators
=================
and | or | not

The AND Operator's Truth Table
==============================
The AND operator evaluates an expression to True if both Boolean values are True; otherwise, it evaluates to False.
Expression              Evaluates to
-------------           ------------
True and True               True
True and False              False
False and True              False
False and False             False

The OR operator's  Truth Table
===============================
The OR operator evaluates an expression to True if either of the two Boolean values is True. If both are False, it evaluates to False.

Expression              Evaluates to
-------------           ------------
True and True               True
True and False              True
False and True              True
False and False             True

The NOT operator's  Truth Table
=================================
Unlike and and or, the not operator operates on only one Boolean value (or expression).
The not operator simply evaluates to the opposite Boolean value.

not True = False
not False = True


Mixing Boolean and Comparison Operators
=======================================
Since the comparison operators evaluate to Boolean values, you can use them in expressions with the Boolean operators.

Recall that the and, or, and not operators are called Boolean operators because they always operate on the Boolean values True and False.
While expressions like 4 < 5 aren’t Boolean values, they are expressions that evaluate down to Boolean values.

>>> (4 < 5) and (5 < 6)
... (4 < 5) and (9 < 6)
... (1 == 2) or (2 == 2)
True
False
True


"""
print('\n')


print(fcs)

print (42 == 42)

print (True and True)

myAge = 26
myPet = 'cat'
print (myAge > 20 and myPet == 'cat')

print("\n")






