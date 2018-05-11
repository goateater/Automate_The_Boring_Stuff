listsExplained = """

Lists (Lists, Indexes, Slices, and the list() Function)
=======================================================
One more topic you’ll need to understand before you can begin writing programs 
in earnest is the list data type and its cousin, the tuple. Lists and tuples can contain 
multiple values, which makes it easier to write programs that handle large 
amounts of data. And since lists themselves can contain other lists, you can use 
them to arrange data into hierarchical structures.

In this chapter, I’ll discuss the basics of lists. I’ll also teach you about methods, 
which are functions that are tied to values of a certain data type. Then I’ll briefly 
cover the list-like tuple and string data types and how they compare to list values. 
In the next chapter, I’ll introduce you to the dictionary data type.



The List Data Type
==================
A list is a value that contains multiple values in an ordered sequence. The term list 
value refers to the list itself (which is a value that can be stored in a variable or 
passed to a function like any other value), not the values inside the list value. A list 
value looks like this: ['cat', 'bat', 'rat', 'elephant']. Just as string values are 
typed with quote characters to mark where the string begins and ends, a list begins 
with an opening square bracket and ends with a closing square bracket, []. Values 
inside the list are also called items. Items are separated with commas (that is, they 
are comma-delimited). For example, enter the following into the interactive shell:


>>> [1, 2, 3]
[1, 2, 3]
>>> ['cat', 'bat', 'rat', 'elephant']
['cat', 'bat', 'rat', 'elephant']
>>> ['hello', 3.1415, True, None, 42]
['hello', 3.1415, True, None, 42]
❶ >>> spam = ['cat', 'bat', 'rat', 'elephant']
>>> spam
['cat', 'bat', 'rat', 'elephant']

The spam variable ❶ is still assigned only one value: the list value. But the list value 
itself contains other values. The value [] is an empty list that contains no values, 
similar to '', the empty string.


Getting Individual Values in a List with Indexes
=================================================
Say you have the list ['cat', 'bat', 'rat', 'elephant'] stored in a variable 
named spam. The Python code spam[0] would evaluate to 'cat', and spam[1] would 
evaluate to 'bat', and so on. The integer inside the square brackets that follows 
the list is called an index. The first value in the list is at index 0, the second value is 
at index 1, the third value is at index 2, and so on. Figure 4-1 shows a list value 
assigned to spam, along with what the index expressions would evaluate to.

Figure 4-1.
https://automatetheboringstuff.com/images/000074.png
A list value stored in the variable spam, showing which value each index
refers to.

For example, type the following expressions into the interactive shell. Start by 
assigning a list to the variable spam.


   >>> spam = ['cat', 'bat', 'rat', 'elephant']
   >>> spam[0]
   'cat'
   >>> spam[1]
   'bat'
   >>> spam[2]
   'rat'
   >>> spam[3]
   'elephant'
   >>> ['cat', 'bat', 'rat', 'elephant'][3]
   'elephant'
❶ >>> 'Hello ' + spam[0]
❷ 'Hello cat'
   >>> 'The ' + spam[1] + ' ate the ' + spam[0] + '.'
   'The bat ate the cat.'
   
   
Notice that the expression 'Hello ' + spam[0] ❶ evaluates to 'Hello ' + 'cat' 
because spam[0] evaluates to the string 'cat'. This expression in turn evaluates to 
the string value 'Hello cat' ❷.


Python will give you an IndexError error message if you use an index that exceeds 
the number of values in your list value.

>>> spam = ['cat', 'bat', 'rat', 'elephant']
>>> spam[10000]

Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    spam[10000]
IndexError: list index out of range


Indexes can be only integer values, not floats. The following example will cause a 
TypeError error:

>>> spam = ['cat', 'bat', 'rat', 'elephant']
>>> spam[1]
'bat'
>>> spam[1.0]
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    spam[1.0]
TypeError: list indices must be integers, not float
>>> spam[int(1.0)]
'bat'


Lists can also contain other list values. The values in these lists of lists can be 
accessed using multiple indexes, like so:


>>> spam = [['cat', 'bat'], [10, 20, 30, 40, 50]]
>>> spam[0]
['cat', 'bat']
>>> spam[0][1]
'bat'
>>> spam[1][4]
50

spam[0][0]
'cat'
spam[1][0]
10
spam[1][0:3]
[10, 20, 30] 

The first index dictates which list value to use, and the second indicates the value 
within the list value. For example, spam[0][1] prints 'bat', the second value in the 
first list. If you only use one index, the program will print the full list value at that 
index.

Negative Indexes 
=================

While indexes start at 0 and go up, you can also use negative integers for the index.
The integer value -1 refers to the last index in a list, the value -2 refers to the 
second-to-last index in a list, and so on. Enter the following into the interactive 
shell:

>>> spam = ['cat', 'bat', 'rat', 'elephant']
>>> spam[-1]
'elephant'
>>> spam[-3]
'bat'
>>> 'The ' + spam[-1] + ' is afraid of the ' + spam[-3] + '.'
'The elephant is afraid of the bat.'

Getting Sublists with Slices
============================
Just as an index can get a single value from a list, a slice can get several values 
from a list, in the form of a new list. A slice is typed between square brackets, like 
an index, but it has two integers separated by a colon. Notice the difference 
between indexes and slices.

spam[2] is a list with an index (one integer).

spam[1:4] is a list with a slice (two integers).

In a slice, the first integer is the index where the slice starts. The second integer is 
the index where the slice ends. A slice goes up to, but will not include, the value at 
the second index. A slice evaluates to a new list value. Enter the following into the 
interactive shell:


>>> spam = ['cat', 'bat', 'rat', 'elephant']
>>> spam[0:4]
['cat', 'bat', 'rat', 'elephant']
>>> spam[1:3]
['bat', 'rat']
>>> spam[0:-1]
['cat', 'bat', 'rat']

As a shortcut, you can leave out one or both of the indexes on either side of the 
colon in the slice. Leaving out the first index is the same as using 0, or the 
beginning of the list. Leaving out the second index is the same as using the length 
of the list, which will slice to the end of the list. Enter the following into the 
interactive shell:


>>> spam = ['cat', 'bat', 'rat', 'elephant']
>>> spam[:2]
['cat', 'bat']
>>> spam[1:]
['bat', 'rat', 'elephant']
>>> spam[:]
['cat', 'bat', 'rat', 'elephant']


Getting a List’s Length with len()
=================================
The len() function will return the number of values that are in a list value passed 
to it, just like it can count the number of characters in a string value. Enter the 
following into the interactive shell:


>>> spam = ['cat', 'dog', 'moose']
>>> len(spam)
3


Changing Values in a List with Indexes
=======================================
Normally a variable name goes on the left side of an assignment statement, like 
spam = 42. However, you can also use an index of a list to change the value at that 
index. For example, spam[1] = 'aardvark' means “Assign the value at index 1 in 
the list spam to the string 'aardvark'.” Enter the following into the interactive 
shell:

>>> spam = ['cat', 'bat', 'rat', 'elephant']
>>> spam[1] = 'aardvark'
>>> spam
['cat', 'aardvark', 'rat', 'elephant']
>>> spam[2] = spam[1]
>>> spam
['cat', 'aardvark', 'aardvark', 'elephant']
>>> spam[-1] = 12345
>>> spam
['cat', 'aardvark', 'aardvark', 12345]


List Concatenation and List Replication
=======================================
The + operator can combine two lists to create a new list value in the same way it 
combines two strings into a new string value. The * operator can also be used with 
a list and an integer value to replicate the list. Enter the following into the 
interactive shell:


>>> [1, 2, 3] + ['A', 'B', 'C']
[1, 2, 3, 'A', 'B', 'C']
>>> ['X', 'Y', 'Z'] * 3
['X', 'Y', 'Z', 'X', 'Y', 'Z', 'X', 'Y', 'Z']
>>> spam = [1, 2, 3]
>>> spam = spam + ['A', 'B', 'C']
>>> spam
[1, 2, 3, 'A', 'B', 'C']

Removing Values from Lists with del Statements
===============================================
The del statement will delete values at an index in a list. All of the values in the list 
after the deleted value will be moved up one index. For example, enter the 
following into the interactive shell:


>>> spam = ['cat', 'bat', 'rat', 'elephant']
>>> del spam[2]
>>> spam
['cat', 'bat', 'elephant']
>>> del spam[2]
>>> spam
['cat', 'bat']


The del statement can also be used on a simple variable to delete it, as if it were an 
“unassignment” statement. If you try to use the variable after deleting it, you will 
get a NameError error because the variable no longer exists.

In practice, you almost never need to delete simple variables. The del statement is 
mostly used to delete values from lists.

Working with Lists
==================
When you first begin writing programs, it’s tempting to create many individual 
variables to store a group of similar values. For example, if I wanted to store the 
names of my cats, I might be tempted to write code like this:


catName1 = 'Zophie'
catName2 = 'Pooka'
catName3 = 'Simon'
catName4 = 'Lady Macbeth'
catName5 = 'Fat-tail'
catName6 = 'Miss Cleo'

(I don’t actually own this many cats, I swear.) It turns out that this is a bad way to 
write code. For one thing, if the number of cats changes, your program will never 
be able to store more cats than you have variables. These types of programs also 
have a lot of duplicate or nearly identical code in them. Consider how much 
duplicate code is in the following program, which you should enter into the file 
editor and save as allMyCats1.py:


print('Enter the name of cat 1:')
catName1 = input()
print('Enter the name of cat 2:')
catName2 = input()
print('Enter the name of cat 3:')
catName3 = input()
print('Enter the name of cat 4:')
catName4 = input()
print('Enter the name of cat 5:')
catName5 = input()
print('Enter the name of cat 6:')
catName6 = input()
print('The cat names are:')
print(catName1 + ' ' + catName2 + ' ' + catName3 + ' ' + catName4 + ' ' +
catName5 + ' ' + catName6)

Instead of using multiple, repetitive variables, you can use a single variable that 
contains a list value. For example, here’s a new and improved version of the 
allMyCats1.py program. This new version uses a single list and can store any 
number of cats that the user types in. In a new file editor window, type the 
following source code and save it as allMyCats2.py:


catNames = []
while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) +
      ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name] # list concatenation
print('The cat names are:')
for name in catNames:
    print('  ' + name)
    
    
When you run this program, the output will look something like this:


Enter the name of cat 1 (Or enter nothing to stop.):
Zophie
Enter the name of cat 2 (Or enter nothing to stop.):
Pooka
Enter the name of cat 3 (Or enter nothing to stop.):
Simon
Enter the name of cat 4 (Or enter nothing to stop.):
Lady Macbeth
Enter the name of cat 5 (Or enter nothing to stop.):
Fat-tail
Enter the name of cat 6 (Or enter nothing to stop.):
Miss Cleo
Enter the name of cat 7 (Or enter nothing to stop.):

The cat names are:
  Zophie
  Pooka
  Simon
  Lady Macbeth
  Fat-tail
  Miss Cleo
  
The benefit of using a list is that your data is now in a structure,
so your program is much more flexible in processing the data than
it would be with several repetitive variables.

"""

print(listsExplained)

