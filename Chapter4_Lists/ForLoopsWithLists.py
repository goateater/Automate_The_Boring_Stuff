forloopswithlists = """

Using for Loops with Lists 
(for Loops with Lists, Multiple Assignment, Augmented Assignment Operators)
===========================================================================
In Chapter 2, you learned about using for loops to execute a block of code a 
certain number of times. Technically, a for loop repeats the code block once for 
each value in a list or list-like value. For example, if you ran this code:

for i in range(4):
    print(i)

the output of this program would be as follows:

0
1
2
3

This is because the return value from range(4) is a list-like value that Python 
considers similar to [0, 1, 2, 3]. The following program has the same output as 
the previous one:

for i in [0, 1, 2, 3]:
    print(i)


What the previous for loop actually does is loop through its clause with the 
variable i set to a successive value in the [0, 1, 2, 3] list in each iteration.

Note!!
======
In this book, I use the term list-like to refer to data types that are technically 
named sequences. You don’t need to know the technical definitions of this term, though.

A common Python technique is to use range(len(someList)) with a for loop to 
iterate over the indexes of a list. For example, enter the following into the 
interactive shell:


>>> supplies = ['pens', 'staplers', 'flame-throwers', 'binders']
>>> for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

Index 0 in supplies is: pens
Index 1 in supplies is: staplers
Index 2 in supplies is: flame-throwers
Index 3 in supplies is: binders

Using range(len(supplies)) in the previously shown for loop is handy because 
the code in the loop can access the index (as the variable i) and the value at that 
index (as supplies[i]). Best of all, range(len(supplies)) will iterate through all 
the indexes of supplies, no matter how many items it contains.


The in and not in Operators
===========================
You can determine whether a value is or isn’t in a list with the in and not in 
operators. Like other operators, in and not in are used in expressions and connect 
two values: a value to look for in a list and the list where it may be found. These 
expressions will evaluate to a Boolean value. Enter the following into the 
interactive shell:


>>> 'howdy' in ['hello', 'hi', 'howdy', 'heyas']
True
>>> spam = ['hello', 'hi', 'howdy', 'heyas']
>>> 'cat' in spam
False
>>> 'howdy' not in spam
False
>>> 'cat' not in spam
True

For example, the following program lets the user type in a pet name and then 
checks to see whether the name is in a list of pets. Open a new file editor window, 
enter the following code, and save it as myPets.py:

myPets = ['Zophie', 'Pooka', 'Fat-tail']
print('Enter a pet name:')
name = input()
if name not in myPets:
    print('I do not have a pet named ' + name)
else:
    print(name + ' is my pet.')
    
    
The output may look something like this:

Enter a pet name:
Footfoot
I do not have a pet named Footfoot


The Multiple Assignment Trick
==============================
The multiple assignment trick is a shortcut that lets you assign multiple variables 
with the values in a list in one line of code. So instead of doing this:

>>> cat = ['fat', 'orange', 'loud']
>>> size = cat[0]
>>> color = cat[1]
>>> disposition = cat[2]


you could type this line of code:

>>> cat = ['fat', 'orange', 'loud']
>>> size, color, disposition = cat

The number of variables and the length of the list must be exactly equal, or Python 
will give you a ValueError:

>>> cat = ['fat', 'orange', 'loud']
>>> size, color, disposition, name = cat
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    size, color, disposition, name = cat
ValueError: need more than 3 values to unpack


The multiple assignment trick can also be used to swap the values in two variables:

>>> a, b = 'Alice', 'Bob'
>>> a, b = b, a
>>> print(a)
'Bob'
>>> print(b)
'Alice'


Augmented Assignment Operators
===============================
When assigning a value to a variable, you will frequently use the variable itself. For 
example, after assigning 42 to the variable spam, you would increase the value in 
spam by 1 with the following code:

>>> spam = 42
>>> spam = spam + 1
>>> spam
43


As a shortcut, you can use the augmented assignment operator += to do the same 
thing:

>>> spam = 42
>>> spam += 1
>>> spam
43


There are augmented assignment operators for the +, -, *, /, and % operators, described in Table 4-1.
Table 4-1. The Augmented Assignment Operators

Augmented assignment statement      Equivalent assignment statement
==============================      ===============================
spam += 1                               spam = spam + 1
spam -= 1                               spam = spam - 1
spam *= 1                               spam = spam * 1
spam /= 1                               spam = spam / 1
spam %= 1                               spam = spam % 1


The += operator can also do string and list concatenation, and the *= operator can 
do string and list replication. Enter the following into the interactive shell:

>>> spam = 'Hello'
>>> spam += ' world!'
>>> spam
'Hello world!'

>>> bacon = ['Zophie']
>>> bacon *= 3
>>> bacon
['Zophie', 'Zophie', 'Zophie']
"""

print(forloopswithlists)

print('\n')

print("Youtube.com URL: ", "\n", "Using for Loops with Lists", "https://youtu.be/umTnflPbYww")
print('\n')
supplies = ['pens', 'staplers', 'flame-throwers', 'binders']
for i in range(len(supplies)):
    print('Index' + str(i) + ' in supplies is: ' + supplies[i])

print('\n')
print('Boolean Results')
print('---------------')
print('howdy' in ['hello', 'hi', 'howdy', 'heyas'])
spam = ['hello', 'hi', 'howdy', 'heyas']
print('cat' in spam)
print(('howdy' not in spam))
print('cat' not in spam)

print('\n')
spam = 'Hello'
spam += ' World'
print(spam)

print('\n')

bacon = ['Zophie']
bacon *= 3
print(bacon)